# PDF to JSON conversion example 

import shutil, os, ctypes
from pdfixsdk import *

# import utils to load required shared libraries
from Utils import inputPath, outputPath

pdfix = GetPdfix()

# open tagged PDF
doc = pdfix.OpenDoc(inputPath + "/input.pdf", "")

# prepare PDF to JSON conversion
jsonConv = doc.CreateJsonConversion()
params = PdfJsonParams()
params.flags = kJsonExportStructTree  # see PdfJsonFlags flagss to extract other content

# extract data to stream
memStm = pdfix.CreateMemStream()
jsonConv.SaveToStream(memStm)

# read memmory stream into bytearray
sz = memStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
memStm.Read(0, rawData, len(rawData))

# cleanup
memStm.Destroy()
doc.Close()

