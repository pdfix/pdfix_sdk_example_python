# UpdateMetadata.py
# Python example for updateing the XMP metadata and document Info dictionary with PDFix SDK

# import utils to load required shared libraries
from Utils import inputPath, outputPath, stream_to_data, bytearray_to_data
from pdfixsdk import *
import ctypes

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# manage document info dictionary
title = doc.GetInfo("Title")
keywords = doc.GetInfo("Keywords")
creator = doc.GetInfo("Creator")
doc.SetInfo("Title", title[::-1]) # reverse string
doc.SetInfo("Keywords", keywords[::-1])
doc.SetInfo("Creator", creator[::-1])

# read/write document XMP metadata
meta_stm_obj = doc.GetMetadata()
byte_array = bytearray(stream_to_data(meta_stm_obj))

# load/modify XMP metadata 
byte_array.extend(bytearray(b'<modified></modified>'))

# write document XMP metadata
raw_data = bytearray_to_data(byte_array)
meta_stm_dict = meta_stm_obj.GetStreamDict().Clone(False)
meta_stm_obj = doc.CreateStreamObject(True, meta_stm_dict, raw_data, size)
doc.GetRootObject().Put("Metadata", meta_stm_obj)

if not doc.Save(outputPath + "/UpdateMetadata.pdf", kSaveFull):
    raise Exception(pdfix.GetError())