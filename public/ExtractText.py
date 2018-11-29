# ExtractText.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage ExtractText_py 
# \page ExtractText_py Extract Text Sample
# Example how to extract text from PDF.
# \snippet /ExtractText.py ExtractText_py

##
# \cond INTERNAL
# ![ExtractText_py]
import sys, os
import Utils
from Pdfix import *

def GetText (element, output):
    elemType = element.GetType()
    if kPdeText == elemType:
        textElem = PdeText(element.obj)
        text = textElem.GetText()
        output.write(text)
        output.write("\n")
    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(0, count):
            child = element.GetChild(i)
            if child is not None: 
                GetText(child, output)
            
def ExtractText(email, key, 
    open_path,                     # PDF document to open 
    save_path,                     # output txt document 
    config_path):                  # path to configuration file 
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + pdfix.GetError())  

    # prepare the output file
    output = open(save_path, "w")

    numPages = doc.GetNumPages()

    for i in range(0, numPages):
        # acquire page
        page = doc.AcquirePage(i)
        if page is None:
            raise Exception('Acquire Page fail : ' + pdfix.GetError())

        # get the page map of the current page
        pageMap = page.AcquirePageMap(0, None)
        if pageMap is None:
            raise Exception('Acquire PageMap fail : ' + pdfix.GetError())

        # get page container
        container = pageMap.GetElement()
        if container is None:
            raise Exception('Get page element failure : ' + pdfix.GetError())

        GetText(container, output)
 
    output.close()
    
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

    ExtractText(email, licenseKey, 
        cwd + 'resources/test.pdf', 
        cwd + 'output/ExtractText.txt',
        cwd + 'resources/config.json')   
    
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![ExtractText_py]
# \endcond
