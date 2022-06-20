# AddTags.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

tagsParams = PdfTagsParams()
if not doc.AddTags(tagsParams, 0, None):
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/AddTags.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
