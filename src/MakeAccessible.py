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

cmd = doc.GetCommand()

stm = pdfix.CreateFileStream(inputPath + "/make-accessible.json", kPsReadOnly)
if not stm:
    raise Exception(pdfix.GetError())

if not cmd.LoadParamsFromStream(stm, kDataFormatJson):
    raise Exception(pdfix.GetError())
stm.Destroy()

if not cmd.Run():
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/MakeAccessible.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
