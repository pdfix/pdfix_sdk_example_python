# TagAs.py
# Example for tagging content in an area on page 1 as Figure

import json

from pdfixsdk import *

from Utils import bytearray_to_data, input_path, output_path

cmd = {
    "commands": [
        {
            "name": "tag_content",
            "params": [
                {
                    "name": "object_types",
                    "value": {
                        "template": {
                            "object_update": [
                                {
                                    "query": {
                                        "$and": [
                                            {"$page_num": "1"},
                                            {"$0_left": {"$gte": "47.27"}},
                                            {"$0_right": {"$lte": "553.02"}},
                                            {"$0_top": {"$lte": "700.03"}},
                                            {"$0_bottom": {"$gte": "525.91"}},
                                        ],
                                        "param": ["pds_object"],
                                    },
                                    "statement": "$if",
                                }
                            ]
                        }
                    },
                },
                {"name": "tag_name", "value": "Figure"},
            ],
        }
    ]
}

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")
doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# prepare the command data
cmdData = json.dumps(cmd).encode()
with open(output_path.joinpath("TagAs.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(cmd, indent=2))

data = bytearray_to_data(bytearray(json.dumps(cmd).encode()))

memStm = pdfix.CreateMemStream()
if memStm is None:
    raise RuntimeError(pdfix.GetError())
memStm.Write(0, data, len(data))

command = doc.GetCommand()
if command is None:
    raise RuntimeError(pdfix.GetError())

if not command.LoadParamsFromStream(memStm, kDataFormatJson):
    raise RuntimeError(pdfix.GetError())

# run the command
if not command.Run():
    raise RuntimeError(pdfix.GetError())

# cleanup
memStm.Destroy()
if not doc.Save(output_path.joinpath("TagAs.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())
doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
