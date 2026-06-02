# ExtractPages.py
# Example how to use CreateDoc() and InsertPages() to extract page(s) from PDF.

from pdfixsdk import *

# import utils to load required shared libraries
from Utils import inputPath, outputPath

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix Initialization fail")

doc_in = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc_in is None:
    raise RuntimeError("Unable to open pdf : " + pdfix.GetError())

doc_out = pdfix.CreateDoc()
if doc_out is None:
    raise RuntimeError("Unable to create pdf : " + pdfix.GetError())

where_to_insert_index = -1
from_page_index = 1
to_page_index = doc_in.GetNumPages() - 1
result = doc_out.InsertPages(
    where_to_insert_index, doc_in, from_page_index, to_page_index, kPageInsertAll
)

if not result:
    raise RuntimeError("Insert pages fail: " + pdfix.GetError())

if not doc_out.Save(outputPath + "/output.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc_out.Close()
doc_in.Close()
