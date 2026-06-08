# ExtractImages.py
# Example how to extract images from PDF.

from pdfixsdk import *

from Utils import input_path, output_path


def SaveImage(pdfix, page, element):
    global imageIndex, output_path
    elem_type = element.GetType()
    if elem_type == kPdeImage:
        image = PdeImage(element.obj)
        bbox = image.GetBBox()

        pageView = page.AcquirePageView(2.0, kRotate0)
        if pageView is None:
            raise RuntimeError(pdfix.GetError())

        devRect = pageView.RectToDevice(bbox)

        # move dev rect to 0,0 - content will be drawn to the top-left corner
        devRect.right -= devRect.left
        devRect.left = 0
        devRect.bottom -= devRect.top
        devRect.top = 0

        # prepare image
        psImage = pdfix.CreateImage(
            pageView.GetDeviceWidth(), pageView.GetDeviceHeight(), kImageDIBFormatArgb
        )
        if psImage is None:
            raise RuntimeError(pdfix.GetError())

        renderParams = PdfPageRenderParams()
        renderParams.clip_box = bbox
        renderParams.image = psImage
        renderParams.matrix = pageView.GetDeviceMatrix()
        if not page.DrawContent(renderParams):
            raise RuntimeError(pdfix.GetError())

        # save image to file
        path = output_path.joinpath(f"ExtractImages_{imageIndex}.png")

        imageParams = PdfImageParams()
        psImage.SaveRect(path.as_posix(), imageParams, devRect)
        psImage.Destroy()
        pageView.Release()

        imageIndex += 1
    else:
        count = element.GetNumChildren()
        if count == 0:
            return
        for i in range(count):
            child = element.GetChild(i)
            if child:
                SaveImage(pdfix, page, child)


imageIndex = 1

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# iterate pages to search for images
for i in range(doc.GetNumPages()):
    # acquire page
    page = doc.AcquirePage(i)
    if page is None:
        raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

    # get the page map of the current page
    pageMap = page.AcquirePageMap()
    if pageMap is None:
        raise RuntimeError(f"Unable to acquire page map: {pdfix.GetError()}")
    if not pageMap.CreateElements():
        raise RuntimeError(f"Unable to acquire page map: {pdfix.GetError()}")

    # get page container
    container = pageMap.GetElement()
    if container is None:
        raise RuntimeError(f"Unable to get page element: {pdfix.GetError()}")

    SaveImage(pdfix, page, container)
    pageMap.Release()
    page.Release()

print(str(imageIndex - 1) + " images found")
doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
