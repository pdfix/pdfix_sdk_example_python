# MakeAccessible.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# preflight document for better tagging structure (optional)
tmpl = doc.GetTemplate()
for i in range(0, doc.GetNumPages()):
    tmpl.AddPage(i, 0, None)
tmpl.Update(0, None)

# set the document title and language
title = "Document title"
lang = "en-US"

# run make accessibile
accessibleParams = PdfAccessibleParams()
if not doc.MakeAccessible(accessibleParams, title, lang, 0, None):
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/MakeAccessible.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
