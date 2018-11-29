# RenderPage.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

## 
# \page Python_Samples Python Samples
# -\subpage RenderPage_py 
# \page RenderPage_py Render page sample
# Example how to render PDF page to an image.
# \snippet /RenderPage.py RenderPage_py

##
# \cond INTERNAL
# ![RenderPage_py]
import sys, os
import Utils
from Pdfix import *
            
def RenderPage(email, key, 
    open_path,                     # PDF document to open 
    image_path,                    # path to image
    zoom,                          # zoom factor
    rotate):                       # page rotation
    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    # authorization
    if not pdfix.Authorize(email, key):
        raise Exception('Authorization fail : ' + pdfix.GetError())

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open doc : ' + pdfix.GetError())  

    # prepare page for rendering
    page = doc.AcquirePage(0)
    if page is None:
        raise Exception('Unable to acquire page : ' + pdfix.GetError())  
    pageView = page.AcquirePageView(zoom, rotate)
    if pageView is None:
        raise Exception('Unable to acquire page view : ' + pdfix.GetError())  
    width = pageView.GetDeviceWidth()
    height = pageView.GetDeviceHeight()

    # create an image
    image = pdfix.CreateImage(width, height, kImageDIBFormatArgb)
    if image is None:
        raise Exception('Unable to create image : ' + pdfix.GetError())  

    # render page
    renderParams = PdfPageRenderParams()
    renderParams.image = image
    renderParams.matrix = pageView.GetDeviceMatrix()
    if not page.DrawContent(renderParams, 0, None):
        raise Exception('Unable to draw content : ' + pdfix.GetError())  

    # save image to file 
    stm = pdfix.CreateFileStream(image_path, kPsTruncate)
    if stm is None:
        raise Exception('Unable to create file stream : ' + pdfix.GetError())  

    imgParams = PdfImageParams()
    imgParams.format = kImageFormatJpg
    imgParams.quality = 75
    if not image.SaveToStream(stm, imgParams):
        raise Exception('Unable to save image to stream : ' + pdfix.GetError())  

    # cleanup
    stm.Destroy()
    image.Destroy()
    page.ReleasePageView(pageView)
    doc.ReleasePage(page)
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

    RenderPage(email, licenseKey, 
        cwd + 'resources/test.pdf',
        cwd + 'output/RenderPage.jpg',
        2.0, kRotate0)   
    
    Pdfix_destroy()

except Exception as e:
    print('Oops! ' + str(e))
    
##
# ![RenderPage_py]
# \endcond
