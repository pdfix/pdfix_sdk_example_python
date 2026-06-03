# SetFormFieldValue.py
# Example how to fill PDF form.

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

field = doc.GetFormFieldByName("Text1")
if field is not None:
    value = field.GetValue()
    value = "New Value"
    field.SetValue(value)

if not doc.Save(output_path / "SetFormFieldValue.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
