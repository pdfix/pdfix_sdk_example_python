# DocumentMetadata.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage DocumentMetadata_py 
# \page DocumentMetadata_py Extract Text Sample
# Example how to extract text from PDF.
# \snippet /DocumentMetadata.py DocumentMetadata_py

##
# \cond INTERNAL
# ![DocumentMetadata_py]
import sys, os
import Utils
from Pdfix import *
            
def DocumentMetadata(email, key, 
    open_path,                     # PDF document to open 
    save_path):                     # output txt document 
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + pdfix.GetError())  

    stm = pdfix.CreateFileStream(save_path, kPsTruncate)
    if stm is None:
        raise Exception('Unable to open output file : ' + pdfix.GetError()) 

    metadata = doc.GetMetadata()
    if metadata is None:
        raise Exception('Unable to read document metadata : ' + pdfix.GetError()) 
    
    if not metadata.SaveToStream(stm):
        raise Exception('Unable to save metadata : ' + pdfix.GetError()) 

    # do something with metadata

    stm.Destroy()
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

    DocumentMetadata(email, licenseKey, 
        cwd + 'resources/test.pdf', 
        cwd + '/output/DocumentMetadata.txt')   
    
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![DocumentMetadata_py]
# \endcond
