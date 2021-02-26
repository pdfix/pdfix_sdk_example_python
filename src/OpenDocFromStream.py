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
raw_data = (ctypes.c_ubyte * size).from_buffer_copy(data)

# open from memory stream
stm = pdfix.CreateMemStream()
stm.Write(0, raw_data, size)
doc = pdfix.OpenDocFromStream(stm, "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())
doc.Close()

# open from file stream
stm = pdfix.CreateFileStream(inputPath + "/test.pdf", kPsReadOnly)
doc = pdfix.OpenDocFromStream(stm, "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())
doc.Close()
