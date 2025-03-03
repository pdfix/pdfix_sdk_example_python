# ArtifactUntaggedCotnent.py

# Description: Artifact untagged content
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

# import utils to load required shared libraries
from Utils import inputPath, outputPath, jsonToRawData
from pdfixsdk import *

inputPdf = inputPath + "/tagged.pdf"
outputPdf = outputPath + "/ArtifactUntagged.pdf"

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
            "name": "artifact_content",
            "params": [
                {
                    "name": "object_types",                                 # objects to process defined by template
                    "value": {
                        "template": {
                            "object_update": [
                                {
                                    "statement": "$if",
                                    "query": {
                                        "$and": [
                                            {"$0_artifact": "false"},       # object is not tagged
                                            {"$0_mcid": "-1"},              # object does not have assigned mcid
                                        ],
                                        "param": ["pds_object"],
                                    }
                                }
                            ]
                        }
                    },
                },
                {"name": "artifact_type", "value": "0"},                    # mark object as an artifact
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
