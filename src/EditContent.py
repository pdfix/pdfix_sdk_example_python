from pdfixsdk import *

from Utils import input_path, output_path


# add text to page
def addText(page: PdfPage):
    cropBox = page.GetCropBox()
    matrix = PdfMatrix()
    matrix.e = cropBox.left + 10
    matrix.f = cropBox.bottom + 10

    sys_font = pdfix.FindSysFont("Arial", kFontForceBold, kFontDefANSICodepage)
    if sys_font is None:
        raise RuntimeError(pdfix.GetError())

    font = doc.CreateFont(sys_font, kFontAnsiCharset, 0)
    if font is None:
        raise RuntimeError(pdfix.GetError())

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
pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

# add text to page
addText(page)
addPath(page)

page.Release()

if not doc.Save(output_path / "EditContent.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
