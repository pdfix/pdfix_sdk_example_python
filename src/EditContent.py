from pdfixsdk.Pdfix import *

# import utils to load required shared libraries
from Utils import inputPath, outputPath

# add text to page
def addText(page: PdfPage):
    cropBox = page.GetCropBox()
    matrix = PdfMatrix()
    matrix.e = cropBox.left + 10
    matrix.f = cropBox.bottom + 10

    sys_font = pdfix.FindSysFont("Arial", kFontForceBold, kFontDefANSICodepage)
    font = doc.CreateFont(sys_font, kFontAnsiCharset, 0)
    sys_font.Destroy()

    content = page.GetContent()
    text_obj = content.AddNewText(-1, font, matrix)
    text_obj.SetText("Sample text")

# add path to page
def addPath(page: PdfPage): 
    cropBox = page.GetCropBox()
    matrix = PdfMatrix()
    matrix.e = cropBox.left
    matrix.f = cropBox.bottom

    content = page.GetContent()
    path_obj = content.AddNewPath(-1, matrix)
    pt = PdfPoint()
    pt.x = 0
    pt.y = 0
    path_obj.MoveTo(pt)
    pt.x = 100
    pt.y = 100
    path_obj.LineTo(pt)
    pt.y = 0
    path_obj.LineTo(pt)
    pt.x = 0
    pt.y = 100
    path_obj.LineTo(pt)
    path_obj.ClosePath()

    path_obj.SetStroke(True)
    path_obj.SetFillType(kFillRuleEvenOdd)
    

# content editing example 
pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

page = doc.AcquirePage(0)
if page is None:
    raise Exception('Unable to acquire page : ' + pdfix.GetError())

# add text to page
addText(page)
addPath(page)

page.Release()

if not doc.Save(outputPath + "/EditContent.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()

