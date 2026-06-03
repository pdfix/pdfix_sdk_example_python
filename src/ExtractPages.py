# ExtractPages.py
# Example how to use CreateDoc() and InsertPages() to extract page(s) from PDF.

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc_in = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc_in is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

doc_out = pdfix.CreateDoc()
if doc_out is None:
    raise RuntimeError(f"Unable to create PDF: {pdfix.GetError()}")

where_to_insert_index = -1
from_page_index = 1
to_page_index = doc_in.GetNumPages() - 1
result = doc_out.InsertPages(
    where_to_insert_index, doc_in, from_page_index, to_page_index, kPageInsertAll
)

if not result:
    raise RuntimeError(f"Unable to insert pages: {pdfix.GetError()}")

if not doc_out.Save(output_path / "output.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc_out.Close()
doc_in.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
