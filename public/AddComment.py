# AddComment.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage AddComment_py 
# \page AddComment_py Add Comment Sample
# Example how to add a comment with reply into PDF.
# \snippet /AddComment.py AddComment_py

##
# \cond INTERNAL
# ![AddComment_py]
import sys, os
import Utils
from Pdfix import *

def AddComment(email, key, open_path, save_path):
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open pdf : ' + pdfix.GetError())

    page = doc.AcquirePage(0)
    if page is None:
        raise Exception('Unable to acquire page : ' + pdfix.GetError())
    
    cropBox = page.GetCropBox()

    # place annotation to the middle of the page
    annotRect = PdfRect()
    annotRect.left = (cropBox.right + cropBox.left) / 2.0 - 10
    annotRect.bottom = (cropBox.top + cropBox.bottom) / 2.0 - 10
    annotRect.right = (cropBox.right + cropBox.left) / 2.0 + 10
    annotRect.top = (cropBox.top + cropBox.bottom) / 2.0 + 10
    annot = page.AddTextAnnot(-1, annotRect)
    if annot is None:
        raise Exception(pdfix.GetError())

    annot.SetAuthor("Peter Brown")
    annot.SetContents("This is my comment.")
    annot.AddReply("Mark Fish", "This is some reply.")

    doc.ReleasePage(page)

    if not doc.Save(save_path, kSaveFull):
        raise Exception(pdfix.GetError())

    doc.Close()
    pdfix.Destroy()

try:
    email = Utils.getEmail()                # email address
    licenseKey = Utils.getLicenseKey()      # license key
    cwd = os.getcwd() + "/"                 # current working directory
    os.makedirs(cwd + 'output')

    # pdfix initialization
    Pdfix_init(cwd + Utils.getModuleName('pdfix'))
    AddComment(email, licenseKey, 
        cwd + '/resources/test.pdf', 
        cwd + '/output/AddComment.pdf')  
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![AddComment_py]
# \endcond
