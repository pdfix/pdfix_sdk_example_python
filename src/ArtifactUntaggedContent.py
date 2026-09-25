# ArtifactUntaggedCotnent.py

# Description: Artifact untagged content
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

from pdfixsdk import GetPdfix, kDataFormatJson, kSaveFull

from Utils import input_path, jsonToRawData, output_path

inputPdf = input_path.joinpath("tagged.pdf")
outputPdf = output_path.joinpath("ArtifactUntagged.pdf")

# initialize pdfix and open document
pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(inputPdf.as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# delete_tags command params
json_dict = {
    "commands": [
        {
            "name": "artifact_content",
            "params": [
                {
                    "name": "object_types",  # objects to process defined by template
                    "value": {
                        "template": {
                            "object_update": [
                                {
                                    "statement": "$if",
                                    "query": {
                                        "$and": [
                                            {
                                                "$0_artifact": "false"
                                            },  # object is not tagged
                                            {
                                                "$0_mcid": "-1"
                                            },  # object does not have assigned mcid
                                        ],
                                        "param": ["pds_object"],
                                    },
                                }
                            ]
                        }
                    },
                },
                {"name": "artifact_type", "value": "0"},  # mark object as an artifact
            ],
        }
    ]
}

# prepare the command
json_data, json_size = jsonToRawData(json_dict)
memStm = pdfix.CreateMemStream()
if memStm is None:
    raise RuntimeError(pdfix.GetError())

memStm.Write(0, json_data, json_size)

command = doc.GetCommand()
if command is None:
    raise RuntimeError(pdfix.GetError())

if not command.LoadParamsFromStream(memStm, kDataFormatJson):
    raise RuntimeError(pdfix.GetError())

memStm.Destroy()

# execute command
if not command.Run():
    raise RuntimeError(f"Unable to run command: {pdfix.GetError()}")

if not doc.Save(outputPdf.as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
