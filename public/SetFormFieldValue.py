# SetFormFieldValue.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage SetFormFieldValue_py 
# \page SetFormFieldValue_py Set Form Field Value Sample
# Example how to fill PDF form.
# \snippet /SetFormFieldValue.py SetFormFieldValue_py

##
# \cond INTERNAL
# ![SetFormFieldValue_py]
import sys, os
import Utils
from Pdfix import *

def SetFormFieldValue(email, key, open_path, save_path):
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open pdf : ' + pdfix.GetError())

    field = doc.GetFormFieldByName("Text1")
    if field is not None:
        value = field.GetValue()
        value = "New Value"
        field.SetValue(value)

    if not doc.Save(save_path, kSaveFull):
        raise Exception(pdfix.GetError())

    doc.Close()

    pdfix.Destroy()

try:
    # pdfix initialization
    email = Utils.getEmail()                # email address
    licenseKey = Utils.getLicenseKey()      # license key
    cwd = os.getcwd() + "/"                 # current working directory
    os.makedirs(cwd + 'output')

    # pdfix initialization
    Pdfix_init(cwd + Utils.getModuleName('pdfix'))

    SetFormFieldValue(email, licenseKey, 
        cwd + 'resources/test.pdf',
        cwd + 'output/SetFormFieldValue.pdf') 

    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![SetFormFieldValue_py]
# \endcond
