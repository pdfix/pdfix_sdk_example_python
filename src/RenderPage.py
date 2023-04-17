# RenderPage.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# prepare page for rendering
page = doc.AcquirePage(0)
if page is None:
    raise Exception('Unable to acquire page : ' + pdfix.GetError()) 

pageView = page.AcquirePageView(1, kRotate0)
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
stm = pdfix.CreateFileStream(outputPath + "/RenderPage.jpg", kPsTruncate)
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
pageView.Release()
page.Release()
doc.Close()
