# Initialization.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage Initialization_py 
# \page Initialization_py Initialization Sample
# Example how to initialize PDFix SDK in python.
# \snippet /Initialization.py Initialization_py
#

##
#\cond INTERNAL
#! [Initialization_py]
import sys, os
import Utils
from Pdfix import *

def Initialization(email, key):
    print('Pdfix Initialization Sample')

    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # check version
    major = pdfix.GetVersionMajor()
    minor = pdfix.GetVersionMinor()
    patch = pdfix.GetVersionPatch()
    print("PDFix SDK Version " + str(major) + "." + str(minor) + "." + str(patch))

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    # some code to execute

    # cleanup
    pdfix.Destroy()

try:
    # pdfix initialization
    email = Utils.getEmail()                # email address
    licenseKey = Utils.getLicenseKey()      # license key
    cwd = os.getcwd() + "/"                 # current working directory

    # pdfix initialization
    Pdfix_init(cwd + Utils.getModuleName('pdfix'))

    Initialization(email, licenseKey)

    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))

##    
#! [Initialization_py]
# \endcond
