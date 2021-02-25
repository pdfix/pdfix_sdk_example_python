# AddWatermark.py 
# Example how to extract text from PDF.

# import initialization to load required shared libraries
from Initialization import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# TODO:

doc.Close()
