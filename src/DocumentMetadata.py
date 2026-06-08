# DocumentMetadata.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

import ctypes

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

title = doc.GetInfo("Title")
doc.SetInfo("Title", "My next presenttion")

metaStm = doc.GetMetadata()
if metaStm is None:
    raise RuntimeError(f"Unable to read document metadata: {pdfix.GetError()}")

sz = metaStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
metaStm.Read(0, rawData, len(rawData))

stm = pdfix.CreateFileStream(
    output_path.joinpath("DocumentMetadata.xml").as_posix(), kPsTruncate
)
if stm is None:
    raise RuntimeError(f"Unable to open output file: {pdfix.GetError()}")
stm.Write(0, rawData, len(rawData))
stm.Destroy()

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
