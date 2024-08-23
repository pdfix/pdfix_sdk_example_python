# ExtractText.py
# Example how to extract text from PDF.

import json, base64, ctypes
# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

doc_template = doc.GetTemplate();
if doc_template is None:
    raise Exception(pdfix.GetError())

confstm = pdfix.CreateFileStream(inputPath + "/config.json", kPsReadOnly)
if (confstm):
    if doc_template.LoadFromStream(confstm, kDataFormatJson) is False:
        raise Exception(pdfix.GetError())
    confstm.Destroy()

def ImageToBase64(image: PsImage) -> str:
    stm = pdfix.CreateMemStream()
    imageParams = PdfImageParams()
    if not image.SaveToStream(stm, imageParams):
        raise Exception(pdfix.GetError())
    sz = stm.GetSize()
    imageData = bytearray(sz)
    rawData = (ctypes.c_ubyte * sz).from_buffer(imageData)
    stm.Read(0, rawData, len(rawData))
    stm.Destroy()

    imageDataBase64 = base64.b64encode(bytes(rawData)).decode("utf-8")
    return imageDataBase64

def ExtractElemToBase64(elem: PdeElement, node: dict):
    page = elem.GetPageMap().GetPage()
    renderParams = PdfPageRenderParams()
    renderParams.clip_box = elem.GetBBox()

    # size of the image
    pageView = page.AcquirePageView(1, kRotate0)
    rect = pageView.RectToDevice(elem.GetBBox())
    renderParams.image = pdfix.CreateImage(rect.right - rect.left, rect.bottom - rect.top,
        kImageDIBFormatArgb)
    renderParams.matrix = pageView.GetDeviceMatrix()
    pageView.Release()

    # draw content to image
    if not page.DrawContent(renderParams):
        raise Exception(pdfix.GetError())
    
    node["imageData"] = ImageToBase64(renderParams.image)
    renderParams.image.Destroy()
    
def ExtractBBox(bbox: PdfRect, node: dict):
    bboxNode = {}
    bboxNode["left"] = bbox.left
    bboxNode["top"] = bbox.top
    bboxNode["right"] = bbox.right
    bboxNode["bottom"] = bbox.bottom
    node["bbox"] = bboxNode

def ExtractColorState(colorState: PdfColorState, node: dict):
    colorStateNode = {}
    node["colorState"] = colorStateNode

def ExtractTextState(textState: PdfTextState, node: dict):
    textStateNode = {}
    ExtractColorState(textState.color_state, textStateNode)
    if textState.font:
        textStateNode["fontName"] = textState.font.GetFontName()
    textStateNode["fontSize"] = textState.font_size
    node["textState"] = textStateNode

def ExtractTextElement(textElem: PdeText, node: dict):
    textState = textElem.GetTextState()
    ExtractTextState(textState, node)
    node["text"] = textElem.GetText()
    node["style"] = textElem.GetTextStyle()

def ExtractImageElement(imageElem: PdeImage, node: dict):
    imageNode = {}
    ExtractElemToBase64(imageElem, imageNode)
    node["imageData"] = imageNode

# general method to extract element of any type
def ExtractPageElement(elem: PdeElement, node: dict):
    elemType = elem.GetType()
    if kPdeText == elemType:        
        node["type"] = "text"
        ExtractTextElement(PdeText(elem.obj), node)
    elif kPdeImage == elemType:        
        node["type"] = "image"
        ExtractImageElement(PdeImage(elem.obj), node)
    else:
        node["type"] = "Unknown " + str(elemType)
    
    ExtractBBox(elem.GetBBox(), node)

    count = elem.GetNumChildren()
    if count > 0:
        childList = []
        for i in range(0, count):
            child = elem.GetChild(i)
            if child is not None:
                childNode = {} 
                ExtractPageElement(child, childNode)
                childList.append(childNode)
        node["kids"] = childList
            
# prepare the output json
output = {}
pagesList = []

# iterate all pages to extract the content
for i in range(0, doc.GetNumPages()):
    pageNode = {}
    # acquire page
    page = doc.AcquirePage(i)
    if page is None:
        raise Exception('Acquire Page fail : ' + pdfix.GetError())

    # get the page map of the current page
    pageMap = page.AcquirePageMap()    
    if pageMap is None:
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())
    if not pageMap.CreateElements():
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())

    # extract the main page container recursively
    container = pageMap.GetElement()
    if container is None:
        raise Exception('Get page element failure : ' + pdfix.GetError())
    ExtractPageElement(container, pageNode)

    # append all artifacts into the output
    artifactsNode = []
    for j in range(0, pageMap.GetNumArtifacts()):
        artifactNode = {}
        ExtractPageElement(pageMap.GetArtifact(j), artifactNode)
        artifactsNode.append(artifactNode)

    pageNode["artifacts"] = artifactsNode        

    pagesList.append(pageNode)
    pageMap.Release()
    page.Release()
 
output["pageMap"] = pagesList
print(json.dumps(output,indent=2))

doc.Close()
