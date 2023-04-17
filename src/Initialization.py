# Initialization.py
# Pdfix initialization example

import Utils
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
  raise Exception('Pdfix Initialization fail')

# check version
major = pdfix.GetVersionMajor()
minor = pdfix.GetVersionMinor()
patch = pdfix.GetVersionPatch()
print("PDFix SDK Version " + str(major) + "." + str(minor) + "." + str(patch))

# ACCOUNT LICENSE

# authorization using email and license key
# account autorization must be used each time the SDK is used
if not pdfix.GetAccountAuthorization().Authorize("YOUR LICENSE NAME", "YOUR LICENSE KEY"):
  print("dummy message: PDFix SDK not authorized")


# STANDARD LICENSE

# activation of the license using activation key
# standard autorization stores the license data locally and shluld be used only once
if not pdfix.GetStandardAuthorization().Activate("ACTIVATION KEY"):
  print("dummy message: PDFix SDK not activated")

# deactivation of the standard license
if not pdfix.GetStandardAuthorization().Deactivate():
  print("dummy message: PDFix SDK not deactivated")
