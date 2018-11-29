# ConvertToHtml.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage ConvertToHtml_py 
# \page ConvertToHtml_py Add Comment Sample
# Example how to add a comment with reply into PDF.
# \snippet /ConvertToHtml.py ConvertToHtml_py

##
# \cond INTERNAL
# ![ConvertToHtml_py]
import sys, os
import Utils
from Pdfix import *
from PdfToHtml import *

def ConvertToHtml(email, key, 
    open_path,                     # PDF document to open 
    save_path,                     # output html document 
    config_path,                   # path to configuration file 
    html_params):                  # PdfHtmlParams structure 
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    pdfToHtml = GetPdfToHtml()
    if pdfToHtml is None:
        raise Exception('PdfToHtml Initialization fail')

    if not pdfToHtml.Initialize(pdfix):
        raise Exception('PdfToHtml Initialize Pdfix fail')

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + pdfix.GetError())   

    htmlDoc = pdfToHtml.OpenHtmlDoc(doc)
    if htmlDoc is None:
        raise Exception('Unable to open html doc : ' + pdfix.GetError())   

    # convert all pages at once
    if not htmlDoc.Save(save_path, html_params, 0, None):
        raise Exception('Unable to open html doc : ' + pdfix.GetError())    
    
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
    PdfToHtml_init(cwd + Utils.getModuleName('pdf_to_html'))

    htmlParams = PdfHtmlParams()
    htmlParams.type = kPdfHtmlFixed
    htmlParams.flags |= kHtmlNoExternalCSS | kHtmlNoExternalJS | kHtmlNoExternalJS
    
    ConvertToHtml(email, licenseKey, 
        cwd + 'resources/test.pdf',
        cwd + 'output/index.html',
        cwd + 'resources/config.json',
        htmlParams)   
    
    PdfToHtml_destroy()
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![ConvertToHtml_py]
# \endcond
