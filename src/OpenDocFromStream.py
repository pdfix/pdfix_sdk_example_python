# OpenDocFromStream.py
# Example how to open and save a PDF using streams.

import ctypes

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

with open(input_path / "test.pdf", "rb") as f:
    data = bytearray(f.read())
size = len(data)
raw_data = (ctypes.c_ubyte * size).from_buffer(data)

# open PDF from memory stream
memStm = pdfix.CreateMemStream()
if memStm is None:
    raise RuntimeError(f"Unable to create memory stream: {pdfix.GetError()}")

memStm.Write(0, raw_data, size)
doc = pdfix.OpenDocFromStream(memStm, "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")
doc.Close()
memStm.Destroy()

# open PDF from file stream
fileStm = pdfix.CreateFileStream(str(input_path / "test.pdf"), kPsReadOnly)
if fileStm is None:
    raise RuntimeError(f"Unable to create file stream: {pdfix.GetError()}")

doc = pdfix.OpenDocFromStream(fileStm, "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# save PDF to to stream
saveStm = pdfix.CreateMemStream()
if saveStm is None:
    raise RuntimeError(f"Unable to create memory stream: {pdfix.GetError()}")

if not doc.SaveToStream(saveStm, kSaveFull):
    raise RuntimeError(f"Unable to save PDF: {pdfix.GetError()}")

# write stream to file
data = (ctypes.c_ubyte * saveStm.GetSize())()
saveStm.Read(0, data, len(data))
with open(output_path / "SaveToStream.pdf", "wb") as f:
    f.write(bytearray(data))
saveStm.Destroy()

doc.Close()
fileStm.Destroy()

# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
