# MakeAccessible.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

commandPath = ""#inputPath + "/make-accessible.json"

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

command = doc.GetCommand()

cmdStm = None

# load the make-accessible command from JSON or use the default
if commandPath == "":
    cmdStm = pdfix.CreateMemStream()
    if not command.SaveCommandsToStream(kActionMakeAccessible, cmdStm, kDataFormatJson, kSaveFull):
        raise Exception(pdfix.GetError())
else:
    cmdStm = pdfix.CreateFileStream(commandPath, kPsReadOnly)
    if not cmdStm:
        raise Exception(pdfix.GetError())

if not command.LoadParamsFromStream(cmdStm, kDataFormatJson):
    raise Exception(pdfix.GetError())

cmdStm.Destroy()

# run the command
if not command.Run():
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/MakeAccessible.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
