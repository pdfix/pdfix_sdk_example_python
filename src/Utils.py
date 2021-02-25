# Utils.py
# Pdfix utils

import platform, os
from Pdfix import Pdfix_init
from PdfToHtml import PdfToHtml_init
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
PdfToHtml_init(basePath + "/" + getModuleName('pdf_to_html'))
OcrTesseract_init(basePath + "/" + getModuleName('ocr_tesseract'))

inputPath = basePath + "/../resources"
outputPath = basePath + "/../output"
if not os.path.isdir(outputPath): 
  os.mkdir(outputPath)

