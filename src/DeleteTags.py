# delete-tags.py

# Description: Delete tags and level-up children
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

# import utils to load required shared libraries
from Utils import inputPath, outputPath
import json, ctypes
from pdfixsdk import *

# function to convert json dictionary to c_ubyte array
def jsonToRawData(json_dict):
  json_str = json.dumps(json_dict)
  json_data = bytearray(json_str.encode('utf-8'))
  json_data_size = len(json_str)
  json_data_raw = (ctypes.c_ubyte * json_data_size).from_buffer(json_data)
  return json_data_raw, json_data_size
    
# initialize pdfix and open document
pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/tagged.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# delete_tags command params
json_dict = { 
   "commands": [
      {
        "name": "delete_tags",
        "params": [
            { "name": "tag_names", "value": "NonStruct, Sect" },            # the list of tags to delete
            { "name": "exclude_tag_names", "value": "false" },              # exclude/include tags listed above
            { "name": "skip_tag_names", "value": "TH,TD,TR,LI,Lbl,LBody" }, # skip tags which should not be deleted 
            { "name": "flags", "value": 255 },                              # flag to process all tags in struct tree
            { "name": "tag_content", "value": "move" }                      # move child tags to parent
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

if not doc.Save(outputPath + "/DeleteTags.pdf", kSaveFull):
  raise Exception(pdfix.GetError())

doc.Close()