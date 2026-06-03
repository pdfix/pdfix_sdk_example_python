# RenderPage.py
# Copyright (c) 2018 PDFix. All Rights Reserved.

from pdfixsdk import *

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path / "test.pdf", "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# prepare page for rendering
page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

pageView = page.AcquirePageView(1, kRotate0)
if pageView is None:
    raise RuntimeError(f"Unable to acquire page view: {pdfix.GetError()}")

width = pageView.GetDeviceWidth()
height = pageView.GetDeviceHeight()

# create an image
image = pdfix.CreateImage(width, height, kImageDIBFormatArgb)
if image is None:
    raise RuntimeError(f"Unable to create image: {pdfix.GetError()}")

# render page
renderParams = PdfPageRenderParams()
renderParams.image = image
renderParams.matrix = pageView.GetDeviceMatrix()
if not page.DrawContent(renderParams):
    raise RuntimeError(f"Unable to draw page content: {pdfix.GetError()}")

# save image to file
stm = pdfix.CreateFileStream(output_path / "RenderPage.jpg", kPsTruncate)
if stm is None:
    raise RuntimeError(f"Unable to create file stream: {pdfix.GetError()}")

imgParams = PdfImageParams()
imgParams.format = kImageFormatJpg
imgParams.quality = 75
if not image.SaveToStream(stm, imgParams):
    raise RuntimeError(f"Unable to save image to stream: {pdfix.GetError()}")

# cleanup
stm.Destroy()
image.Destroy()
pageView.Release()
page.Release()
doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
