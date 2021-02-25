# Initialization.py
# Pdfix initialization example

import Utils
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
  raise Exception('Pdfix Initialization fail')

# check version
major = pdfix.GetVersionMajor()
minor = pdfix.GetVersionMinor()
patch = pdfix.GetVersionPatch()
print("PDFix SDK Version " + str(major) + "." + str(minor) + "." + str(patch))
