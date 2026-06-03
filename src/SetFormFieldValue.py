# SetFormFieldValue.py
# Example how to fill PDF form.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

pdfix  = GetPdfix()
if pdfix is None:
    raise RuntimeError('Pdfix initialization failed')

doc = pdfix.OpenDoc(f"{inputPath}/test.pdf", "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')

field = doc.GetFormFieldByName("Text1")
if field is not None:
    value = field.GetValue()
    value = "New Value"
    field.SetValue(value)

if not doc.Save(f"{outputPath}/SetFormFieldValue.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
