# MakeAccessible.py
# Example how to run the make_accessible batch command.

import json

from pdfixsdk import *

from Utils import input_path, output_path, stream_to_data

commandPath = ""  # input_path / "make-accessible.json"


def extract_json_name(json_text):
    if not json_text:
        return None

    try:
        data = json.loads(json_text)
        return data.get("name")
    except Exception:
        return None


print("GetPdfix...", flush=True)
pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

print("OpenDoc...", flush=True)
doc = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

print("GetCommand...", flush=True)
command = doc.GetCommand()
if command is None:
    raise RuntimeError(pdfix.GetError())

cmdStm = None

try:
    # load the make_accessible command from JSON file
    # or find the embedded custom action named "make_accessible"
    if commandPath == "":
        cmd_count = command.GetNumCustomActions()

        for i in range(cmd_count):
            tmpStm = pdfix.CreateMemStream()
            if tmpStm is None:
                raise RuntimeError(pdfix.GetError())

            try:
                if not command.SaveCustomActionToStream(
                    i, tmpStm, kDataFormatJson, kSaveFull
                ):
                    raise RuntimeError(pdfix.GetError())

                json_text = bytearray(stream_to_data(tmpStm))
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
            raise RuntimeError(
                "Embedded custom action 'make_accessible' was not found."
            )
    else:
        cmdStm = pdfix.CreateFileStream(commandPath, kPsReadOnly)
        if cmdStm is None:
            raise RuntimeError(pdfix.GetError())

    if not command.LoadParamsFromStream(cmdStm, kDataFormatJson):
        raise RuntimeError(pdfix.GetError())

    cmdStm.Destroy()
    cmdStm = None

    # run the command
    print("Running command...", flush=True)
    if not command.Run():
        raise RuntimeError(pdfix.GetError())

    print("Save...", flush=True)
    if not doc.Save(output_path / "MakeAccessible.pdf", kSaveFull):
        raise RuntimeError(pdfix.GetError())
except Exception as e:
    print(f"ERROR: {e}", flush=True)
    raise

finally:
    if cmdStm is not None:
        cmdStm.Destroy()
    doc.Close()
    # pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
    # keeps running but must release PDFix (see Initialization.py, License.py).
