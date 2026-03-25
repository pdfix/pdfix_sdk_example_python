# import utils to load required shared libraries
print("START", flush=True)
import json

from Utils import inputPath, outputPath
print("Loading Pdfix...", flush=True)
from pdfixsdk import *

print("Loading Utils...", flush=True)
import Utils

commandPath = ""  # inputPath + "/make-accessible.json"

print("GetPdfix...", flush=True)
pdfix = GetPdfix()
if pdfix is None:
    raise Exception("Pdfix Initialization fail")

print("OpenDoc...", flush=True)
doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception("Unable to open pdf : " + pdfix.GetError())

print("GetCommand...", flush=True)
command = doc.GetCommand()
if command is None:
    raise Exception(pdfix.GetError())

cmdStm = None


def extract_json_name(json_text):
    if not json_text:
        return None

    try:
        data = json.loads(json_text)
        return data.get("name")
    except Exception:
        return None


try:
    # load the make_accessible command from JSON file
    # or find the embedded custom action named "make_accessible"
    if commandPath == "":
        cmd_count = command.GetNumCustomActions()

        for i in range(cmd_count):
            tmpStm = pdfix.CreateMemStream()
            if tmpStm is None:
                raise Exception(pdfix.GetError())

            try:
                if not command.SaveCustomActionToStream(
                    i, tmpStm, kDataFormatJson, kSaveFull
                ):
                    raise Exception(pdfix.GetError())

                json_text = bytearray(Utils.stream_to_data(tmpStm))
                name = extract_json_name(json_text)

                if name == "make_accessible":
                    cmdStm = tmpStm
                    tmpStm = None
                    break
            except Exception as e:
                print("[WARNING]: Loading JSON command failed. [{}] {}".format(i, e))
            finally:
                if tmpStm is not None:
                    tmpStm.Destroy()

        if cmdStm is None:
            raise Exception("Embedded custom action 'make_accessible' was not found.")
    else:
        cmdStm = pdfix.CreateFileStream(commandPath, kPsReadOnly)
        if cmdStm is None:
            raise Exception(pdfix.GetError())

    if not command.LoadParamsFromStream(cmdStm, kDataFormatJson):
        raise Exception(pdfix.GetError())

    cmdStm.Destroy()
    cmdStm = None

    # run the command
    print("Running command...", flush=True)
    if not command.Run():
        raise Exception(pdfix.GetError())

    print("Save...", flush=True)
    if not doc.Save(outputPath + "/MakeAccessible.pdf", kSaveFull):
        raise Exception(pdfix.GetError())
except Exception as e:
    print(f"ERROR: {e}", flush=True)
    raise    

finally:
    if cmdStm is not None:
        cmdStm.Destroy()
    doc.Close()