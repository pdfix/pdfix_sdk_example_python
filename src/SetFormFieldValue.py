# SetFormFieldValue.py
# Example how to fill PDF form.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

field = doc.GetFormFieldByName("Text1")
if field is not None:
    value = field.GetValue()
    value = "New Value"
    field.SetValue(value)

if not doc.Save(outputPath + "/SetFormFieldValue.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
