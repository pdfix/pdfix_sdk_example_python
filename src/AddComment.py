# AddComment.py
# Example how to add a comment with reply into PDF.

from pdfixsdk import (
    GetPdfix,
    PdfRect,
    PdfTextAnnot,
    kAnnotText,
    kSaveFull,
)

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

cropBox = page.GetCropBox()

# place annotation to the middle of the page
annotRect = PdfRect()
annotRect.left = (cropBox.right + cropBox.left) / 2.0 - 10
annotRect.bottom = (cropBox.top + cropBox.bottom) / 2.0 - 10
annotRect.right = (cropBox.right + cropBox.left) / 2.0 + 10
annotRect.top = (cropBox.top + cropBox.bottom) / 2.0 + 10
annot = page.CreateAnnot(kAnnotText, annotRect)
if annot is None:
    raise RuntimeError(pdfix.GetError())
annot.__class__ = PdfTextAnnot
page.AddAnnot(-1, annot)
annot.SetAuthor("Peter Brown")
annot.SetContents("This is my comment.")
annot.AddReply("Mark Fish", "This is some reply.")
page.Release()

if not doc.Save(output_path.joinpath("AddComment.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
