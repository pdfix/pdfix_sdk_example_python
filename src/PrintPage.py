## 
# \page Python_Samples Python Samples
# -\subpage PrintPage_py 
# \page PrintPage_py Print PDF page to printer
# Example how to print a page to default printer on Windows.
# \snippet /PrintPage.py PrintPage_py

##
# \cond INTERNAL
# ![PrintPage_py]
import os
#import win32print, win32ui # https://github.com/mhammond/pywin32
import Utils
from Pdfix import *

def PrintPage(open_path):
    # pdfix initialization
    Pdfix_init(os.getcwd() + "/" + Utils.getModuleName('pdfix'))

    pdfix  = GetPdfix()
    if pdfix is None:
        raise Exception('Pdfix Initialization fail')

    doc = pdfix.OpenDoc(open_path, "")
    if doc is None:
        raise Exception('Unable to open pdf : ' + pdfix.GetError())

    page = doc.AcquirePage(0)
    if page is None:
        raise Exception('Unable to acquire page : ' + pdfix.GetError())
    cropBox = page.GetCropBox()

    # hDC = win32ui.CreateDC ()
    # hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())

    # PHYSICALWIDTH = 110
    # PHYSICALHEIGHT = 111
    # printerSize = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

    # hDC.StartDoc ("Test doc")
    # hDC.StartPage ()

    printerSize = 8000, 10000

    zoom = min(printerSize[0] / (cropBox.right - cropBox.left), 
        printerSize[1] / (cropBox.top - cropBox.bottom))
    # render first page to jpg image
    pageView = page.AcquirePageView(zoom, kRotate0)
    if not pageView:
        raise Exception('Unable to acquire page view : ' + pdfix.GetError())

    clipRect = pageView.RectToDevice(cropBox)
    # params = PdfPageRenderParams()
    # params.device = hDC
    # params.matrix = pageView.GetDeviceMatrix()
    # params.clip_rect = clipRect
    # params.render_flags = kRenderAnnot
    # if  not page.DrawContent(params, 0, None):
    #     raise Exception('Unable to draw content : ' + pdfix.GetError())
    page.Release()

    # hDC.EndPage ()
    # hDC.EndDoc ()

    doc.Close()
    pdfix.Destroy()

    Pdfix_destroy()
    
##
# ![PrintPage_py]
# \endcond
