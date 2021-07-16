# AddComment.py
# Example how to add a comment with reply into PDF.

import os

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

page = doc.AcquirePage(0)
if page is None:
    raise Exception('Unable to acquire page : ' + pdfix.GetError())

cropBox = page.GetCropBox()

# place annotation to the middle of the page
annotRect = PdfRect()
annotRect.left = (cropBox.right + cropBox.left) / 2.0 - 10
annotRect.bottom = (cropBox.top + cropBox.bottom) / 2.0 - 10
annotRect.right = (cropBox.right + cropBox.left) / 2.0 + 10
annotRect.top = (cropBox.top + cropBox.bottom) / 2.0 + 10
annot = page.CreateAnnot(kAnnotText, annotRect)
annot.__class__ = PdfTextAnnot
page.AddAnnot(-1, annot)
if annot is None:
    raise Exception(pdfix.GetError())
annot.SetAuthor("Peter Brown")
annot.SetContents("This is my comment.")
annot.AddReply("Mark Fish", "This is some reply.")
page.Release()

if not doc.Save(outputPath + "/AddComment.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
