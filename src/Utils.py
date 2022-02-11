# Utils.py
# Pdfix utils

import platform, os, math
from Pdfix import Pdfix_init
from OcrTesseract import OcrTesseract_init
from Pdfix import *

# get the shared library name based on the platform
def getModuleName(module):
  pltfm = platform.system()
  if pltfm == 'Darwin':
    return 'lib' + module + '.dylib'
  elif pltfm == "Windows":
    return module + '.dll'
  elif pltfm == "Linux":
    return 'lib' + module + '.so'

# load pdfix library from the current folder
basePath = os.path.dirname(os.path.abspath(__file__))
Pdfix_init(basePath + "/" + getModuleName('pdfix'))
OcrTesseract_init(basePath + "/" + getModuleName('ocr_tesseract'))

inputPath = basePath + "/../resources"
outputPath = basePath + "/../output"
if not os.path.isdir(outputPath): 
  os.mkdir(outputPath)

kPi = 3.1415926535897932384626433832795

def PdfMatrixConcat(m:PdfMatrix, m1:PdfMatrix, prepend:bool):
  ret = PdfMatrix()
  if (prepend):
    swap = m
    m = m1
    m1 = swap
  ret.a = m.a * m1.a + m.b * m1.c
  ret.b = m.a * m1.b + m.b * m1.d
  ret.c = m.c * m1.a + m.d * m1.c
  ret.d = m.c * m1.b + m.d * m1.d
  ret.e = m.e * m1.a + m.f * m1.c + m1.e
  ret.f = m.e * m1.b + m.f * m1.d + m1.f
  return ret

def PdfMatrixRotate(m:PdfMatrix, radian:float, prepend:bool):
  cosValue = math.cos(radian)
  sinValue = math.sin(radian)
  m1 = PdfMatrix()
  m1.a = cosValue
  m1.b = sinValue
  m1.c = -sinValue
  m1.d = cosValue
  return PdfMatrixConcat(m, m1, prepend)

def PdfMatrixTranslate(m:PdfMatrix, x:float, y:float, prepend:bool):
  ret = m
  if prepend:
    ret.e = m.e + x * m.a + y + m.c
    ret.f = m.f + y * m.d + x * m.b
  ret.e = m.e + x
  ret.f = m.f + y
  return ret
   

def PdfMatrixInverse(orig:PdfMatrix):
  inverse = PdfMatrix()
  i = orig.a * orig.d - orig.b * orig.c
  if abs(i) == 0:
    return inverse
  j = -i
  inverse.a = orig.d / i
  inverse.b = orig.b / j
  inverse.c = orig.c / j
  inverse.d = orig.a / i
  inverse.e = (orig.c * orig.f - orig.d * orig.e) / i
  inverse.f = (orig.a * orig.f - orig.b * orig.e) / j
  return inverse

