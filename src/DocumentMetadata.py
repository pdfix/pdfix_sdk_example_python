# DocumentMetadata.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *
import ctypes  

pdfix  = GetPdfix()
if pdfix is None:
    raise RuntimeError('Pdfix initialization failed')

doc = pdfix.OpenDoc(f"{inputPath}/test.pdf", "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')

title = doc.GetInfo("Title")
doc.SetInfo("Title", "My next presenttion")

metaStm = doc.GetMetadata()
if metaStm is None:
    raise RuntimeError(f'Unable to read document metadata: {pdfix.GetError()}') 

sz = metaStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
metaStm.Read(0, rawData, len(rawData))

stm = pdfix.CreateFileStream(f"{outputPath}/DocumentMetadata.xml", kPsTruncate)
if stm is None:
    raise RuntimeError(f'Unable to open output file: {pdfix.GetError()}') 
stm.Write(0, rawData, len(rawData))
stm.Destroy()

doc.Close()
