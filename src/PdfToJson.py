# PDF to JSON conversion example 

import shutil, os, ctypes
from pdfixsdk import *

# import utils to load required shared libraries
from Utils import inputPath, outputPath

pdfix = GetPdfix()

# open tagged PDF
doc = pdfix.OpenDoc(inputPath + "/tagged.pdf", "")

# prepare PDF to JSON conversion params
params = PdfJsonParams()
params.flags = (kJsonExportStructTree | kJsonExportDocInfo | kJsonExportBBox | kJsonExportText)  # see PdfJsonFlags flagss to extract other conten

# prepare PDF to JSON conversion
jsonConv = doc.CreateJsonConversion()
jsonConv.SetParams(params)

# extract data to stream
memStm = pdfix.CreateMemStream()
jsonConv.SaveToStream(memStm)

# read memmory stream into bytearray
sz = memStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
memStm.Read(0, rawData, len(rawData))

print(data.decode("utf-8"))

# cleanup
memStm.Destroy()
doc.Close()

