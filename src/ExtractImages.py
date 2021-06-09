# ExtractImages.py
# Example how to extract images from PDF.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

imageIndex = 1
def SaveImage(pdfix, page, element):
    global imageIndex, outputPath
    elem_type = element.GetType()
    if (elem_type == kPdeImage):
        image = PdeImage(element.obj)
        bbox = image.GetBBox()

        pageView = page.AcquirePageView(2.0, kRotate0)
        devRect = pageView.RectToDevice(bbox)

        # prepare image 
        psImage = pdfix.CreateImage(pageView.GetDeviceWidth(), pageView.GetDeviceHeight(), kImageDIBFormatArgb)        
        renderParams = PdfPageRenderParams()
        renderParams.clip_box = bbox
        renderParams.image = image
        renderParams.matrix = pageView.GetDeviceMatrix()
        page.DrawContent(renderParams, 0, None)

        # save image to file
        path = outputPath + "/ExtractImages_" + str(imageIndex) + ".png"

        imageParams = PdfImageParams()
        psImage.SaveRect(path, imageParams, devRect)
        psImage.Destroy()

        imageIndex += 1        
    else:
        count = element.GetNumChildren()
        if (count == 0):
            return
        for i in range(count):
            child = element.GetChild(i)
            if child:
                SaveImage(pdfix, page, child)

# iterate pages to search for images
for i in range(0, doc.GetNumPages()):
    # acquire page
    page = doc.AcquirePage(i)
    if page is None:
        raise Exception('Acquire Page fail : ' + pdfix.GetError())
    
    # get the page map of the current page
    pageMap = page.AcquirePageMap()    
    if pageMap is None:
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())
    if not pageMap.CreateElements(0, None):
        raise Exception('Acquire PageMap fail: ' + pdfix.GetError())
    
    # get page container
    container = pageMap.GetElement()    
    if container is None:
        raise Exception('Get page element failure : ' + pdfix.GetError())
    
    SaveImage(pdfix, page, container)
    page.Release()

print(str(imageIndex - 1) + " images found")
doc.Close()
