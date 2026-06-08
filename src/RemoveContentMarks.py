# RemoveContentMarks.py

# Description: Remove content marks with invalid MCID from content
# https://pdfix.net/pdfix-batch-commands/#delete_tags

# Installation:
# pip install pdfix-sdk

from pdfixsdk import *

from Utils import input_path, jsonToRawData, output_path

inputPdf = input_path.joinpath("tagged.pdf")
outputPdf = output_path.joinpath("RemoveContentMarks.pdf")

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
            "name": "remove_content_marks",
            "params": [
                {"name": "object_types", "value": ".*"},  # all object types
                {"name": "flags", "value": "8"},  # objects with an invalid mcid
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
