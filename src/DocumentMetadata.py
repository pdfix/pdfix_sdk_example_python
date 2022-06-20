# DocumentMetadata.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *
import ctypes  

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

title = doc.GetInfo("Title")
doc.SetInfo("Title", "My next presenttion")

metaStm = doc.GetMetadata()
if metaStm is None:
    raise Exception('Unable to read document metadata: ' + pdfix.GetError()) 

sz = metaStm.GetSize()
data = bytearray(sz)
rawData = (ctypes.c_ubyte * sz).from_buffer(data)
metaStm.Read(0, rawData, len(rawData))

stm = pdfix.CreateFileStream(outputPath + "/DocumentMetadata.xml", kPsTruncate)
if stm is None:
    raise Exception('Unable to open output file : ' + pdfix.GetError()) 
stm.Write(0, rawData, len(rawData))
stm.Destroy()

doc.Close()
