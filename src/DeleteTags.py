# delete-tags.py

# Description: Delete tags and level-up children
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

from pdfixsdk import *

from Utils import input_path, jsonToRawData, output_path

# initialize pdfix and open document
pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("tagged.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# delete_tags command params
json_dict = {
    "commands": [
        {
            "name": "delete_tags",
            "params": [
                {
                    "name": "tag_names",
                    "value": "NonStruct, Sect",
                },  # the list of tags to delete
                {
                    "name": "exclude_tag_names",
                    "value": "false",
                },  # exclude/include tags listed above
                {
                    "name": "skip_tag_names",
                    "value": "TH,TD,TR,LI,Lbl,LBody",
                },  # skip tags which should not be deleted
                {
                    "name": "flags",
                    "value": 255,
                },  # flag to process all tags in struct tree
                {"name": "tag_content", "value": "move"},  # move child tags to parent
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

if not doc.Save(output_path.joinpath("DeleteTags.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
