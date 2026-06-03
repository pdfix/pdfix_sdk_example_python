# UpdateMetadata.py
# Python example for updateing the XMP metadata and document Info dictionary with PDFix SDK

# import utils to load required shared libraries

from pdfixsdk import *

from Utils import bytearray_to_data, inputPath, outputPath, stream_to_data

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(f"{inputPath}/test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# manage document info dictionary
title = doc.GetInfo("Title")
keywords = doc.GetInfo("Keywords")
creator = doc.GetInfo("Creator")
doc.SetInfo("Title", title[::-1])  # reverse string
doc.SetInfo("Keywords", keywords[::-1])
doc.SetInfo("Creator", creator[::-1])

# read/write document XMP metadata
meta_stm_obj = doc.GetMetadata()
if meta_stm_obj is None:
    raise RuntimeError(f"Unable to read document metadata: {pdfix.GetError()}")

byte_array = bytearray(stream_to_data(meta_stm_obj))

# load/modify XMP metadata
byte_array.extend(bytearray(b"<modified></modified>"))

# write document XMP metadata
size = len(byte_array)
raw_data = bytearray_to_data(byte_array)
meta_stm_dict = meta_stm_obj.GetStreamDict().Clone(False)
if meta_stm_dict is None:
    raise RuntimeError(pdfix.GetError())

meta_stm_obj = doc.CreateStreamObject(True, meta_stm_dict, raw_data, size)
if meta_stm_obj is None:
    raise RuntimeError(pdfix.GetError())

doc.GetRootObject().Put("Metadata", meta_stm_obj)

if not doc.Save(f"{outputPath}/UpdateMetadata.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
