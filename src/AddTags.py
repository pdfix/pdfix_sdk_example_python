# AddTags.py
from Pdfix import *

# import initialization to load required shared libraries
from Initialization import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

if not doc.AddTags(0, None):
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/AddTags.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
