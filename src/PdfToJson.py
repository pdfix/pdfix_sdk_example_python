# PDF to JSON conversion example

import ctypes

from pdfixsdk import *

# import utils to load required shared libraries
from Utils import inputPath

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

# open tagged PDF
doc = pdfix.OpenDoc(f"{inputPath}/tagged.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# prepare PDF to JSON conversion params
params = PdfJsonParams()
params.flags = (
    kJsonExportStructTree | kJsonExportDocInfo | kJsonExportBBox | kJsonExportText
)  # see PdfJsonFlags flagss to extract other conten

# prepare PDF to JSON conversion
jsonConv = doc.CreateJsonConversion()
if jsonConv is None:
    raise RuntimeError(f"Unable to create JSON conversion: {pdfix.GetError()}")

if not jsonConv.SetParams(params):
    raise RuntimeError(f"Unable to set JSON conversion parameters: {pdfix.GetError()}")

# extract data to stream
memStm = pdfix.CreateMemStream()
if memStm is None:
    raise RuntimeError(pdfix.GetError())

if not jsonConv.SaveToStream(memStm):
    raise RuntimeError(f"Unable to save JSON to stream: {pdfix.GetError()}")

# read memmory stream into bytearray
sz = memStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
memStm.Read(0, rawData, len(rawData))

print(data.decode("utf-8"))

# cleanup
memStm.Destroy()
doc.Close()
