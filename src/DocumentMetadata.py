# DocumentMetadata.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

title = doc.GetInfo("Title")
doc.SetInfo("Title", "My next presenttion")

stm = pdfix.CreateFileStream(outputPath + "DocumentMetadata.xml", kPsTruncate)
if stm is None:
    raise Exception('Unable to open output file : ' + pdfix.GetError()) 

metadata = doc.GetMetadata()
if metadata is None:
    raise Exception('Unable to read document metadata: ' + pdfix.GetError()) 

if not metadata.SaveToStream(stm):
    raise Exception('Unable to save metadata : ' + pdfix.GetError()) 
stm.Destroy()
doc.Close()
