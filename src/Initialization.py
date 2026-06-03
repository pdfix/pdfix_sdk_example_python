# Initialization.py
# Pdfix initialization example

import Utils
from pdfixsdk import *

pdfix  = GetPdfix()
if pdfix is None:
  raise RuntimeError('Pdfix initialization failed')

# check version
major = pdfix.GetVersionMajor()
minor = pdfix.GetVersionMinor()
patch = pdfix.GetVersionPatch()
print(f"PDFix SDK Version {major}.{minor}.{patch}")

pdfix.Destroy()

