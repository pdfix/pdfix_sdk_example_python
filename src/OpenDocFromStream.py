# OpenDocFromStream.py 
# Example how to extract text from PDF.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *
import ctypes  

pdfix  = GetPdfix()
if pdfix is None:
    raise RuntimeError('Pdfix initialization failed')

f = open(f"{inputPath}/test.pdf", "rb")
data = bytearray(f.read())
size = f.tell()
f.close()
raw_data = (ctypes.c_ubyte * size).from_buffer(data)

# open PDF from memory stream
memStm = pdfix.CreateMemStream()
if memStm is None:
    raise RuntimeError(f'Unable to create memory stream: {pdfix.GetError()}')

memStm.Write(0, raw_data, size)
doc = pdfix.OpenDocFromStream(memStm, "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')
doc.Close()
memStm.Destroy()

# open PDF from file stream
fileStm = pdfix.CreateFileStream(f"{inputPath}/test.pdf", kPsReadOnly)
if fileStm is None:
    raise RuntimeError(f'Unable to create file stream: {pdfix.GetError()}')

doc = pdfix.OpenDocFromStream(fileStm, "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')

# save PDF to to stream
saveStm = pdfix.CreateMemStream()
if saveStm is None:
    raise RuntimeError(f'Unable to create memory stream: {pdfix.GetError()}')

if not doc.SaveToStream(saveStm, kSaveFull):
    raise RuntimeError(f'Unable to save PDF: {pdfix.GetError()}')

# write stream to file
data = (ctypes.c_ubyte * saveStm.GetSize())()
saveStm.Read(0, data, len(data))
f = open(f"{outputPath}/SaveToStream.pdf", "wb")
f.write(data)
f.close()
saveStm.Destroy()

doc.Close()
fileStm.Destroy()
