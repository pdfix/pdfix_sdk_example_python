# License.py
# Pdfix license management
from pdfixsdk import *
from Utils import stream_to_data
import json

pdfix = GetPdfix()

# STANDARD LICENSE (ACTIVATION)
# activation of the license using activation key
# standard autorization stores the license data locally and shluld be used only once
if not pdfix.GetStandardAuthorization().Activate("LICENSE KEY"):
  print("dummy message: PDFix SDK not activated")

# deactivation of the standard license on a computer
if not pdfix.GetStandardAuthorization().Deactivate():
  print("dummy message: PDFix SDK not deactivated")



# ACCOUNT LICENSE
# authorization using name and license key
# account autorization must be used each time the Pdfix object is constructed (once per run)
if not pdfix.GetAccountAuthorization().Authorize("YOUR LICENSE NAME", "YOUR LICENSE KEY"):
  print("dummy message: PDFix SDK not authorized")


# LICESNE STATUS
# read the license status
mem_stm = pdfix.CreateMemStream()
pdfix.GetStandardAuthorization().SaveToStream(mem_stm, kDataFormatJson)
bytes = bytearray(stream_to_data(mem_stm))
print(json.dumps(bytes.decode("utf-8"), indent=2))
mem_stm.Destroy()
