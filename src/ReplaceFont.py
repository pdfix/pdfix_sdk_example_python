# ReplaceFont.py
# Copyright (c) 2024 PDFix. All Rights Reserved.

# Code example for replacing the font in a PDF

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *
import ctypes, json

# function to convert json dictionary to c_ubyte array
def jsonToRawData(json_dict):
  json_str = json.dumps(json_dict)
  json_data = bytearray(json_str.encode('utf-8'))
  json_data_size = len(json_str)
  json_data_raw = (ctypes.c_ubyte * json_data_size).from_buffer(json_data)
  return json_data_raw, json_data_size

pdfix = GetPdfix()

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# delete_tags command params
json_dict = { 
   "commands": [
      {
        "name": "replace_font",
        "params": [
            { "name": "font_name", "value": "TimesNewRomanPS" },            # The font name in PDF to be replaced (regex)
            { "name": "font_family", "value": "Calibri" }                   # The font family to be used as a replacement
          ] 
      }
   ]
}

# prepare the command
json_data, json_size = jsonToRawData(json_dict)
memStm = pdfix.CreateMemStream()
memStm.Write(0, json_data, json_size)

command = doc.GetCommand()
command.LoadParamsFromStream(memStm, kDataFormatJson)
memStm.Destroy()

# execute command
if not command.Run():
    raise Exception('Unable to run command DeleteTags : ' + str(pdfix.GetError()))

if not doc.Save(outputPath + "/ReplaceFont.pdf", kSaveFull):
  raise Exception(pdfix.GetError())

doc.Close()