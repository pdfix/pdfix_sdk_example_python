################################################################################
# Copyright (c) 2018 PDFix (http://pdfix.net). All Rights Reserved.
# This file was generated automatically
################################################################################
from ctypes import Structure, c_int, c_bool, c_void_p, c_double, byref, POINTER, c_wchar_p, c_char_p, c_ubyte, create_unicode_buffer, cdll
from Pdfix import *

# Enumerators
# 
(kErrorHtmlPdfDocInvalid, kErrorHtmlPageOutOfRange) = (1000, 1001)
# 
(kHtmlNone, kHtmlExportJavaScripts, kHtmlExportFonts, kHtmlRetainFontSize, kHtmlRetainTextColor, kHtml41Support, kHtmlNoExternalCSS, kHtmlNoExternalJS, kHtmlNoExternalIMG, kHtmlNoExternalFONT, kHtmlGrayBackground) = (0x00, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100, 0x0200)
# PdfHtmlType
(kPdfHtmlFixed, kPdfHtmlResponsive) = (0, 1)

# Structures - Private
class zz_PdfHtmlParams(Structure):
    _fields_ = [("flags", c_int), ("width", c_int), ("type", c_int), ("image_params", zz_PdfImageParams)]

# Structures - Public
class PdfHtmlParams(Structure):
    def __init__(self):
        self.flags = 0
        self.width = 1200
        self.type = kPdfHtmlFixed
        self.image_params = PdfImageParams()
    def GetIntStruct(self):
        result = zz_PdfHtmlParams()
        result.flags = self.flags
        result.width = self.width
        result.type = self.type
        result.image_params = self.image_params.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.flags = struct.flags
        self.width = struct.width
        self.type = struct.type
        self.image_params.SetIntStruct(struct.image_params)

# Objects
class _PdfToHtmlBase(object):
    def __init__(self, _obj):
        self.obj = _obj

class PdfToHtml(PdfixPlugin):
    def __init__(self, _obj):
        super(PdfToHtml, self).__init__(_obj)

    def OpenHtmlDoc(self, _doc):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfToHtmlOpenHtmlDoc(self.obj, _doc.obj)
        if ret:
            return PdfHtmlDoc(ret)
        else:
            return None

    def SaveCSS(self, _stream):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfToHtmlSaveCSS(self.obj, _stream.obj)
        return ret

    def SaveJavaScript(self, _stream):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfToHtmlSaveJavaScript(self.obj, _stream.obj)
        return ret

class PdfHtmlDoc(_PdfToHtmlBase):
    def __init__(self, _obj):
        super(PdfHtmlDoc, self).__init__(_obj)

    def Close(self):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfHtmlDocClose(self.obj)
        return ret

    def Save(self, _path, _params, _cancel_proc, _cancel_data):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfHtmlDocSave(self.obj, _path, _params.GetIntStruct(), _cancel_proc, _cancel_data)
        return ret

    def SaveDocHtml(self, _stream, _params, _cancel_proc, _cancel_data):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfHtmlDocSaveDocHtml(self.obj, _stream.obj, _params.GetIntStruct(), _cancel_proc, _cancel_data)
        return ret

    def SavePageHtml(self, _stream, _params, _page_num, _cancel_proc, _cancel_data):
        global PdfToHtmlLib
        ret = PdfToHtmlLib.PdfHtmlDocSavePageHtml(self.obj, _stream.obj, _params.GetIntStruct(), _page_num, _cancel_proc, _cancel_data)
        return ret

def GetPdfToHtml():
    global PdfToHtmlLib
    obj = PdfToHtmlLib.GetPdfToHtml()
    return PdfToHtml(obj)

PdfToHtmlLib = None

def PdfToHtml_init(path):
    global PdfToHtmlLib
    PdfToHtmlLib = cdll.LoadLibrary(path)
    if PdfToHtmlLib is None:
        raise Exception("LoadLibrary fail")
    PdfToHtmlLib.PdfToHtmlOpenHtmlDoc.restype = c_void_p
    PdfToHtmlLib.PdfToHtmlOpenHtmlDoc.argtypes = [c_void_p, c_void_p]
    PdfToHtmlLib.PdfToHtmlSaveCSS.restype = c_int
    PdfToHtmlLib.PdfToHtmlSaveCSS.argtypes = [c_void_p, c_void_p]
    PdfToHtmlLib.PdfToHtmlSaveJavaScript.restype = c_int
    PdfToHtmlLib.PdfToHtmlSaveJavaScript.argtypes = [c_void_p, c_void_p]
    PdfToHtmlLib.PdfHtmlDocClose.restype = c_int
    PdfToHtmlLib.PdfHtmlDocClose.argtypes = [c_void_p]
    PdfToHtmlLib.PdfHtmlDocSave.restype = c_int
    PdfToHtmlLib.PdfHtmlDocSave.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfHtmlParams), c_int, c_void_p]
    PdfToHtmlLib.PdfHtmlDocSaveDocHtml.restype = c_int
    PdfToHtmlLib.PdfHtmlDocSaveDocHtml.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfHtmlParams), c_int, c_void_p]
    PdfToHtmlLib.PdfHtmlDocSavePageHtml.restype = c_int
    PdfToHtmlLib.PdfHtmlDocSavePageHtml.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfHtmlParams), c_int, c_int, c_void_p]
    PdfToHtmlLib.GetPdfToHtml.restype = c_void_p

def PdfToHtml_destroy():
    global PdfToHtmlLib
    del PdfToHtmlLib
    PdfToHtmlLib = None

