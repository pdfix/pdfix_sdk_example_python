# Initialization.py
# Pdfix initialization example

from pdfixsdk import *

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

# check version
major = pdfix.GetVersionMajor()
minor = pdfix.GetVersionMinor()
patch = pdfix.GetVersionPatch()
print(f"PDFix SDK Version {major}.{minor}.{patch}")

# Destroy() releases the SDK (native library, license slots) while this process keeps
# running. One-shot document examples omit Destroy() and exit after doc.Close().
pdfix.Destroy()
