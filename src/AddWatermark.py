# AddWatermark.py 
# Example how to extract text from PDF.

# import utils to load required shared libraries
from Utils import *
from Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

img_stm = pdfix.CreateFileStream( inputPath + "/watermark.png" , kPsReadOnly)
if img_stm is None:
    raise Exception(pdfix.GetError())

# identify image format from file path
format = kImageFormatPng

image_obj = doc.CreateXObjectFromImage(img_stm, format)

if image_obj is None:
    raise Exception(pdfix.GetError())

page_num = doc.GetNumPages()
for i in range(page_num):
    page = doc.AcquirePage(i)
    if page is None:
        raise Exception(pdfix.GetError())

    content = page.GetContent()
    if content is None:
        raise Exception(pdfix.GetError())
            
    xobjdict = image_obj.GetStreamDict()
    width = xobjdict.GetNumber("Width")
    height = xobjdict.GetNumber("Height")

    # prepare the matrix
    page_mx = page.GetDefaultMatrix()
    crop_rect = page.GetCropBox()
    page_mx_rev = PdfMatrixInverse(page_mx)

    # scale
    scale = 1.5
    width_scaled = width * scale
    height_scaled = height * scale

    matrix = PdfMatrix()
    matrix.a = width_scaled
    matrix.b = 0
    matrix.c = 0
    matrix.d = height_scaled
    matrix.e = 0
    matrix.f = 0

    # rotation
    rotation = 45.0
    if rotation != 0.0:
        matrix = PdfMatrixTranslate(matrix, -width_scaled / 2, -height_scaled / 2, False)
        matrix = PdfMatrixRotate(matrix, (rotation / 180.0) * kPi, False)
        matrix = PdfMatrixTranslate(matrix, width_scaled / 2, height_scaled / 2, False)
    
    rect_h = crop_rect.right - crop_rect.left
    rect_v = crop_rect.top - crop_rect.bottom

    # horizontal align
    h_align = kAlignmentCenter
    if (h_align == kAlignmentCenter):
        matrix = PdfMatrixTranslate(matrix, (rect_h - width_scaled) / 2, 0.0, False)
    elif (h_align == kAlignmentRight):
        matrix = PdfMatrixTranslate(matrix, (rect_h - width_scaled), 0.0, False)

    # vertical align
    v_align = kAlignmentCenter
    if (v_align == kAlignmentCenter):
        matrix = PdfMatrixTranslate(matrix, 0.0, (rect_v - height_scaled) / 2, False)
    elif (v_align == kAlignmentTop):
        matrix = PdfMatrixTranslate(matrix, 0.0, (rect_v - height_scaled), False)

    # horizontal and vertical offset
    offs_h = 10
    offs_v = 20

    # -offs_v because y coordinate from top to bottom
    matrix = PdfMatrixTranslate(matrix, offs_h, -offs_v, False)
    order_top = 1
    if order_top == 1:
        position = -1
    else:
        position = 0
    imageobject = content.AddNewImage(position, image_obj, matrix)

    # set opacity of the image
    opacity = 0.8
    graphicState = imageobject.GetGState()
    graphicState.color_state.fill_opacity = (int)(opacity * 255)
    imageobject.SetGState(graphicState)
    page.SetContent()
    page.Release()

if (not doc.Save(outputPath + "/AddWatermark.pdf", kSaveFull)):
    raise Exception(pdfix.GetError())

doc.Close()
