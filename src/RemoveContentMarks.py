# RemoveContentMarks.py

# Description: Remove content marks with invalid MCID from content
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

# import utils to load required shared libraries
from Utils import inputPath, outputPath, jsonToRawData
from pdfixsdk import *

inputPdf = inputPath + "/tagged.pdf"
outputPdf = outputPath + "/RemoveContentMarks.pdf"

# initialize pdfix and open document
pdfix = GetPdfix()
if pdfix is None:
    raise Exception("Pdfix Initialization fail")

doc = pdfix.OpenDoc(inputPdf, "")
if doc is None:
    raise Exception("Failed to open pdf : " + str(pdfix.GetError()))

# delete_tags command params
json_dict = {
    "commands": [
        {
            "name": "remove_content_marks",
            "params": [
                { "name": "object_types", "value": ".*" },                  # all object types
                { "name": "flags", "value": "8" }                           # objects with an invalid mcid
            ],
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
    raise Exception("Failed to run commend: " + pdfix.GetError())

if not doc.Save(outputPdf, kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
