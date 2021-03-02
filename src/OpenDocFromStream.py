# OpenDocFromStream.py 
# Example how to extract text from PDF.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from Pdfix import *
import ctypes  

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

f = open(inputPath + "/test.pdf", "rb")
data = bytearray(f.read())
size = f.tell()
f.close()
raw_data = (ctypes.c_ubyte * size).from_buffer(data)

# open PDF from memory stream
memStm = pdfix.CreateMemStream()
memStm.Write(0, raw_data, size)
doc = pdfix.OpenDocFromStream(memStm, "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())
doc.Close()
memStm.Destroy()

# open PDF from file stream
fileStm = pdfix.CreateFileStream(inputPath + "/test.pdf", kPsReadOnly)
doc = pdfix.OpenDocFromStream(fileStm, "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# save PDF to to stream
saveStm = pdfix.CreateMemStream()
if not doc.SaveToStream(saveStm, kSaveFull):
    raise Exception('Unable to save pdf : ' + pdfix.GetError())

# write stream to file
data = (ctypes.c_ubyte * saveStm.GetSize())()
saveStm.Read(0, data, len(data))
f = open(outputPath + "/SaveToStream.pdf", "wb")
f.write(data)
f.close()
saveStm.Destroy()

doc.Close()
fileStm.Destroy()
