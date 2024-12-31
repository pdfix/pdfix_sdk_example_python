# TagAs.py
# Example for tagging content in an area on page 1 as Figure

from pdfixsdk import *
import json
from Utils import inputPath, outputPath, bytearray_to_data

cmd = {
    "commands": [
        {
            "name": "tag_as",
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
doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")

# prepare the command data
cmdData = json.dumps(cmd).encode()
with open(outputPath + "/TagAs.json", "w") as f:
    f.write(json.dumps(cmd, indent=2))

data = bytearray_to_data(bytearray(json.dumps(cmd).encode()))

memStm = pdfix.CreateMemStream()
memStm.Write(0, data, len(data))

command = doc.GetCommand()
command.LoadParamsFromStream(memStm, kDataFormatJson)

# run the command
command.Run()

# cleanup
memStm.Destroy()
doc.Save(outputPath + "/TagAs.pdf", kSaveFull)
