# AddWatermark.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage AddWatermark_py 
# \page AddWatermark_py Extract Text Sample
# Example how to extract text from PDF.
# \snippet /AddWatermark.py AddWatermark_py

##
# \cond INTERNAL
# ![AddWatermark_py]
import sys, os
import Utils
from Pdfix import *
            
def AddWatermark(email, key, 
    open_path,                     # PDF document to open 
    save_path,                     # output txt document 
    watermark_path):               # path to configuration file 
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + pdfix.GetError())  

    # TODO:

    doc.Close()
    pdfix.Destroy()

try:
    email = Utils.getEmail()                # email address
    licenseKey = Utils.getLicenseKey()      # license key
    cwd = os.getcwd() + "/"                 # current working directory
    os.makedirs(cwd + 'output')

    # pdfix initialization
    Pdfix_init(cwd + Utils.getModuleName('pdfix'))  # load pdfix module
    AddWatermark(email, licenseKey, 
        cwd + 'resources/test.pdf', 
        cwd + 'output/AddWatermark.pdf',
        cwd + 'resources/watermark.png')     
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![AddWatermark_py]
# \endcond
