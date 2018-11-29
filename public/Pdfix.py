################################################################################
# Copyright (c) 2018 PDFix (http://pdfix.net). All Rights Reserved.
# This file was generated automatically
################################################################################
from ctypes import Structure, c_int, c_bool, c_void_p, c_double, byref, POINTER, c_wchar_p, c_char_p, c_ubyte, create_unicode_buffer, cdll

# Enumerators
# PdfAuthPlatform
(kAuthPlatformWin, kAuthPlatformMac, kAuthPlatformLinux, kAuthPlatformAndroid, kAuthPlatformiOS, kAuthPlatformServer) = (0, 1, 2, 3, 4, 5)
# PdfAuthOption
(kAuthOptionBasic, kAuthOptionProfessional, kAuthOptionEnterprise) = (0, 1, 2)
# 
(kErrorUnknown, kErrorOutOfMemory, kErrorMalformedInput, kErrorMethodNotImplemented, kErrorPdfDocInvalid, kErrorPdfDocOpen, kErrorPdfDocCreate, kErrorPdfDocSave, kErrorPdfDocXFA, kErrorPdfDocInterForm, kErrorPdfDocClose, kErrorPdfDocInfo, kErrorPdfDocStructTreeMissing, kErrorPdfDigSigDestroy, kErrorPdfDigSigOpenPfxFile, kErrorPdfDigSigSaveFile, kErrorPdfDigSigReadFile, kErrorPdfDigSigCertOpenSystemStore, kErrorPdfDigSigPFXImportCertStore, kErrorPdfDigSigCertFindInStore, kErrorPdfDigSigPFXImportOpenSSL, kErrorPdfDigSigPFXParseOpenSSL, kErrorPdfDigSigByteRange, kErrorPdfDigSigCryptMemAlloc, kErrorPdfDigSigCryptSignMessage, kErrorPdfDigSigTimeStampMessage, kErrorPdfDigSigTimeStampRequest, kErrorPdfDigSigCryptHash, kErrorPdfDigSigVerifyDetachedMessage, kErrorPdfDigSigUnknownType, kErrorPdfDigSigCallback, kErrorPdsObjectInvalid, kErrorPdfFontSubstFontMissing, kErrorPdfPageRelease, kErrorPdfPageGetImage, kErrorPdfPageInvalidObj, kErrorPdfPageInvalidColorSpace, kErrorPdfPageMapInvalidObj, kErrorPdfPageMapParse, kErrorPdfPageMapRangeOutOf, kErrorPdfPageMapAddElement, kErrorPdfPageMapCantInsertTj, kErrorPdfPageViewNotFound, kErrorPsImageOpenFile, kErrorPsImageUnsupportedFormat, kErrorPsImageWriteBMP, kErrorPsImageWritePNG, kErrorPsImageWriteJPG, kErrorPsImageInvalidBitmap, kErrorPsImageFormat, kErrorPdfAnnotMalformed, kErrorPdfAnnotInvalidType, kErrorPdeAnnotMalformed, kErrorPdeElementMalformed, kErrorPdeTextRunMalformed, kErrorPdeWordMalformed, kErrorPdeLineMalformed, kErrorPdeListMalformed, kErrorPdeTextMalformed, kErrorPdeTextRangeOutOf, kErrorPdeTextSelectRange, kErrorPdeTableMalformed, kErrorPdeTableCellRangeOutOf, kErrorPdeCellRangeOutOf, kErrorPsRegexDestroy, kErrorPsRegexPatternMissing, kErrorPsEventMalformed, kErrorPsEventExists, kErrorPsNoEvent, kErrorPdfBookmarkMalformed, kErrorPdfBookmarkRoot, kErrorPsAuthorizationFailed, kErrorPsAuthorizationNeeded, kErrorPsAuthorizationCalled, kErrorPsAuthorizationEmail, kErrorPsAuthorizationWin, kErrorPsAuthorizationMac, kErrorPsAuthorizationAndroid, kErrorPsAuthorizationiOS, kErrorPsAuthorizationLinux, kErrorPsAuthorizationServer, kErrorPsAuthorizationFeature, kErrorPsAuthorizationDate, kErrorPsAuthorizationVersion, kErrorPsAuthorizationNumber, kErrorPsAuthorizationOsCheck, kErrorPdfFontNotEmbedded, kErrorPdfFontSave, kErrorPathNotFound, kErrorPdfPageMapAddTags, kErrorPdfPageMapRemoveTags, kErrorPdfAlternateNotFound, kErrorPdfAlternateInvalid, kErrorPdfAlternateResourceNotFound, kErrorPdfHtmlAlternateFont, kErrorPdfHtmlAlternateCreateAF, kErrorPdfHtmlAlternateWriteAF, kErrorPdfHtmlAlternateImage, kErrorPsStreamReadProcMissing, kErrorPsStreamWriteProcMissing, kErrorPsStreamGetSizeProcMissing, kErrorPdfPageMapTagAttributes, kErrorPdfPageMapTagParentTree, kErrorPdeContentWriter, kErrorParsingDataFile, kErrorPsRegexSearchFail, kErrorDocTemplateInvalidQuery, kErrorDocTemplateInvalidValue, kErrorPdsStructTreeInvalid, kErrorInit, kErrorIndexOutOfRange, kErrorPdsStructElementNotFound) = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112)
# PdfEventType
(kEventUnknown, kEventDocWillSave, kEventDocWillClose, kEventDocDidOpen, kEventDocDidSave, kEventAnnotWillChange, kEventAnnotDidChange, kEventPageWillAddAnnot, kEventPageWillRemoveAnnot, kEventPageDidAddAnnot, kEventPageDidRemoveAnnot, kEventageContentsDidChange) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# PdfSaveFlags
(kSaveIncremental, kSaveFull) = (0, 1)
# PdfDigSigValidState
(kDigSigBlank, kDigSigUnknown, kDigSigInvalid, kDigSigValid, kDigSigDoubleChecked, kDigSigValidStateEnumSize) = (0, 1, 2, 3, 4, 5)
# PdfAlignment
(kAlignmentNone, kAlignmentLeft, kAlignmentRight, kAlignmentJustify, kAlignmentTop, kAlignmentBottom, kAlignmentCenter) = (0, 1, 2, 3, 4, 5, 6)
# PdfRotate
(kRotate0, kRotate90, kRotate180, kRotate270) = (0, 90, 180, 270)
# PdfObjectType
(kPdsUnknown, kPdsBoolean, kPdsNumber, kPdsString, kPdsName, kPdsArray, kPdsDictionary, kPdsStream, kPdsNull, kPdsReference) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# PdfPageObjectType
(kPdsPageUnknown, kPdsPageText, kPdsPagePath, kPdsPageImage, kPdsPageShading, kPdsPageForm) = (0, 1, 2, 3, 4, 5)
# PdfElementType
(kPdeUnknown, kPdeText, kPdeTextLine, kPdeWord, kPdeTextRun, kPdeImage, kPdeContainer, kPdeList, kPdeLine, kPdeRect, kPdeTable, kPdeCell, kPdeToc, kPdeFormField, kPdeHeader, kPdeFooter, kPdeColumn, kPdeRow) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
# PdfLineCap
(kPdfLineCapButt, kPdfLineCapRound, kPdfLineCapSquare) = (0, 1, 2)
# PdfLineJoin
(kPdfLineJoinMiter, kPdfLineJoinRound, kPdfLineJoinBevel) = (0, 1, 2)
# PdfFillType
(kFillTypeNone, kFillTypeSolid, kFillTypePattern) = (0, 1, 2)
# PdfTextAlignment
(kTextAlignmentNone, kTextAlignmentLeft, kTextAlignmentRight, kTextAlignmentCenter, kTextAlignmentJustify) = (0, 1, 2, 3, 4)
# PdfAnnotSubtype
(kAnnotUnknown, kAnnotText, kAnnotLink, kAnnotFreeText, kAnnotLine, kAnnotSquare, kAnnotCircle, kAnnotPolygon, kAnnotPolyLine, kAnnotHighlight, kAnnotUnderline, kAnnotSquiggly, kAnnotStrikeOut, kAnnotStamp, kAnnotCaret, kAnnotInk, kAnnotPopup, kAnnotFileAttachment, kAnnotSound, kAnnotMovie, kAnnotWidget, kAnnotScreen, kAnnotPrinterMark, kAnnotTrapNet, kAnnotWatermark, kAnnot3D, kAnnotRedact) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
# 
(kAnnotFlagNone, kAnnotFlagInvisible, kAnnotFlagHidden, kAnnotFlagPrint, kAnnotFlagNoZoom, kAnnotFlagNoRotate, kAnnotFlagNoView, kAnnotFlagReadOnly, kAnnotFlagLocked, kAnnotFlagToggleNoView, kAnnotFlagLockedContents) = (0x0000, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100, 0x0200)
# 
(kRemoveAnnotSingle, kRemoveAnnotPopup, kRemoveAnnotReply) = (0x0000, 0x0001, 0x0002)
# PdfBorderStyle
(kBorderSolid, kBorderDashed, kBorderBeveled, kBorderInset, kBorderUnderline) = (0, 1, 2, 3, 4)
# 
(kTextFlagNone, kTextFlagUnderline, kTextFlagStrikeout, kTextFlagHighlight, kTextFlagSubscript, kTextFlagSuperscript, kTextFlagNoUnicode, kTextFlagPatternFill, kTextFlagPatternStroke, kTextFlagAngle, kTextFlagWhiteSpace, kTextFlagUnicode) = (0x000, 0x001, 0x002, 0x004, 0x008, 0x010, 0x020, 0x040, 0x080, 0x100, 0x200, 0x400)
# 
(kFieldFlagNone, kFieldFlagReadOnly, kFieldFlagRequired, kFieldFlagNoExport, kFieldFlagMultiline, kFieldFlagPassword, kFieldFlagNoToggleToOff, kFieldFlagRadio, kFieldFlagPushButton, kFieldFlagCombo, kFieldFlagEdit, kFieldFlagSort, kFieldFlagMultiSelect, kFieldFlagDoNotSpellCheck, kFieldFlagDCommitOnSelChange, kFieldFlagFileSelect, kFieldFlagDoNotScroll, kFieldFlagComb, kFieldFlagRichText, kFieldFlagRadiosInUnison) = (0x00000000, 0x00000001, 0x00000002, 0x00000004, 0x00001000, 0x00002000, 0x00004000, 0x00008000, 0x00010000, 0x00200000, 0x00400000, 0x00800000, 0x00200000, 0x00400000, 0x04000000, 0x00100000, 0x00800000, 0x01000000, 0x02000000, 0x02000000)
# PdfFieldType
(kFieldUnknown, kFieldButton, kFieldRadio, kFieldCheck, kFieldText, kFieldCombo, kFieldList, kFieldSignature) = (0, 1, 2, 3, 4, 5, 6, 7)
# PdfActionEventType
(kActionEventAnnotEnter, kActionEventAnnotExit, kActionEventAnnotMouseDown, kActionEventAnnotMouseUp, kActionEventAnnotFocus, kActionEventAnnotBlur, kActionEventAnnotPageOpen, kActionEventAnnotPageClose, kActionEventAnnotPageVisible, kActionEventAnnotPageInvisible, kActionEventPageOpen, kActionEventPageClose, kActionEventFieldKeystroke, kActionEventFieldFormat, kActionEventFieldValidate, kActionEventFieldCalculate, kActionEventDocWillClose, kActionEventDocWillSave, kActionEventDocDidSave, kActionEventDocWillPrint, kActionEventDocDidPrint) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
# PdfActionType
(kActionUnknown, kActionGoTo, kActionGoToR, kActionGoToE, kActionLaunch, kActionThread, kActionURI, kActionSound, kActionMovie, kActionHide, kActionNamed, kActionSubmitForm, kActionResetForm, kActionImportData, kActionJavaScript, kActionSetOCGState, kActionRendition, kActionTrans, kActionGoTo3DView) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
# 
(kRenderAnnot, kRenderLCDText, kRenderNoNativeText, kRenderGrayscale, kRenderLimitedCache, kRenderForceHalftone, kRenderPrinting, kRenderNoText, kRenderNoBackground) = (0x001, 0x002, 0x004, 0x008, 0x010, 0x020, 0x040, 0x080, 0x100)
# PdfRenderMode
(kRenderElemNone, kRenderElem) = (0, 1)
# PdfImageFormat
(kImageFormatPng, kImageFormatJpg, kImageFormatBmp, kImageFormatEmf) = (0, 1, 2, 3)
# 
(kFontFixedPitch, kFontSerif, kFontSymbolic, kFontScript, kFontNotSymbolic, kFontItalic, kFontAllCap, kFontSmallCap, kFontForceBold) = (0x00001, 0x00002, 0x00004, 0x00008, 0x00020, 0x00040, 0x10000, 0x20000, 0x40000)
# PdfFontCharset
(kFontAnsiCharset, kFontDefaultCharset, kFontSymbolCharset, kFontUnknownCharset, kFontMacintoshCharset, kFontShiftJISCharset, kFontHangeulCharset, kFontKoreanCharset, kFontGB2312Charset, kFontCHineseBig5Charset, kFontGreekCharset, kFontTurkishCharset, kFontVietnameseCharset, kFontHebrewCharset, kFontArabicCharset, kFontArabicTCharset, kFontArabicUCharset, kFontHebrewUCharset, kFontBalticCharset, kFontRussianCharset, kFontThaiCharset, kFontEastEuropeCharset) = (0, 1, 2, 3, 77, 128, 129, 130, 134, 136, 161, 162, 163, 177, 178, 179, 180, 181, 186, 204, 222, 238)
# PdfPageRangeType
(kAllPages, kEvenPagesOnly, kOddPagesOnly) = (0, 1, 2)
# PdfFontType
(kFontUnknownType, kFontType1, kFontTrueType, kFontType3, kFontCIDFont) = (0, 1, 2, 3, 4)
# PdfFontFormat
(kFontFormatTtf, kFontFormatWoff) = (0, 1)
# PdfDestZoomType
(kPdfZoomXYZ, kPdfZoomFitPage, kPdfZoomFitHorz, kPdfZoomFitVert, kPdfZoomFitRect, kPdfZoomFitBbox, kPdfZoomFitBHorz, kPdfZoomFitBVert) = (1, 2, 3, 4, 5, 6, 7, 8)
# PdfDigSigType
(kDigSigOpenSSL, kDigSigCert, kDigSigCustom) = (0, 1, 2)
# PdfImageType
(kImageFigure, kImageImage, kImagePath, kImageRect, kImageShading, kImageTable) = (0, 1, 2, 3, 4, 5)
# PdfTableType
(kTableGraphic, kTableIsolated, kTableIsolatedCol, kTableIsolatedRow, kTableForm, kTableElement) = (0, 1, 2, 3, 4, 5)
# PdfListType
(kListUnordered, kListOrdered) = (0, 1)
# 
(kWordHyphen, kWordBullet, kWordFilling, kWordNumber, kWordImage) = (0x0001, 0x0002, 0x0008, 0x0010, 0x10000)
# 
(kTextLineNewLine, kTextLineBullet, kTextLineHyphen, kTextLineIndent, kTextLineDropCap) = (0x0001, 0x0002, 0x0004, 0x0008, 0x0010)
# PdfTextStyle
(kTextNormal, kTextH1, kTextH2, kTextH3, kTextH4, kTextH5, kTextH6, kTextH7, kTextH8, kTextNote) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# PdfRegexType
(kRegexHyphen, kRegexBullet, kRegexBulletFont, kRegexBulletLine, kRegexFilling, kRegexToc, kRegexNumber, kRegexAllCaps, kRegexFirstCap, kRegexCurrency, kRegexPercent, kRegexTerminal, kRegexTableCaption, kRegexImageCaption, kRegexChartCaption, kRegexNoteCaption, kRegexNumberedList, kRegexNumberedSplit, kRegexSentences, kRegexAlphaNum, kRegexColon, kRegexPhoneNumber, kRegexDate, kRegexPageNumber, kRegexLast) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
# PsFileMode
(kPsWrite, kPsReadOnly, kPsTruncate) = (0, 1, 2)
# PdfAlternateType
(kAlternatePdf, kAlternateHtml) = (0, 1)
# PdfMediaType
(kCSSMediaTypeAll, kCSSMediaTypePrint, kCSSMediaTypeScreen, kCSSMediaTypeSpeech) = (0, 1, 2, 3)
# PsImageDIBFormat
(kImageDIBFormatArgb) = (0x220)
# PsDataFormat
(kDataFormatJson, kDataFormatXml) = (0, 1)
# PdfStreamType
(kFileStream, kMemoryStream, kProcStream) = (0, 1, 2)
# PdfStructElementType
(kPdsStructKidInvalid, kPdsStructKidElement, kPdsStructKidPageContent, kPdsStructKidStreamContent, kPdsStructKidObject) = (0, 1, 2, 3, 4)

# Structures - Private
class zz_PdfEventParams(Structure):
    _fields_ = [("type", c_int), ("doc", c_void_p), ("page", c_void_p), ("annot", c_void_p)]

class zz_PdfPageRangeParams(Structure):
    _fields_ = [("start_page", c_int), ("end_page", c_int), ("page_range_spec", c_int)]

class zz_PdfWatermarkParams(Structure):
    _fields_ = [("page_range", zz_PdfPageRangeParams), ("order_top", c_int), ("h_align", c_int), ("v_align", c_int), ("percentage_vals", c_int), ("h_value", c_double), ("v_value", c_double), ("scale", c_double), ("rotation", c_double), ("opacity", c_double)]

class zz_PdfPoint(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

class zz_PdfDevPoint(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

class zz_PdfRect(Structure):
    _fields_ = [("left", c_double), ("top", c_double), ("right", c_double), ("bottom", c_double)]

class zz_PdfDevRect(Structure):
    _fields_ = [("left", c_int), ("top", c_int), ("right", c_int), ("bottom", c_int)]

class zz_PdfQuad(Structure):
    _fields_ = [("tl", zz_PdfPoint), ("tr", zz_PdfPoint), ("bl", zz_PdfPoint), ("br", zz_PdfPoint)]

class zz_PdfDevQuad(Structure):
    _fields_ = [("tl", zz_PdfDevPoint), ("tr", zz_PdfDevPoint), ("bl", zz_PdfDevPoint), ("br", zz_PdfDevPoint)]

class zz_PdfMatrix(Structure):
    _fields_ = [("a", c_double), ("b", c_double), ("c", c_double), ("d", c_double), ("e", c_double), ("f", c_double)]

class zz_PdfRGB(Structure):
    _fields_ = [("r", c_int), ("g", c_int), ("b", c_int)]

class zz_PdfColorState(Structure):
    _fields_ = [("fill_type", c_int), ("stroke_type", c_int), ("fill_color", zz_PdfRGB), ("stroke_color", zz_PdfRGB), ("fill_opacity", c_int), ("stroke_opacity", c_int)]

class zz_PdfTextState(Structure):
    _fields_ = [("color_state", zz_PdfColorState), ("font", c_void_p), ("font_size", c_double), ("char_spacing", c_double), ("word_spacing", c_double), ("flags", c_int)]

class zz_PdfGraphicState(Structure):
    _fields_ = [("color_state", zz_PdfColorState), ("line_width", c_double), ("miter_limit", c_double), ("line_cap", c_int), ("line_join", c_int)]

class zz_PdfFontState(Structure):
    _fields_ = [("type", c_int), ("flags", c_int), ("bbox", zz_PdfRect), ("ascent", c_int), ("descent", c_int), ("italic", c_int), ("bold", c_int), ("fixed_width", c_int), ("vertical", c_int), ("embedded", c_int), ("height", c_int)]

class zz_PdfPageRenderParams(Structure):
    _fields_ = [("device", c_void_p), ("image", c_void_p), ("matrix", zz_PdfMatrix), ("clip_rect", zz_PdfDevRect), ("render_flags", c_int)]

class zz_PdfAnnotAppearance(Structure):
    _fields_ = [("fill_color", zz_PdfRGB), ("fill_type", c_int), ("border_color", zz_PdfRGB), ("border_width", c_double), ("border", c_int), ("opacity", c_double), ("font_size", c_double), ("text_align", c_int)]

class zz_PdfBookmarkAppearance(Structure):
    _fields_ = [("color", zz_PdfRGB), ("italic", c_int), ("bold", c_int)]

class zz_PdfWhitespaceParams(Structure):
    _fields_ = [("width", c_double), ("height", c_double)]

class zz_PdfFlattenAnnotsParams(Structure):
    _fields_ = [("page_range", zz_PdfPageRangeParams), ("flags", c_int)]

class zz_PdfMediaQueryParams(Structure):
    _fields_ = [("type", c_int), ("min_width", c_int)]

class zz_PdfImageParams(Structure):
    _fields_ = [("format", c_int), ("quality", c_int)]

class zz_PdfAccessibleParams(Structure):
    _fields_ = [("accept_tags", c_int), ("embed_fonts", c_int), ("subset_fonts", c_int)]

# Structures - Public
class PdfEventParams(Structure):
    def __init__(self):
        self.type = kEventUnknown
        self.doc = None
        self.page = None
        self.annot = None
    def GetIntStruct(self):
        result = zz_PdfEventParams()
        result.type = self.type
        result.doc = self.doc.obj
        result.page = self.page.obj
        result.annot = self.annot.obj
        return result
    def SetIntStruct(self, struct):
        self.type = struct.type
        self.doc = PdfDoc(struct.doc)
        self.page = PdfPage(struct.page)
        self.annot = PdfAnnot(struct.annot)

class PdfPageRangeParams(Structure):
    def __init__(self):
        self.start_page = 0
        self.end_page = -1
        self.page_range_spec = kAllPages
    def GetIntStruct(self):
        result = zz_PdfPageRangeParams()
        result.start_page = self.start_page
        result.end_page = self.end_page
        result.page_range_spec = self.page_range_spec
        return result
    def SetIntStruct(self, struct):
        self.start_page = struct.start_page
        self.end_page = struct.end_page
        self.page_range_spec = struct.page_range_spec

class PdfWatermarkParams(Structure):
    def __init__(self):
        self.page_range = PdfPageRangeParams()
        self.order_top = 1
        self.h_align = kAlignmentLeft
        self.v_align = kAlignmentTop
        self.percentage_vals = 0
        self.h_value = 0
        self.v_value = 0
        self.scale = 1
        self.rotation = 0
        self.opacity = 1
    def GetIntStruct(self):
        result = zz_PdfWatermarkParams()
        result.page_range = self.page_range.GetIntStruct()
        result.order_top = self.order_top
        result.h_align = self.h_align
        result.v_align = self.v_align
        result.percentage_vals = self.percentage_vals
        result.h_value = self.h_value
        result.v_value = self.v_value
        result.scale = self.scale
        result.rotation = self.rotation
        result.opacity = self.opacity
        return result
    def SetIntStruct(self, struct):
        self.page_range.SetIntStruct(struct.page_range)
        self.order_top = struct.order_top
        self.h_align = struct.h_align
        self.v_align = struct.v_align
        self.percentage_vals = struct.percentage_vals
        self.h_value = struct.h_value
        self.v_value = struct.v_value
        self.scale = struct.scale
        self.rotation = struct.rotation
        self.opacity = struct.opacity

class PdfPoint(Structure):
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetIntStruct(self):
        result = zz_PdfPoint()
        result.x = self.x
        result.y = self.y
        return result
    def SetIntStruct(self, struct):
        self.x = struct.x
        self.y = struct.y

class PdfDevPoint(Structure):
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetIntStruct(self):
        result = zz_PdfDevPoint()
        result.x = self.x
        result.y = self.y
        return result
    def SetIntStruct(self, struct):
        self.x = struct.x
        self.y = struct.y

class PdfRect(Structure):
    def __init__(self):
        self.left = 0.
        self.top = 0.
        self.right = 0.
        self.bottom = 0.
    def GetIntStruct(self):
        result = zz_PdfRect()
        result.left = self.left
        result.top = self.top
        result.right = self.right
        result.bottom = self.bottom
        return result
    def SetIntStruct(self, struct):
        self.left = struct.left
        self.top = struct.top
        self.right = struct.right
        self.bottom = struct.bottom

class PdfDevRect(Structure):
    def __init__(self):
        self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0
    def GetIntStruct(self):
        result = zz_PdfDevRect()
        result.left = self.left
        result.top = self.top
        result.right = self.right
        result.bottom = self.bottom
        return result
    def SetIntStruct(self, struct):
        self.left = struct.left
        self.top = struct.top
        self.right = struct.right
        self.bottom = struct.bottom

class PdfQuad(Structure):
    def __init__(self):
        self.tl = PdfPoint()
        self.tr = PdfPoint()
        self.bl = PdfPoint()
        self.br = PdfPoint()
    def GetIntStruct(self):
        result = zz_PdfQuad()
        result.tl = self.tl.GetIntStruct()
        result.tr = self.tr.GetIntStruct()
        result.bl = self.bl.GetIntStruct()
        result.br = self.br.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.tl.SetIntStruct(struct.tl)
        self.tr.SetIntStruct(struct.tr)
        self.bl.SetIntStruct(struct.bl)
        self.br.SetIntStruct(struct.br)

class PdfDevQuad(Structure):
    def __init__(self):
        self.tl = PdfDevPoint()
        self.tr = PdfDevPoint()
        self.bl = PdfDevPoint()
        self.br = PdfDevPoint()
    def GetIntStruct(self):
        result = zz_PdfDevQuad()
        result.tl = self.tl.GetIntStruct()
        result.tr = self.tr.GetIntStruct()
        result.bl = self.bl.GetIntStruct()
        result.br = self.br.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.tl.SetIntStruct(struct.tl)
        self.tr.SetIntStruct(struct.tr)
        self.bl.SetIntStruct(struct.bl)
        self.br.SetIntStruct(struct.br)

class PdfMatrix(Structure):
    def __init__(self):
        self.a = 1
        self.b = 0
        self.c = 0
        self.d = 1
        self.e = 0
        self.f = 0
    def GetIntStruct(self):
        result = zz_PdfMatrix()
        result.a = self.a
        result.b = self.b
        result.c = self.c
        result.d = self.d
        result.e = self.e
        result.f = self.f
        return result
    def SetIntStruct(self, struct):
        self.a = struct.a
        self.b = struct.b
        self.c = struct.c
        self.d = struct.d
        self.e = struct.e
        self.f = struct.f

class PdfRGB(Structure):
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
    def GetIntStruct(self):
        result = zz_PdfRGB()
        result.r = self.r
        result.g = self.g
        result.b = self.b
        return result
    def SetIntStruct(self, struct):
        self.r = struct.r
        self.g = struct.g
        self.b = struct.b

class PdfColorState(Structure):
    def __init__(self):
        self.fill_type = kFillTypeNone
        self.stroke_type = kFillTypeNone
        self.fill_color = PdfRGB()
        self.stroke_color = PdfRGB()
        self.fill_opacity = 255
        self.stroke_opacity = 255
    def GetIntStruct(self):
        result = zz_PdfColorState()
        result.fill_type = self.fill_type
        result.stroke_type = self.stroke_type
        result.fill_color = self.fill_color.GetIntStruct()
        result.stroke_color = self.stroke_color.GetIntStruct()
        result.fill_opacity = self.fill_opacity
        result.stroke_opacity = self.stroke_opacity
        return result
    def SetIntStruct(self, struct):
        self.fill_type = struct.fill_type
        self.stroke_type = struct.stroke_type
        self.fill_color.SetIntStruct(struct.fill_color)
        self.stroke_color.SetIntStruct(struct.stroke_color)
        self.fill_opacity = struct.fill_opacity
        self.stroke_opacity = struct.stroke_opacity

class PdfTextState(Structure):
    def __init__(self):
        self.color_state = PdfColorState()
        self.font = None
        self.font_size = 0
        self.char_spacing = 0
        self.word_spacing = 0
        self.flags = 0
    def GetIntStruct(self):
        result = zz_PdfTextState()
        result.color_state = self.color_state.GetIntStruct()
        result.font = self.font.obj
        result.font_size = self.font_size
        result.char_spacing = self.char_spacing
        result.word_spacing = self.word_spacing
        result.flags = self.flags
        return result
    def SetIntStruct(self, struct):
        self.color_state.SetIntStruct(struct.color_state)
        self.font = PdfFont(struct.font)
        self.font_size = struct.font_size
        self.char_spacing = struct.char_spacing
        self.word_spacing = struct.word_spacing
        self.flags = struct.flags

class PdfGraphicState(Structure):
    def __init__(self):
        self.color_state = PdfColorState()
        self.line_width = 1
        self.miter_limit = 0
        self.line_cap = kPdfLineCapButt
        self.line_join = kPdfLineJoinMiter
    def GetIntStruct(self):
        result = zz_PdfGraphicState()
        result.color_state = self.color_state.GetIntStruct()
        result.line_width = self.line_width
        result.miter_limit = self.miter_limit
        result.line_cap = self.line_cap
        result.line_join = self.line_join
        return result
    def SetIntStruct(self, struct):
        self.color_state.SetIntStruct(struct.color_state)
        self.line_width = struct.line_width
        self.miter_limit = struct.miter_limit
        self.line_cap = struct.line_cap
        self.line_join = struct.line_join

class PdfFontState(Structure):
    def __init__(self):
        self.type = kFontUnknownType
        self.flags = 0
        self.bbox = PdfRect()
        self.ascent = 0
        self.descent = 0
        self.italic = 0
        self.bold = 0
        self.fixed_width = 0
        self.vertical = 0
        self.embedded = 0
        self.height = 0
    def GetIntStruct(self):
        result = zz_PdfFontState()
        result.type = self.type
        result.flags = self.flags
        result.bbox = self.bbox.GetIntStruct()
        result.ascent = self.ascent
        result.descent = self.descent
        result.italic = self.italic
        result.bold = self.bold
        result.fixed_width = self.fixed_width
        result.vertical = self.vertical
        result.embedded = self.embedded
        result.height = self.height
        return result
    def SetIntStruct(self, struct):
        self.type = struct.type
        self.flags = struct.flags
        self.bbox.SetIntStruct(struct.bbox)
        self.ascent = struct.ascent
        self.descent = struct.descent
        self.italic = struct.italic
        self.bold = struct.bold
        self.fixed_width = struct.fixed_width
        self.vertical = struct.vertical
        self.embedded = struct.embedded
        self.height = struct.height

class PdfPageRenderParams(Structure):
    def __init__(self):
        self.device = 0
        self.image = None
        self.matrix = PdfMatrix()
        self.clip_rect = PdfDevRect()
        self.render_flags = kRenderAnnot
    def GetIntStruct(self):
        result = zz_PdfPageRenderParams()
        result.device = self.device
        result.image = self.image.obj
        result.matrix = self.matrix.GetIntStruct()
        result.clip_rect = self.clip_rect.GetIntStruct()
        result.render_flags = self.render_flags
        return result
    def SetIntStruct(self, struct):
        self.device = struct.device
        self.image = PsImage(struct.image)
        self.matrix.SetIntStruct(struct.matrix)
        self.clip_rect.SetIntStruct(struct.clip_rect)
        self.render_flags = struct.render_flags

class PdfAnnotAppearance(Structure):
    def __init__(self):
        self.fill_color = PdfRGB()
        self.fill_type = kFillTypeNone
        self.border_color = PdfRGB()
        self.border_width = 1
        self.border = kBorderSolid
        self.opacity = 1
        self.font_size = 0
        self.text_align = kTextAlignmentLeft
    def GetIntStruct(self):
        result = zz_PdfAnnotAppearance()
        result.fill_color = self.fill_color.GetIntStruct()
        result.fill_type = self.fill_type
        result.border_color = self.border_color.GetIntStruct()
        result.border_width = self.border_width
        result.border = self.border
        result.opacity = self.opacity
        result.font_size = self.font_size
        result.text_align = self.text_align
        return result
    def SetIntStruct(self, struct):
        self.fill_color.SetIntStruct(struct.fill_color)
        self.fill_type = struct.fill_type
        self.border_color.SetIntStruct(struct.border_color)
        self.border_width = struct.border_width
        self.border = struct.border
        self.opacity = struct.opacity
        self.font_size = struct.font_size
        self.text_align = struct.text_align

class PdfBookmarkAppearance(Structure):
    def __init__(self):
        self.color = PdfRGB()
        self.italic = 0
        self.bold = 0
    def GetIntStruct(self):
        result = zz_PdfBookmarkAppearance()
        result.color = self.color.GetIntStruct()
        result.italic = self.italic
        result.bold = self.bold
        return result
    def SetIntStruct(self, struct):
        self.color.SetIntStruct(struct.color)
        self.italic = struct.italic
        self.bold = struct.bold

class PdfWhitespaceParams(Structure):
    def __init__(self):
        self.width = 0
        self.height = 0
    def GetIntStruct(self):
        result = zz_PdfWhitespaceParams()
        result.width = self.width
        result.height = self.height
        return result
    def SetIntStruct(self, struct):
        self.width = struct.width
        self.height = struct.height

class PdfFlattenAnnotsParams(Structure):
    def __init__(self):
        self.page_range = PdfPageRangeParams()
        self.flags = kAnnotUnknown
    def GetIntStruct(self):
        result = zz_PdfFlattenAnnotsParams()
        result.page_range = self.page_range.GetIntStruct()
        result.flags = self.flags
        return result
    def SetIntStruct(self, struct):
        self.page_range.SetIntStruct(struct.page_range)
        self.flags = struct.flags

class PdfMediaQueryParams(Structure):
    def __init__(self):
        self.type = kCSSMediaTypeAll
        self.min_width = 1200
    def GetIntStruct(self):
        result = zz_PdfMediaQueryParams()
        result.type = self.type
        result.min_width = self.min_width
        return result
    def SetIntStruct(self, struct):
        self.type = struct.type
        self.min_width = struct.min_width

class PdfImageParams(Structure):
    def __init__(self):
        self.format = kImageFormatPng
        self.quality = 100
    def GetIntStruct(self):
        result = zz_PdfImageParams()
        result.format = self.format
        result.quality = self.quality
        return result
    def SetIntStruct(self, struct):
        self.format = struct.format
        self.quality = struct.quality

class PdfAccessibleParams(Structure):
    def __init__(self):
        self.accept_tags = 0
        self.embed_fonts = 0
        self.subset_fonts = 0
    def GetIntStruct(self):
        result = zz_PdfAccessibleParams()
        result.accept_tags = self.accept_tags
        result.embed_fonts = self.embed_fonts
        result.subset_fonts = self.subset_fonts
        return result
    def SetIntStruct(self, struct):
        self.accept_tags = struct.accept_tags
        self.embed_fonts = struct.embed_fonts
        self.subset_fonts = struct.subset_fonts

# Objects
class _PdfixBase(object):
    def __init__(self, _obj):
        self.obj = _obj

class PdsObject(_PdfixBase):
    def __init__(self, _obj):
        super(PdsObject, self).__init__(_obj)

    def GetObjectType(self):
        global PdfixLib
        ret = PdfixLib.PdsObjectGetObjectType(self.obj)
        return ret

class PdsBoolean(PdsObject):
    def __init__(self, _obj):
        super(PdsBoolean, self).__init__(_obj)

    def GetValue(self):
        global PdfixLib
        ret = PdfixLib.PdsBooleanGetValue(self.obj)
        return ret

class PdsNumber(PdsObject):
    def __init__(self, _obj):
        super(PdsNumber, self).__init__(_obj)

    def IsIntegerValue(self):
        global PdfixLib
        ret = PdfixLib.PdsNumberIsIntegerValue(self.obj)
        return ret

    def GetIntegerValue(self):
        global PdfixLib
        ret = PdfixLib.PdsNumberGetIntegerValue(self.obj)
        return ret

    def GetValue(self):
        global PdfixLib
        ret = PdfixLib.PdsNumberGetValue(self.obj)
        return ret

class PdsString(PdsObject):
    def __init__(self, _obj):
        super(PdsString, self).__init__(_obj)

    def GetValue(self, _buffer, _len):
        global PdfixLib
        ret = PdfixLib.PdsStringGetValue(self.obj, _buffer, _len)
        return ret

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PdsStringGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStringGetText(self.obj, _buffer, _len)
        return _buffer.value

class PdsName(PdsObject):
    def __init__(self, _obj):
        super(PdsName, self).__init__(_obj)

    def GetValue(self):
        global PdfixLib
        _len = PdfixLib.PdsNameGetValue(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsNameGetValue(self.obj, _buffer, _len)
        return _buffer.value

class PdsArray(PdsObject):
    def __init__(self, _obj):
        super(PdsArray, self).__init__(_obj)

    def GetNumObjects(self):
        global PdfixLib
        ret = PdfixLib.PdsArrayGetNumObjects(self.obj)
        return ret

    def Get(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsArrayGet(self.obj, _index)
        if ret:
            return PdsObject(ret)
        else:
            return None

class PdsDictionary(PdsObject):
    def __init__(self, _obj):
        super(PdsDictionary, self).__init__(_obj)

    def Known(self, _key):
        global PdfixLib
        ret = PdfixLib.PdsDictionaryKnown(self.obj, _key)
        return ret

    def GetNumKeys(self):
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetNumKeys(self.obj)
        return ret

    def GetKey(self, _index):
        global PdfixLib
        _len = PdfixLib.PdsDictionaryGetKey(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsDictionaryGetKey(self.obj, _index, _buffer, _len)
        return _buffer.value

    def Get(self, _key):
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGet(self.obj, _key)
        if ret:
            return PdsObject(ret)
        else:
            return None

class PdsStream(PdsObject):
    def __init__(self, _obj):
        super(PdsStream, self).__init__(_obj)

    def GetStreamDict(self):
        global PdfixLib
        ret = PdfixLib.PdsStreamGetStreamDict(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetRawDataSize(self):
        global PdfixLib
        ret = PdfixLib.PdsStreamGetRawDataSize(self.obj)
        return ret

class PdsNull(PdsObject):
    def __init__(self, _obj):
        super(PdsNull, self).__init__(_obj)

class PdsReference(PdsObject):
    def __init__(self, _obj):
        super(PdsReference, self).__init__(_obj)

    def GetObjectNumber(self):
        global PdfixLib
        ret = PdfixLib.PdsReferenceGetObjectNumber(self.obj)
        return ret

class PdsPageObject(_PdfixBase):
    def __init__(self, _obj):
        super(PdsPageObject, self).__init__(_obj)

    def GetObjectType(self):
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetObjectType(self.obj)
        return ret

    def GetBBox(self):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdsPageObjectGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

class PdsText(PdsPageObject):
    def __init__(self, _obj):
        super(PdsText, self).__init__(_obj)

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PdsTextGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsTextGetText(self.obj, _buffer, _len)
        return _buffer.value

class PdsForm(PdsPageObject):
    def __init__(self, _obj):
        super(PdsForm, self).__init__(_obj)

class PdsPath(PdsPageObject):
    def __init__(self, _obj):
        super(PdsPath, self).__init__(_obj)

class PdsImage(PdsPageObject):
    def __init__(self, _obj):
        super(PdsImage, self).__init__(_obj)

class PdsShading(PdsPageObject):
    def __init__(self, _obj):
        super(PdsShading, self).__init__(_obj)

class PdeElement(_PdfixBase):
    def __init__(self, _obj):
        super(PdeElement, self).__init__(_obj)

    def GetType(self):
        global PdfixLib
        ret = PdfixLib.PdeElementGetType(self.obj)
        return ret

    def GetBBox(self):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdeElementGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetId(self):
        global PdfixLib
        ret = PdfixLib.PdeElementGetId(self.obj)
        return ret

    def GetGraphicState(self):
        global PdfixLib
        result = PdfGraphicState()
        _g_state = result.GetIntStruct()
        PdfixLib.PdeElementGetGraphicState(self.obj, _g_state)
        result.SetIntStruct(_g_state)
        return result

    def GetNumChildren(self):
        global PdfixLib
        ret = PdfixLib.PdeElementGetNumChildren(self.obj)
        return ret

    def GetChild(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeElementGetChild(self.obj, _index)
        if ret:
            return PdeElement(ret)
        else:
            return None

    def GetAlignment(self):
        global PdfixLib
        ret = PdfixLib.PdeElementGetAlignment(self.obj)
        return ret

    def GetAngle(self):
        global PdfixLib
        ret = PdfixLib.PdeElementGetAngle(self.obj)
        return ret

    def SetRenderMode(self, _mode):
        global PdfixLib
        ret = PdfixLib.PdeElementSetRenderMode(self.obj, _mode)
        return ret

class PdeContainer(PdeElement):
    def __init__(self, _obj):
        super(PdeContainer, self).__init__(_obj)

class PdeList(PdeElement):
    def __init__(self, _obj):
        super(PdeList, self).__init__(_obj)

class PdeToc(PdeElement):
    def __init__(self, _obj):
        super(PdeToc, self).__init__(_obj)

class PdeAnnot(PdeElement):
    def __init__(self, _obj):
        super(PdeAnnot, self).__init__(_obj)

    def GetAnnot(self):
        global PdfixLib
        ret = PdfixLib.PdeAnnotGetAnnot(self.obj)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

class PdeFormField(PdeAnnot):
    def __init__(self, _obj):
        super(PdeFormField, self).__init__(_obj)

class PdeImage(PdeContainer):
    def __init__(self, _obj):
        super(PdeImage, self).__init__(_obj)

    def GetImageType(self):
        global PdfixLib
        ret = PdfixLib.PdeImageGetImageType(self.obj)
        return ret

    def GetCaption(self):
        global PdfixLib
        ret = PdfixLib.PdeImageGetCaption(self.obj)
        if ret:
            return PdeElement(ret)
        else:
            return None

class PdeLine(PdeElement):
    def __init__(self, _obj):
        super(PdeLine, self).__init__(_obj)

class PdeRect(PdeContainer):
    def __init__(self, _obj):
        super(PdeRect, self).__init__(_obj)

class PdeHeader(PdeContainer):
    def __init__(self, _obj):
        super(PdeHeader, self).__init__(_obj)

class PdeFooter(PdeContainer):
    def __init__(self, _obj):
        super(PdeFooter, self).__init__(_obj)

class PdeCell(PdeContainer):
    def __init__(self, _obj):
        super(PdeCell, self).__init__(_obj)

    def GetRowSpan(self):
        global PdfixLib
        ret = PdfixLib.PdeCellGetRowSpan(self.obj)
        return ret

    def GetColSpan(self):
        global PdfixLib
        ret = PdfixLib.PdeCellGetColSpan(self.obj)
        return ret

    def HasBorderGraphicState(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeCellHasBorderGraphicState(self.obj, _index)
        return ret

    def GetSpanCell(self):
        global PdfixLib
        ret = PdfixLib.PdeCellGetSpanCell(self.obj)
        if ret:
            return PdeCell(ret)
        else:
            return None

class PdeTable(PdeContainer):
    def __init__(self, _obj):
        super(PdeTable, self).__init__(_obj)

    def GetNumRows(self):
        global PdfixLib
        ret = PdfixLib.PdeTableGetNumRows(self.obj)
        return ret

    def GetNumCols(self):
        global PdfixLib
        ret = PdfixLib.PdeTableGetNumCols(self.obj)
        return ret

    def GetCell(self, _row, _col):
        global PdfixLib
        ret = PdfixLib.PdeTableGetCell(self.obj, _row, _col)
        if ret:
            return PdeCell(ret)
        else:
            return None

    def GetRowAlignment(self, _row):
        global PdfixLib
        ret = PdfixLib.PdeTableGetRowAlignment(self.obj, _row)
        return ret

    def GetColAlignment(self, _col):
        global PdfixLib
        ret = PdfixLib.PdeTableGetColAlignment(self.obj, _col)
        return ret

    def GetCaption(self):
        global PdfixLib
        ret = PdfixLib.PdeTableGetCaption(self.obj)
        if ret:
            return PdeElement(ret)
        else:
            return None

    def GetTableType(self):
        global PdfixLib
        ret = PdfixLib.PdeTableGetTableType(self.obj)
        return ret

class PdeWord(PdeElement):
    def __init__(self, _obj):
        super(PdeWord, self).__init__(_obj)

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PdeWordGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeWordGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self):
        global PdfixLib
        ret = PdfixLib.PdeWordHasTextState(self.obj)
        return ret

    def GetTextState(self):
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeWordGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumChars(self):
        global PdfixLib
        ret = PdfixLib.PdeWordGetNumChars(self.obj)
        return ret

    def GetCharCode(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeWordGetCharCode(self.obj, _index)
        return ret

    def GetCharText(self, _index):
        global PdfixLib
        _len = PdfixLib.PdeWordGetCharText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeWordGetCharText(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetCharTextState(self, _index):
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeWordGetCharTextState(self.obj, _index, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetCharBBox(self, _index):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdeWordGetCharBBox(self.obj, _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetFlags(self):
        global PdfixLib
        ret = PdfixLib.PdeWordGetFlags(self.obj)
        return ret

    def GetBackground(self):
        global PdfixLib
        ret = PdfixLib.PdeWordGetBackground(self.obj)
        if ret:
            return PdeElement(ret)
        else:
            return None

    def GetOrigin(self):
        global PdfixLib
        result = PdfPoint()
        _point = result.GetIntStruct()
        PdfixLib.PdeWordGetOrigin(self.obj, _point)
        result.SetIntStruct(_point)
        return result

class PdeTextLine(PdeElement):
    def __init__(self, _obj):
        super(PdeTextLine, self).__init__(_obj)

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PdeTextLineGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeTextLineGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self):
        global PdfixLib
        ret = PdfixLib.PdeTextLineHasTextState(self.obj)
        return ret

    def GetTextState(self):
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeTextLineGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumWords(self):
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetNumWords(self.obj)
        return ret

    def GetWord(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetWord(self.obj, _index)
        if ret:
            return PdeWord(ret)
        else:
            return None

    def GetFlags(self):
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetFlags(self.obj)
        return ret

class PdeText(PdeElement):
    def __init__(self, _obj):
        super(PdeText, self).__init__(_obj)

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PdeTextGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeTextGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self):
        global PdfixLib
        ret = PdfixLib.PdeTextHasTextState(self.obj)
        return ret

    def GetTextState(self):
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeTextGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumTextLines(self):
        global PdfixLib
        ret = PdfixLib.PdeTextGetNumTextLines(self.obj)
        return ret

    def GetTextLine(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeTextGetTextLine(self.obj, _index)
        if ret:
            return PdeTextLine(ret)
        else:
            return None

    def GetNumWords(self):
        global PdfixLib
        ret = PdfixLib.PdeTextGetNumWords(self.obj)
        return ret

    def GetWord(self, _index):
        global PdfixLib
        ret = PdfixLib.PdeTextGetWord(self.obj, _index)
        if ret:
            return PdeWord(ret)
        else:
            return None

    def GetLineSpacing(self):
        global PdfixLib
        ret = PdfixLib.PdeTextGetLineSpacing(self.obj)
        return ret

    def GetIndent(self):
        global PdfixLib
        ret = PdfixLib.PdeTextGetIndent(self.obj)
        return ret

    def GetTextStyle(self):
        global PdfixLib
        ret = PdfixLib.PdeTextGetTextStyle(self.obj)
        return ret

class PdfAction(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAction, self).__init__(_obj)

    def GetSubtype(self):
        global PdfixLib
        ret = PdfixLib.PdfActionGetSubtype(self.obj)
        return ret

    def GetJavaScript(self):
        global PdfixLib
        _len = PdfixLib.PdfActionGetJavaScript(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfActionGetJavaScript(self.obj, _buffer, _len)
        return _buffer.value

    def GetURI(self):
        global PdfixLib
        _len = PdfixLib.PdfActionGetURI(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfActionGetURI(self.obj, _buffer, _len)
        return _buffer.value

class PdfAnnot(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAnnot, self).__init__(_obj)

    def GetSubtype(self):
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetSubtype(self.obj)
        return ret

    def GetFlags(self):
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetFlags(self.obj)
        return ret

    def GetAppearance(self):
        global PdfixLib
        result = PdfAnnotAppearance()
        _appearance = result.GetIntStruct()
        PdfixLib.PdfAnnotGetAppearance(self.obj, _appearance)
        result.SetIntStruct(_appearance)
        return result

    def GetBBox(self):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfAnnotGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def PointInAnnot(self, _point):
        global PdfixLib
        ret = PdfixLib.PdfAnnotPointInAnnot(self.obj, _point.GetIntStruct())
        return ret

    def RectInAnnot(self, _rect):
        global PdfixLib
        ret = PdfixLib.PdfAnnotRectInAnnot(self.obj, _rect.GetIntStruct())
        return ret

class PdfLinkAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfLinkAnnot, self).__init__(_obj)

    def GetNumQuads(self):
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotGetNumQuads(self.obj)
        return ret

    def GetQuad(self, _index):
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdfLinkAnnotGetQuad(self.obj, _index, _quad)
        result.SetIntStruct(_quad)
        return result

    def AddQuad(self, _quad):
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotAddQuad(self.obj, _quad.GetIntStruct())
        return ret

    def RemoveQuad(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotRemoveQuad(self.obj, _index)
        return ret

    def GetAction(self):
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

class PdfMarkupAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfMarkupAnnot, self).__init__(_obj)

    def GetContents(self):
        global PdfixLib
        _len = PdfixLib.PdfMarkupAnnotGetContents(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfMarkupAnnotGetContents(self.obj, _buffer, _len)
        return _buffer.value

    def SetContents(self, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotSetContents(self.obj, _buffer)
        return ret

    def GetAuthor(self):
        global PdfixLib
        _len = PdfixLib.PdfMarkupAnnotGetAuthor(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfMarkupAnnotGetAuthor(self.obj, _buffer, _len)
        return _buffer.value

    def SetAuthor(self, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotSetAuthor(self.obj, _buffer)
        return ret

    def GetNumReplies(self):
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotGetNumReplies(self.obj)
        return ret

    def GetReply(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotGetReply(self.obj, _index)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

    def AddReply(self, _author, _text):
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotAddReply(self.obj, _author, _text)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

class PdfTextAnnot(PdfMarkupAnnot):
    def __init__(self, _obj):
        super(PdfTextAnnot, self).__init__(_obj)

class PdfTextMarkupAnnot(PdfMarkupAnnot):
    def __init__(self, _obj):
        super(PdfTextMarkupAnnot, self).__init__(_obj)

    def GetNumQuads(self):
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotGetNumQuads(self.obj)
        return ret

    def GetQuad(self, _index):
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdfTextMarkupAnnotGetQuad(self.obj, _index, _quad)
        result.SetIntStruct(_quad)
        return result

    def AddQuad(self, _quad):
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotAddQuad(self.obj, _quad.GetIntStruct())
        return ret

    def RemoveQuad(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotRemoveQuad(self.obj, _index)
        return ret

class PdfWidgetAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfWidgetAnnot, self).__init__(_obj)

    def GetCaption(self):
        global PdfixLib
        _len = PdfixLib.PdfWidgetAnnotGetCaption(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfWidgetAnnotGetCaption(self.obj, _buffer, _len)
        return _buffer.value

    def GetFontName(self):
        global PdfixLib
        _len = PdfixLib.PdfWidgetAnnotGetFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfWidgetAnnotGetFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetAction(self):
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetAAction(self, _event):
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetAAction(self.obj, _event)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetFormField(self):
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetFormField(self.obj)
        if ret:
            return PdfFormField(ret)
        else:
            return None

class PdfBaseDigSig(_PdfixBase):
    def __init__(self, _obj):
        super(PdfBaseDigSig, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigDestroy(self.obj)
        return ret

    def SetReason(self, _reason):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetReason(self.obj, _reason)
        return ret

    def SetLocation(self, _location):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetLocation(self.obj, _location)
        return ret

    def SetContactInfo(self, _contact):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetContactInfo(self.obj, _contact)
        return ret

    def SetName(self, _name):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetName(self.obj, _name)
        return ret

    def SetTimeStampServer(self, _url, _user_name, _password):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetTimeStampServer(self.obj, _url, _user_name, _password)
        return ret

    def SignDoc(self, _doc, _path):
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSignDoc(self.obj, _doc.obj, _path)
        return ret

class PdfDigSig(PdfBaseDigSig):
    def __init__(self, _obj):
        super(PdfDigSig, self).__init__(_obj)

    def SetPfxFile(self, _pfx_file, _pfx_password):
        global PdfixLib
        ret = PdfixLib.PdfDigSigSetPfxFile(self.obj, _pfx_file, _pfx_password)
        return ret

class PdfCustomDigSig(PdfBaseDigSig):
    def __init__(self, _obj):
        super(PdfCustomDigSig, self).__init__(_obj)

    def RegisterDigestDataProc(self, _proc, _data):
        global PdfixLib
        ret = PdfixLib.PdfCustomDigSigRegisterDigestDataProc(self.obj, _proc, _data)
        return ret

class PdfDoc(_PdfixBase):
    def __init__(self, _obj):
        super(PdfDoc, self).__init__(_obj)

    def Save(self, _path, _flags):
        global PdfixLib
        ret = PdfixLib.PdfDocSave(self.obj, _path, _flags)
        return ret

    def SaveToStream(self, _stream, _flags):
        global PdfixLib
        ret = PdfixLib.PdfDocSaveToStream(self.obj, _stream.obj, _flags)
        return ret

    def Close(self):
        global PdfixLib
        ret = PdfixLib.PdfDocClose(self.obj)
        return ret

    def AddWatermarkFromImage(self, _params, _path):
        global PdfixLib
        ret = PdfixLib.PdfDocAddWatermarkFromImage(self.obj, _params.GetIntStruct(), _path)
        return ret

    def GetNumPages(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumPages(self.obj)
        return ret

    def AcquirePage(self, _page_num):
        global PdfixLib
        ret = PdfixLib.PdfDocAcquirePage(self.obj, _page_num)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def ReleasePage(self, _page):
        global PdfixLib
        ret = PdfixLib.PdfDocReleasePage(self.obj, _page.obj)
        return ret

    def GetNumDocumentJavaScripts(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumDocumentJavaScripts(self.obj)
        return ret

    def GetDocumentJavaScript(self, _index):
        global PdfixLib
        _len = PdfixLib.PdfDocGetDocumentJavaScript(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetDocumentJavaScript(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetDocumentJavaScriptName(self, _index):
        global PdfixLib
        _len = PdfixLib.PdfDocGetDocumentJavaScriptName(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetDocumentJavaScriptName(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetNumCalculatedFormFields(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumCalculatedFormFields(self.obj)
        return ret

    def GetCalculatedFormField(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfDocGetCalculatedFormField(self.obj, _index)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetNumFormFields(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumFormFields(self.obj)
        return ret

    def GetFormField(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfDocGetFormField(self.obj, _index)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetFormFieldByName(self, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfDocGetFormFieldByName(self.obj, _buffer)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetInfo(self, _key):
        global PdfixLib
        _len = PdfixLib.PdfDocGetInfo(self.obj, _key, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetInfo(self.obj, _key, _buffer, _len)
        return _buffer.value

    def SetInfo(self, _key, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfDocSetInfo(self.obj, _key, _buffer)
        return ret

    def GetBookmarkRoot(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetBookmarkRoot(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def FlattenAnnots(self, _params):
        global PdfixLib
        ret = PdfixLib.PdfDocFlattenAnnots(self.obj, _params.GetIntStruct())
        return ret

    def RemoveStructTree(self):
        global PdfixLib
        ret = PdfixLib.PdfDocRemoveStructTree(self.obj)
        return ret

    def GetNumAlternates(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumAlternates(self.obj)
        return ret

    def AcquireAlternate(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfDocAcquireAlternate(self.obj, _index)
        if ret:
            return PdfAlternate(ret)
        else:
            return None

    def CreatePdsObject(self, _type, _indirect):
        global PdfixLib
        ret = PdfixLib.PdfDocCreatePdsObject(self.obj, _type, _indirect)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def AddTags(self, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfDocAddTags(self.obj, _cancel_proc, _cancel_data)
        return ret

    def GetDocTemplate(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetDocTemplate(self.obj)
        if ret:
            return PdfDocTemplate(ret)
        else:
            return None

    def GetMetadata(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetMetadata(self.obj)
        if ret:
            return PsMetadata(ret)
        else:
            return None

    def GetLang(self):
        global PdfixLib
        _len = PdfixLib.PdfDocGetLang(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetLang(self.obj, _buffer, _len)
        return _buffer.value

    def SetLang(self, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfDocSetLang(self.obj, _buffer)
        return ret

    def EmbedFonts(self, _subset, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfDocEmbedFonts(self.obj, _subset, _cancel_proc, _cancel_data)
        return ret

    def MakeAccessible(self, _params, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfDocMakeAccessible(self.obj, _params.GetIntStruct(), _cancel_proc, _cancel_data)
        return ret

    def GetRootObject(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetRootObject(self.obj)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetInfoObject(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetInfoObject(self.obj)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetStructTree(self):
        global PdfixLib
        ret = PdfixLib.PdfDocGetStructTree(self.obj)
        if ret:
            return PdsStructTree(ret)
        else:
            return None

class PdfDocTemplate(_PdfixBase):
    def __init__(self, _obj):
        super(PdfDocTemplate, self).__init__(_obj)

    def PreflightDoc(self, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfDocTemplatePreflightDoc(self.obj, _cancel_proc, _cancel_data)
        return ret

    def LoadFromStream(self, _stream, _format):
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateLoadFromStream(self.obj, _stream.obj, _format)
        return ret

    def SaveToStream(self, _stream, _format):
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSaveToStream(self.obj, _stream.obj, _format)
        return ret

    def SetDefaults(self):
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSetDefaults(self.obj)
        return ret

class PdfAlternate(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAlternate, self).__init__(_obj)

    def GetSubtype(self):
        global PdfixLib
        ret = PdfixLib.PdfAlternateGetSubtype(self.obj)
        return ret

    def GetName(self):
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetName(self.obj, _buffer, _len)
        return _buffer.value

    def GetDescription(self):
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetDescription(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetDescription(self.obj, _buffer, _len)
        return _buffer.value

    def GetFileName(self):
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetFileName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetFileName(self.obj, _buffer, _len)
        return _buffer.value

    def SaveContent(self, _path):
        global PdfixLib
        ret = PdfixLib.PdfAlternateSaveContent(self.obj, _path)
        return ret

    def Release(self):
        global PdfixLib
        ret = PdfixLib.PdfAlternateRelease(self.obj)
        return ret

class PdfHtmlAlternate(PdfAlternate):
    def __init__(self, _obj):
        super(PdfHtmlAlternate, self).__init__(_obj)

    def SaveResource(self, _resource_name, _path):
        global PdfixLib
        ret = PdfixLib.PdfHtmlAlternateSaveResource(self.obj, _resource_name, _path)
        return ret

class PdfFont(_PdfixBase):
    def __init__(self, _obj):
        super(PdfFont, self).__init__(_obj)

    def GetFontName(self):
        global PdfixLib
        _len = PdfixLib.PdfFontGetFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetFaceName(self):
        global PdfixLib
        _len = PdfixLib.PdfFontGetFaceName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetFaceName(self.obj, _buffer, _len)
        return _buffer.value

    def GetFontState(self):
        global PdfixLib
        result = PdfFontState()
        _font_state = result.GetIntStruct()
        PdfixLib.PdfFontGetFontState(self.obj, _font_state)
        result.SetIntStruct(_font_state)
        return result

    def GetSystemFontName(self):
        global PdfixLib
        _len = PdfixLib.PdfFontGetSystemFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetSystemFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetSystemFontCharset(self):
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontCharset(self.obj)
        return ret

    def GetSystemFontBold(self):
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontBold(self.obj)
        return ret

    def GetSystemFontItalic(self):
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontItalic(self.obj)
        return ret

    def SaveToStream(self, _stream, _format):
        global PdfixLib
        ret = PdfixLib.PdfFontSaveToStream(self.obj, _stream.obj, _format)
        return ret

class PdfFormField(_PdfixBase):
    def __init__(self, _obj):
        super(PdfFormField, self).__init__(_obj)

    def GetType(self):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetType(self.obj)
        return ret

    def GetFlags(self):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldSetFlags(self.obj, _flags)
        return ret

    def GetValue(self):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetValue(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetValue(self.obj, _buffer, _len)
        return _buffer.value

    def SetValue(self, _buffer):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldSetValue(self.obj, _buffer)
        return ret

    def GetDefaultValue(self):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetDefaultValue(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetDefaultValue(self.obj, _buffer, _len)
        return _buffer.value

    def GetFullName(self):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetFullName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetFullName(self.obj, _buffer, _len)
        return _buffer.value

    def GetTooltip(self):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetTooltip(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetTooltip(self.obj, _buffer, _len)
        return _buffer.value

    def GetOptionCount(self):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetOptionCount(self.obj)
        return ret

    def GetOptionValue(self, _index):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetOptionValue(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetOptionValue(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetOptionCaption(self, _index):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetOptionCaption(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetOptionCaption(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetAction(self):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetAAction(self, _event):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetAAction(self.obj, _event)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetMaxLength(self):
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetMaxLength(self.obj)
        return ret

    def GetWidgetExportValue(self, _annot):
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetWidgetExportValue(self.obj, _annot, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetWidgetExportValue(self.obj, _annot, _buffer, _len)
        return _buffer.value

class PsImage(_PdfixBase):
    def __init__(self, _obj):
        super(PsImage, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PsImageDestroy(self.obj)
        return ret

    def Save(self, _path, _params):
        global PdfixLib
        ret = PdfixLib.PsImageSave(self.obj, _path, _params.GetIntStruct())
        return ret

    def SaveRect(self, _path, _params, _dev_rect):
        global PdfixLib
        ret = PdfixLib.PsImageSaveRect(self.obj, _path, _params.GetIntStruct(), _dev_rect.GetIntStruct())
        return ret

    def SaveToStream(self, _stream, _params):
        global PdfixLib
        ret = PdfixLib.PsImageSaveToStream(self.obj, _stream.obj, _params.GetIntStruct())
        return ret

    def SaveRectToStream(self, _stream, _params, _dev_rect):
        global PdfixLib
        ret = PdfixLib.PsImageSaveRectToStream(self.obj, _stream.obj, _params.GetIntStruct(), _dev_rect.GetIntStruct())
        return ret

    def GetPointColor(self, _point):
        global PdfixLib
        result = PdfRGB()
        _color = result.GetIntStruct()
        PdfixLib.PsImageGetPointColor(self.obj, _point, _color)
        result.SetIntStruct(_color)
        return result

class PdfPage(_PdfixBase):
    def __init__(self, _obj):
        super(PdfPage, self).__init__(_obj)

    def GetCropBox(self):
        global PdfixLib
        result = PdfRect()
        _crop_box = result.GetIntStruct()
        PdfixLib.PdfPageGetCropBox(self.obj, _crop_box)
        result.SetIntStruct(_crop_box)
        return result

    def GetMediaBox(self):
        global PdfixLib
        result = PdfRect()
        _media_box = result.GetIntStruct()
        PdfixLib.PdfPageGetMediaBox(self.obj, _media_box)
        result.SetIntStruct(_media_box)
        return result

    def GetRotate(self):
        global PdfixLib
        ret = PdfixLib.PdfPageGetRotate(self.obj)
        return ret

    def GetDefaultMatrix(self):
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdfPageGetDefaultMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def GetNumber(self):
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumber(self.obj)
        return ret

    def AcquirePageMap(self, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfPageAcquirePageMap(self.obj, _cancel_proc, _cancel_data)
        if ret:
            return PdePageMap(ret)
        else:
            return None

    def ReleasePageMap(self):
        global PdfixLib
        ret = PdfixLib.PdfPageReleasePageMap(self.obj)
        return ret

    def AcquirePageView(self, _zoom, _rotate):
        global PdfixLib
        ret = PdfixLib.PdfPageAcquirePageView(self.obj, _zoom, _rotate)
        if ret:
            return PdfPageView(ret)
        else:
            return None

    def ReleasePageView(self, _page_view):
        global PdfixLib
        ret = PdfixLib.PdfPageReleasePageView(self.obj, _page_view.obj)
        return ret

    def GetNumAnnots(self):
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnots(self.obj)
        return ret

    def GetAnnot(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnot(self.obj, _index)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

    def RemoveAnnot(self, _index, _flags):
        global PdfixLib
        ret = PdfixLib.PdfPageRemoveAnnot(self.obj, _index, _flags)
        return ret

    def AddTextAnnot(self, _index, _rect):
        global PdfixLib
        ret = PdfixLib.PdfPageAddTextAnnot(self.obj, _index, _rect.GetIntStruct())
        if ret:
            return PdfTextAnnot(ret)
        else:
            return None

    def AddLinkAnnot(self, _index, _rect):
        global PdfixLib
        ret = PdfixLib.PdfPageAddLinkAnnot(self.obj, _index, _rect.GetIntStruct())
        if ret:
            return PdfLinkAnnot(ret)
        else:
            return None

    def AddTextMarkupAnnot(self, _index, _rect, _subtype):
        global PdfixLib
        ret = PdfixLib.PdfPageAddTextMarkupAnnot(self.obj, _index, _rect.GetIntStruct(), _subtype)
        if ret:
            return PdfTextMarkupAnnot(ret)
        else:
            return None

    def GetNumAnnotsAtPoint(self, _point):
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnotsAtPoint(self.obj, _point.GetIntStruct())
        return ret

    def GetAnnotAtPoint(self, _point, _index):
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnotAtPoint(self.obj, _point.GetIntStruct(), _index)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

    def GetNumAnnotsAtRect(self, _rect):
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnotsAtRect(self.obj, _rect.GetIntStruct())
        return ret

    def GetAnnotAtRect(self, _rect, _index):
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnotAtRect(self.obj, _rect.GetIntStruct(), _index)
        if ret:
            return PdfAnnot(ret)
        else:
            return None

    def DrawContent(self, _params, _cancel_proc, _cancel_data):
        global PdfixLib
        ret = PdfixLib.PdfPageDrawContent(self.obj, _params.GetIntStruct(), _cancel_proc, _cancel_data)
        return ret

    def GetNumMcidPageObjects(self, _mcid):
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumMcidPageObjects(self.obj, _mcid)
        return ret

    def GetMcidPageObject(self, _mcid, _index):
        global PdfixLib
        ret = PdfixLib.PdfPageGetMcidPageObject(self.obj, _mcid, _index)
        if ret:
            return PdsPageObject(ret)
        else:
            return None

class PdePageMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdePageMap, self).__init__(_obj)

    def GetElement(self):
        global PdfixLib
        ret = PdfixLib.PdePageMapGetElement(self.obj)
        if ret:
            return PdeElement(ret)
        else:
            return None

    def GetWhitespace(self, _params, _index):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdePageMapGetWhitespace(self.obj, _params, _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetBBox(self):
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdePageMapGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

class PdfPageView(_PdfixBase):
    def __init__(self, _obj):
        super(PdfPageView, self).__init__(_obj)

    def GetDeviceWidth(self):
        global PdfixLib
        ret = PdfixLib.PdfPageViewGetDeviceWidth(self.obj)
        return ret

    def GetDeviceHeight(self):
        global PdfixLib
        ret = PdfixLib.PdfPageViewGetDeviceHeight(self.obj)
        return ret

    def GetDeviceMatrix(self):
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdfPageViewGetDeviceMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def RectToDevice(self, _rect):
        global PdfixLib
        result = PdfDevRect()
        _dev_rect = result.GetIntStruct()
        PdfixLib.PdfPageViewRectToDevice(self.obj, _rect, _dev_rect)
        result.SetIntStruct(_dev_rect)
        return result

    def PointToDevice(self, _point):
        global PdfixLib
        result = PdfDevPoint()
        _dev_point = result.GetIntStruct()
        PdfixLib.PdfPageViewPointToDevice(self.obj, _point, _dev_point)
        result.SetIntStruct(_dev_point)
        return result

class PdfBookmark(_PdfixBase):
    def __init__(self, _obj):
        super(PdfBookmark, self).__init__(_obj)

    def GetTitle(self):
        global PdfixLib
        _len = PdfixLib.PdfBookmarkGetTitle(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfBookmarkGetTitle(self.obj, _buffer, _len)
        return _buffer.value

    def GetAppearance(self, _appearance):
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetAppearance(self.obj, _appearance.GetIntStruct())
        return ret

    def GetAction(self):
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetNumChildren(self):
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetNumChildren(self.obj)
        return ret

    def GetChild(self, _index):
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetChild(self.obj, _index)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetParent(self):
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetParent(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

class PsRegex(_PdfixBase):
    def __init__(self, _obj):
        super(PsRegex, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PsRegexDestroy(self.obj)
        return ret

    def SetPattern(self, _pattern):
        global PdfixLib
        ret = PdfixLib.PsRegexSetPattern(self.obj, _pattern)
        return ret

    def Search(self, _text, _position):
        global PdfixLib
        ret = PdfixLib.PsRegexSearch(self.obj, _text, _position)
        return ret

    def GetText(self):
        global PdfixLib
        _len = PdfixLib.PsRegexGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsRegexGetText(self.obj, _buffer, _len)
        return _buffer.value

    def GetPosition(self):
        global PdfixLib
        ret = PdfixLib.PsRegexGetPosition(self.obj)
        return ret

    def GetLength(self):
        global PdfixLib
        ret = PdfixLib.PsRegexGetLength(self.obj)
        return ret

    def GetNumMatches(self):
        global PdfixLib
        ret = PdfixLib.PsRegexGetNumMatches(self.obj)
        return ret

    def GetMatchText(self, _index):
        global PdfixLib
        _len = PdfixLib.PsRegexGetMatchText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsRegexGetMatchText(self.obj, _index, _buffer, _len)
        return _buffer.value

class PsStream(_PdfixBase):
    def __init__(self, _obj):
        super(PsStream, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PsStreamDestroy(self.obj)
        return ret

    def IsEof(self):
        global PdfixLib
        ret = PdfixLib.PsStreamIsEof(self.obj)
        return ret

    def GetSize(self):
        global PdfixLib
        ret = PdfixLib.PsStreamGetSize(self.obj)
        return ret

    def Read(self, _offset, _buffer, _size):
        global PdfixLib
        ret = PdfixLib.PsStreamRead(self.obj, _offset, _buffer, _size)
        return ret

    def Write(self, _offset, _buffer, _size):
        global PdfixLib
        ret = PdfixLib.PsStreamWrite(self.obj, _offset, _buffer, _size)
        return ret

    def GetPos(self):
        global PdfixLib
        ret = PdfixLib.PsStreamGetPos(self.obj)
        return ret

    def Flush(self):
        global PdfixLib
        ret = PdfixLib.PsStreamFlush(self.obj)
        return ret

    def GetStream(self):
        global PdfixLib
        ret = PdfixLib.PsStreamGetStream(self.obj)
        return ret

    def GetType(self):
        global PdfixLib
        ret = PdfixLib.PsStreamGetType(self.obj)
        return ret

class PsFileStream(PsStream):
    def __init__(self, _obj):
        super(PsFileStream, self).__init__(_obj)

class PsMemoryStream(PsStream):
    def __init__(self, _obj):
        super(PsMemoryStream, self).__init__(_obj)

    def Resize(self, _size):
        global PdfixLib
        ret = PdfixLib.PsMemoryStreamResize(self.obj, _size)
        return ret

class PsProcStream(PsStream):
    def __init__(self, _obj):
        super(PsProcStream, self).__init__(_obj)

    def SetReadProc(self, _proc):
        global PdfixLib
        ret = PdfixLib.PsProcStreamSetReadProc(self.obj, _proc)
        return ret

    def SetWriteProc(self, _proc):
        global PdfixLib
        ret = PdfixLib.PsProcStreamSetWriteProc(self.obj, _proc)
        return ret

    def SetDestroyProc(self, _proc):
        global PdfixLib
        ret = PdfixLib.PsProcStreamSetDestroyProc(self.obj, _proc)
        return ret

    def SetGetSizeProc(self, _proc):
        global PdfixLib
        ret = PdfixLib.PsProcStreamSetGetSizeProc(self.obj, _proc)
        return ret

class PdsStructElement(_PdfixBase):
    def __init__(self, _obj):
        super(PdsStructElement, self).__init__(_obj)

    def GetType(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetType(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetType(self.obj, _buffer, _len)
        return _buffer.value

    def GetActualText(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetActualText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetActualText(self.obj, _buffer, _len)
        return _buffer.value

    def GetAlt(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetAlt(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetAlt(self.obj, _buffer, _len)
        return _buffer.value

    def GetAbbreviation(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetAbbreviation(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetAbbreviation(self.obj, _buffer, _len)
        return _buffer.value

    def GetPageNumber(self):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetPageNumber(self.obj)
        return ret

    def GetAttrObject(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetAttrObject(self.obj, _index)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetElementObject(self):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetElementObject(self.obj)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetKidObject(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetKidObject(self.obj, _index)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetKidType(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetKidType(self.obj, _index)
        return ret

    def GetKidPageNumber(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetKidPageNumber(self.obj, _index)
        return ret

    def GetKidMcid(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetKidMcid(self.obj, _index)
        return ret

    def GetNumAttrObjects(self):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumAttrObjects(self.obj)
        return ret

    def GetNumKids(self):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumKids(self.obj)
        return ret

    def GetParentObject(self):
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetParentObject(self.obj)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetTitle(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetTitle(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetTitle(self.obj, _buffer, _len)
        return _buffer.value

    def GetID(self):
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetID(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetID(self.obj, _buffer, _len)
        return _buffer.value

class PdsClassMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdsClassMap, self).__init__(_obj)

    def GetAttrObject(self, _class_name, _index):
        global PdfixLib
        ret = PdfixLib.PdsClassMapGetAttrObject(self.obj, _class_name, _index)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetNumAttrObjects(self, _class_name):
        global PdfixLib
        ret = PdfixLib.PdsClassMapGetNumAttrObjects(self.obj, _class_name)
        return ret

class PdsRoleMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdsRoleMap, self).__init__(_obj)

    def DoesMap(self, _src, _dst):
        global PdfixLib
        ret = PdfixLib.PdsRoleMapDoesMap(self.obj, _src, _dst)
        return ret

    def GetDirectMap(self, _type):
        global PdfixLib
        _len = PdfixLib.PdsRoleMapGetDirectMap(self.obj, _type, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsRoleMapGetDirectMap(self.obj, _type, _buffer, _len)
        return _buffer.value

class PdsStructTree(_PdfixBase):
    def __init__(self, _obj):
        super(PdsStructTree, self).__init__(_obj)

    def GetClassMap(self):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetClassMap(self.obj)
        if ret:
            return PdsClassMap(ret)
        else:
            return None

    def GetKidObject(self, _index):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetKidObject(self.obj, _index)
        if ret:
            return PdsObject(ret)
        else:
            return None

    def GetNumKids(self):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetNumKids(self.obj)
        return ret

    def GetRoleMap(self):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetRoleMap(self.obj)
        if ret:
            return PdsRoleMap(ret)
        else:
            return None

    def AcquireStructElement(self, _object):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeAcquireStructElement(self.obj, _object.obj)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def ReleaseStructElement(self, _element):
        global PdfixLib
        ret = PdfixLib.PdsStructTreeReleaseStructElement(self.obj, _element.obj)
        return ret

class PsMetadata(_PdfixBase):
    def __init__(self, _obj):
        super(PsMetadata, self).__init__(_obj)

    def SaveToStream(self, _stream):
        global PdfixLib
        ret = PdfixLib.PsMetadataSaveToStream(self.obj, _stream.obj)
        return ret

    def LoadFromStream(self, _stream):
        global PdfixLib
        ret = PdfixLib.PsMetadataLoadFromStream(self.obj, _stream.obj)
        return ret

class Pdfix(_PdfixBase):
    def __init__(self, _obj):
        super(Pdfix, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PdfixDestroy(self.obj)
        return ret

    def Authorize(self, _email, _serial_number):
        global PdfixLib
        ret = PdfixLib.PdfixAuthorize(self.obj, _email, _serial_number)
        return ret

    def IsAuthorized(self):
        global PdfixLib
        ret = PdfixLib.PdfixIsAuthorized(self.obj)
        return ret

    def IsAuthorizedPlatform(self, _platform):
        global PdfixLib
        ret = PdfixLib.PdfixIsAuthorizedPlatform(self.obj, _platform)
        return ret

    def IsAuthorizedOption(self, _option):
        global PdfixLib
        ret = PdfixLib.PdfixIsAuthorizedOption(self.obj, _option)
        return ret

    def GetErrorType(self):
        global PdfixLib
        ret = PdfixLib.PdfixGetErrorType(self.obj)
        return ret

    def GetError(self):
        global PdfixLib
        ret = PdfixLib.PdfixGetError(self.obj)
        return ret

    def SetError(self, _type, _error):
        global PdfixLib
        ret = PdfixLib.PdfixSetError(self.obj, _type, _error)
        return ret

    def GetVersionMajor(self):
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionMajor(self.obj)
        return ret

    def GetVersionMinor(self):
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionMinor(self.obj)
        return ret

    def GetVersionPatch(self):
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionPatch(self.obj)
        return ret

    def OpenDoc(self, _path, _password):
        global PdfixLib
        ret = PdfixLib.PdfixOpenDoc(self.obj, _path, _password)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def OpenDocFromStream(self, _stream, _password):
        global PdfixLib
        ret = PdfixLib.PdfixOpenDocFromStream(self.obj, _stream.obj, _password)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def CreateDigSig(self):
        global PdfixLib
        ret = PdfixLib.PdfixCreateDigSig(self.obj)
        if ret:
            return PdfDigSig(ret)
        else:
            return None

    def CreateCustomDigSig(self):
        global PdfixLib
        ret = PdfixLib.PdfixCreateCustomDigSig(self.obj)
        if ret:
            return PdfCustomDigSig(ret)
        else:
            return None

    def CreateRegex(self):
        global PdfixLib
        ret = PdfixLib.PdfixCreateRegex(self.obj)
        if ret:
            return PsRegex(ret)
        else:
            return None

    def CreateFileStream(self, _path, _mode):
        global PdfixLib
        ret = PdfixLib.PdfixCreateFileStream(self.obj, _path, _mode)
        if ret:
            return PsFileStream(ret)
        else:
            return None

    def CreateMemStream(self):
        global PdfixLib
        ret = PdfixLib.PdfixCreateMemStream(self.obj)
        if ret:
            return PsMemoryStream(ret)
        else:
            return None

    def CreateCustomStream(self, _read_proc, _client_data):
        global PdfixLib
        ret = PdfixLib.PdfixCreateCustomStream(self.obj, _read_proc, _client_data)
        if ret:
            return PsProcStream(ret)
        else:
            return None

    def RegisterEvent(self, _type, _proc, _data):
        global PdfixLib
        ret = PdfixLib.PdfixRegisterEvent(self.obj, _type, _proc, _data)
        return ret

    def UnregisterEvent(self, _type, _proc, _data):
        global PdfixLib
        ret = PdfixLib.PdfixUnregisterEvent(self.obj, _type, _proc, _data)
        return ret

    def SetRegex(self, _type, _regex):
        global PdfixLib
        ret = PdfixLib.PdfixSetRegex(self.obj, _type, _regex)
        return ret

    def CreateImage(self, _width, _height, _format):
        global PdfixLib
        ret = PdfixLib.PdfixCreateImage(self.obj, _width, _height, _format)
        if ret:
            return PsImage(ret)
        else:
            return None

class PdfixPlugin(_PdfixBase):
    def __init__(self, _obj):
        super(PdfixPlugin, self).__init__(_obj)

    def Destroy(self):
        global PdfixLib
        ret = PdfixLib.PdfixPluginDestroy(self.obj)
        return ret

    def Initialize(self, _pdfix):
        global PdfixLib
        ret = PdfixLib.PdfixPluginInitialize(self.obj, _pdfix.obj)
        return ret

    def GetVersionMajor(self):
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionMajor(self.obj)
        return ret

    def GetVersionMinor(self):
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionMinor(self.obj)
        return ret

    def GetVersionPatch(self):
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionPatch(self.obj)
        return ret

    def GetPdfix(self):
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetPdfix(self.obj)
        if ret:
            return Pdfix(ret)
        else:
            return None

def GetPdfix():
    global PdfixLib
    obj = PdfixLib.GetPdfix()
    return Pdfix(obj)

PdfixLib = None

def Pdfix_init(path):
    global PdfixLib
    PdfixLib = cdll.LoadLibrary(path)
    if PdfixLib is None:
        raise Exception("LoadLibrary fail")
    PdfixLib.PdsObjectGetObjectType.restype = c_int
    PdfixLib.PdsObjectGetObjectType.argtypes = [c_void_p]
    PdfixLib.PdsBooleanGetValue.restype = c_int
    PdfixLib.PdsBooleanGetValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberIsIntegerValue.restype = c_int
    PdfixLib.PdsNumberIsIntegerValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberGetIntegerValue.restype = c_int
    PdfixLib.PdsNumberGetIntegerValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberGetValue.restype = c_double
    PdfixLib.PdsNumberGetValue.argtypes = [c_void_p]
    PdfixLib.PdsStringGetValue.restype = c_int
    PdfixLib.PdsStringGetValue.argtypes = [c_void_p, c_char_p, c_int]
    PdfixLib.PdsStringGetText.restype = c_int
    PdfixLib.PdsStringGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsNameGetValue.restype = c_int
    PdfixLib.PdsNameGetValue.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsArrayGetNumObjects.restype = c_int
    PdfixLib.PdsArrayGetNumObjects.argtypes = [c_void_p]
    PdfixLib.PdsArrayGet.restype = c_void_p
    PdfixLib.PdsArrayGet.argtypes = [c_void_p, c_int]
    PdfixLib.PdsDictionaryKnown.restype = c_int
    PdfixLib.PdsDictionaryKnown.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetNumKeys.restype = c_int
    PdfixLib.PdsDictionaryGetNumKeys.argtypes = [c_void_p]
    PdfixLib.PdsDictionaryGetKey.restype = c_int
    PdfixLib.PdsDictionaryGetKey.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryGet.restype = c_void_p
    PdfixLib.PdsDictionaryGet.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStreamGetStreamDict.restype = c_void_p
    PdfixLib.PdsStreamGetStreamDict.argtypes = [c_void_p]
    PdfixLib.PdsStreamGetRawDataSize.restype = c_int
    PdfixLib.PdsStreamGetRawDataSize.argtypes = [c_void_p]
    PdfixLib.PdsReferenceGetObjectNumber.restype = c_int
    PdfixLib.PdsReferenceGetObjectNumber.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetObjectType.restype = c_int
    PdfixLib.PdsPageObjectGetObjectType.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetBBox.restype = c_int
    PdfixLib.PdsPageObjectGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdsTextGetText.restype = c_int
    PdfixLib.PdsTextGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeElementGetType.restype = c_int
    PdfixLib.PdeElementGetType.argtypes = [c_void_p]
    PdfixLib.PdeElementGetBBox.restype = c_int
    PdfixLib.PdeElementGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdeElementGetId.restype = c_int
    PdfixLib.PdeElementGetId.argtypes = [c_void_p]
    PdfixLib.PdeElementGetGraphicState.restype = c_int
    PdfixLib.PdeElementGetGraphicState.argtypes = [c_void_p, POINTER(zz_PdfGraphicState)]
    PdfixLib.PdeElementGetNumChildren.restype = c_int
    PdfixLib.PdeElementGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdeElementGetChild.restype = c_void_p
    PdfixLib.PdeElementGetChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdeElementGetAlignment.restype = c_int
    PdfixLib.PdeElementGetAlignment.argtypes = [c_void_p]
    PdfixLib.PdeElementGetAngle.restype = c_double
    PdfixLib.PdeElementGetAngle.argtypes = [c_void_p]
    PdfixLib.PdeElementSetRenderMode.restype = c_int
    PdfixLib.PdeElementSetRenderMode.argtypes = [c_void_p, c_int]
    PdfixLib.PdeAnnotGetAnnot.restype = c_void_p
    PdfixLib.PdeAnnotGetAnnot.argtypes = [c_void_p]
    PdfixLib.PdeImageGetImageType.restype = c_int
    PdfixLib.PdeImageGetImageType.argtypes = [c_void_p]
    PdfixLib.PdeImageGetCaption.restype = c_void_p
    PdfixLib.PdeImageGetCaption.argtypes = [c_void_p]
    PdfixLib.PdeCellGetRowSpan.restype = c_int
    PdfixLib.PdeCellGetRowSpan.argtypes = [c_void_p]
    PdfixLib.PdeCellGetColSpan.restype = c_int
    PdfixLib.PdeCellGetColSpan.argtypes = [c_void_p]
    PdfixLib.PdeCellHasBorderGraphicState.restype = c_int
    PdfixLib.PdeCellHasBorderGraphicState.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetSpanCell.restype = c_void_p
    PdfixLib.PdeCellGetSpanCell.argtypes = [c_void_p]
    PdfixLib.PdeTableGetNumRows.restype = c_int
    PdfixLib.PdeTableGetNumRows.argtypes = [c_void_p]
    PdfixLib.PdeTableGetNumCols.restype = c_int
    PdfixLib.PdeTableGetNumCols.argtypes = [c_void_p]
    PdfixLib.PdeTableGetCell.restype = c_void_p
    PdfixLib.PdeTableGetCell.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdeTableGetRowAlignment.restype = c_int
    PdfixLib.PdeTableGetRowAlignment.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetColAlignment.restype = c_int
    PdfixLib.PdeTableGetColAlignment.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetCaption.restype = c_void_p
    PdfixLib.PdeTableGetCaption.argtypes = [c_void_p]
    PdfixLib.PdeTableGetTableType.restype = c_int
    PdfixLib.PdeTableGetTableType.argtypes = [c_void_p]
    PdfixLib.PdeWordGetText.restype = c_int
    PdfixLib.PdeWordGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeWordHasTextState.restype = c_int
    PdfixLib.PdeWordHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeWordGetTextState.restype = c_int
    PdfixLib.PdeWordGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeWordGetNumChars.restype = c_int
    PdfixLib.PdeWordGetNumChars.argtypes = [c_void_p]
    PdfixLib.PdeWordGetCharCode.restype = c_int
    PdfixLib.PdeWordGetCharCode.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordGetCharText.restype = c_int
    PdfixLib.PdeWordGetCharText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdeWordGetCharTextState.restype = c_int
    PdfixLib.PdeWordGetCharTextState.argtypes = [c_void_p, c_int, POINTER(zz_PdfTextState)]
    PdfixLib.PdeWordGetCharBBox.restype = c_int
    PdfixLib.PdeWordGetCharBBox.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdeWordGetFlags.restype = c_int
    PdfixLib.PdeWordGetFlags.argtypes = [c_void_p]
    PdfixLib.PdeWordGetBackground.restype = c_void_p
    PdfixLib.PdeWordGetBackground.argtypes = [c_void_p]
    PdfixLib.PdeWordGetOrigin.restype = c_int
    PdfixLib.PdeWordGetOrigin.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdeTextLineGetText.restype = c_int
    PdfixLib.PdeTextLineGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeTextLineHasTextState.restype = c_int
    PdfixLib.PdeTextLineHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeTextLineGetTextState.restype = c_int
    PdfixLib.PdeTextLineGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeTextLineGetNumWords.restype = c_int
    PdfixLib.PdeTextLineGetNumWords.argtypes = [c_void_p]
    PdfixLib.PdeTextLineGetWord.restype = c_void_p
    PdfixLib.PdeTextLineGetWord.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextLineGetFlags.restype = c_int
    PdfixLib.PdeTextLineGetFlags.argtypes = [c_void_p]
    PdfixLib.PdeTextGetText.restype = c_int
    PdfixLib.PdeTextGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeTextHasTextState.restype = c_int
    PdfixLib.PdeTextHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextState.restype = c_int
    PdfixLib.PdeTextGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeTextGetNumTextLines.restype = c_int
    PdfixLib.PdeTextGetNumTextLines.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextLine.restype = c_void_p
    PdfixLib.PdeTextGetTextLine.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextGetNumWords.restype = c_int
    PdfixLib.PdeTextGetNumWords.argtypes = [c_void_p]
    PdfixLib.PdeTextGetWord.restype = c_void_p
    PdfixLib.PdeTextGetWord.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextGetLineSpacing.restype = c_double
    PdfixLib.PdeTextGetLineSpacing.argtypes = [c_void_p]
    PdfixLib.PdeTextGetIndent.restype = c_double
    PdfixLib.PdeTextGetIndent.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextStyle.restype = c_int
    PdfixLib.PdeTextGetTextStyle.argtypes = [c_void_p]
    PdfixLib.PdfActionGetSubtype.restype = c_int
    PdfixLib.PdfActionGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfActionGetJavaScript.restype = c_int
    PdfixLib.PdfActionGetJavaScript.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfActionGetURI.restype = c_int
    PdfixLib.PdfActionGetURI.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAnnotGetSubtype.restype = c_int
    PdfixLib.PdfAnnotGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfAnnotGetFlags.restype = c_int
    PdfixLib.PdfAnnotGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfAnnotGetAppearance.restype = c_int
    PdfixLib.PdfAnnotGetAppearance.argtypes = [c_void_p, POINTER(zz_PdfAnnotAppearance)]
    PdfixLib.PdfAnnotGetBBox.restype = c_int
    PdfixLib.PdfAnnotGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfAnnotPointInAnnot.restype = c_int
    PdfixLib.PdfAnnotPointInAnnot.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdfAnnotRectInAnnot.restype = c_int
    PdfixLib.PdfAnnotRectInAnnot.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfLinkAnnotGetNumQuads.restype = c_int
    PdfixLib.PdfLinkAnnotGetNumQuads.argtypes = [c_void_p]
    PdfixLib.PdfLinkAnnotGetQuad.restype = c_int
    PdfixLib.PdfLinkAnnotGetQuad.argtypes = [c_void_p, c_int, POINTER(zz_PdfQuad)]
    PdfixLib.PdfLinkAnnotAddQuad.restype = c_int
    PdfixLib.PdfLinkAnnotAddQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdfLinkAnnotRemoveQuad.restype = c_int
    PdfixLib.PdfLinkAnnotRemoveQuad.argtypes = [c_void_p, c_int]
    PdfixLib.PdfLinkAnnotGetAction.restype = c_void_p
    PdfixLib.PdfLinkAnnotGetAction.argtypes = [c_void_p]
    PdfixLib.PdfMarkupAnnotGetContents.restype = c_int
    PdfixLib.PdfMarkupAnnotGetContents.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfMarkupAnnotSetContents.restype = c_int
    PdfixLib.PdfMarkupAnnotSetContents.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfMarkupAnnotGetAuthor.restype = c_int
    PdfixLib.PdfMarkupAnnotGetAuthor.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfMarkupAnnotSetAuthor.restype = c_int
    PdfixLib.PdfMarkupAnnotSetAuthor.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfMarkupAnnotGetNumReplies.restype = c_int
    PdfixLib.PdfMarkupAnnotGetNumReplies.argtypes = [c_void_p]
    PdfixLib.PdfMarkupAnnotGetReply.restype = c_void_p
    PdfixLib.PdfMarkupAnnotGetReply.argtypes = [c_void_p, c_int]
    PdfixLib.PdfMarkupAnnotAddReply.restype = c_void_p
    PdfixLib.PdfMarkupAnnotAddReply.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfTextMarkupAnnotGetNumQuads.restype = c_int
    PdfixLib.PdfTextMarkupAnnotGetNumQuads.argtypes = [c_void_p]
    PdfixLib.PdfTextMarkupAnnotGetQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotGetQuad.argtypes = [c_void_p, c_int, POINTER(zz_PdfQuad)]
    PdfixLib.PdfTextMarkupAnnotAddQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotAddQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdfTextMarkupAnnotRemoveQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotRemoveQuad.argtypes = [c_void_p, c_int]
    PdfixLib.PdfWidgetAnnotGetCaption.restype = c_int
    PdfixLib.PdfWidgetAnnotGetCaption.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfWidgetAnnotGetFontName.restype = c_int
    PdfixLib.PdfWidgetAnnotGetFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfWidgetAnnotGetAction.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetAction.argtypes = [c_void_p]
    PdfixLib.PdfWidgetAnnotGetAAction.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetAAction.argtypes = [c_void_p, c_int]
    PdfixLib.PdfWidgetAnnotGetFormField.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetFormField.argtypes = [c_void_p]
    PdfixLib.PdfBaseDigSigDestroy.restype = c_int
    PdfixLib.PdfBaseDigSigDestroy.argtypes = [c_void_p]
    PdfixLib.PdfBaseDigSigSetReason.restype = c_int
    PdfixLib.PdfBaseDigSigSetReason.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetLocation.restype = c_int
    PdfixLib.PdfBaseDigSigSetLocation.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetContactInfo.restype = c_int
    PdfixLib.PdfBaseDigSigSetContactInfo.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetName.restype = c_int
    PdfixLib.PdfBaseDigSigSetName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetTimeStampServer.restype = c_int
    PdfixLib.PdfBaseDigSigSetTimeStampServer.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSignDoc.restype = c_int
    PdfixLib.PdfBaseDigSigSignDoc.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfDigSigSetPfxFile.restype = c_int
    PdfixLib.PdfDigSigSetPfxFile.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfCustomDigSigRegisterDigestDataProc.restype = c_int
    PdfixLib.PdfCustomDigSigRegisterDigestDataProc.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfDocSave.restype = c_int
    PdfixLib.PdfDocSave.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSaveToStream.restype = c_int
    PdfixLib.PdfDocSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocClose.restype = c_int
    PdfixLib.PdfDocClose.argtypes = [c_void_p]
    PdfixLib.PdfDocAddWatermarkFromImage.restype = c_int
    PdfixLib.PdfDocAddWatermarkFromImage.argtypes = [c_void_p, POINTER(zz_PdfWatermarkParams), c_wchar_p]
    PdfixLib.PdfDocGetNumPages.restype = c_int
    PdfixLib.PdfDocGetNumPages.argtypes = [c_void_p]
    PdfixLib.PdfDocAcquirePage.restype = c_void_p
    PdfixLib.PdfDocAcquirePage.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocReleasePage.restype = c_int
    PdfixLib.PdfDocReleasePage.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetNumDocumentJavaScripts.restype = c_int
    PdfixLib.PdfDocGetNumDocumentJavaScripts.argtypes = [c_void_p]
    PdfixLib.PdfDocGetDocumentJavaScript.restype = c_int
    PdfixLib.PdfDocGetDocumentJavaScript.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfDocGetDocumentJavaScriptName.restype = c_int
    PdfixLib.PdfDocGetDocumentJavaScriptName.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfDocGetNumCalculatedFormFields.restype = c_int
    PdfixLib.PdfDocGetNumCalculatedFormFields.argtypes = [c_void_p]
    PdfixLib.PdfDocGetCalculatedFormField.restype = c_void_p
    PdfixLib.PdfDocGetCalculatedFormField.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetNumFormFields.restype = c_int
    PdfixLib.PdfDocGetNumFormFields.argtypes = [c_void_p]
    PdfixLib.PdfDocGetFormField.restype = c_void_p
    PdfixLib.PdfDocGetFormField.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetFormFieldByName.restype = c_void_p
    PdfixLib.PdfDocGetFormFieldByName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocGetInfo.restype = c_int
    PdfixLib.PdfDocGetInfo.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSetInfo.restype = c_int
    PdfixLib.PdfDocSetInfo.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfDocGetBookmarkRoot.restype = c_void_p
    PdfixLib.PdfDocGetBookmarkRoot.argtypes = [c_void_p]
    PdfixLib.PdfDocFlattenAnnots.restype = c_int
    PdfixLib.PdfDocFlattenAnnots.argtypes = [c_void_p, POINTER(zz_PdfFlattenAnnotsParams)]
    PdfixLib.PdfDocRemoveStructTree.restype = c_int
    PdfixLib.PdfDocRemoveStructTree.argtypes = [c_void_p]
    PdfixLib.PdfDocGetNumAlternates.restype = c_int
    PdfixLib.PdfDocGetNumAlternates.argtypes = [c_void_p]
    PdfixLib.PdfDocAcquireAlternate.restype = c_void_p
    PdfixLib.PdfDocAcquireAlternate.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreatePdsObject.restype = c_void_p
    PdfixLib.PdfDocCreatePdsObject.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfDocAddTags.restype = c_int
    PdfixLib.PdfDocAddTags.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfDocGetDocTemplate.restype = c_void_p
    PdfixLib.PdfDocGetDocTemplate.argtypes = [c_void_p]
    PdfixLib.PdfDocGetMetadata.restype = c_void_p
    PdfixLib.PdfDocGetMetadata.argtypes = [c_void_p]
    PdfixLib.PdfDocGetLang.restype = c_int
    PdfixLib.PdfDocGetLang.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSetLang.restype = c_int
    PdfixLib.PdfDocSetLang.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocEmbedFonts.restype = c_int
    PdfixLib.PdfDocEmbedFonts.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocMakeAccessible.restype = c_int
    PdfixLib.PdfDocMakeAccessible.argtypes = [c_void_p, POINTER(zz_PdfAccessibleParams), c_int, c_void_p]
    PdfixLib.PdfDocGetRootObject.restype = c_void_p
    PdfixLib.PdfDocGetRootObject.argtypes = [c_void_p]
    PdfixLib.PdfDocGetInfoObject.restype = c_void_p
    PdfixLib.PdfDocGetInfoObject.argtypes = [c_void_p]
    PdfixLib.PdfDocGetStructTree.restype = c_void_p
    PdfixLib.PdfDocGetStructTree.argtypes = [c_void_p]
    PdfixLib.PdfDocTemplatePreflightDoc.restype = c_int
    PdfixLib.PdfDocTemplatePreflightDoc.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfDocTemplateLoadFromStream.restype = c_int
    PdfixLib.PdfDocTemplateLoadFromStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocTemplateSaveToStream.restype = c_int
    PdfixLib.PdfDocTemplateSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocTemplateSetDefaults.restype = c_int
    PdfixLib.PdfDocTemplateSetDefaults.argtypes = [c_void_p]
    PdfixLib.PdfAlternateGetSubtype.restype = c_int
    PdfixLib.PdfAlternateGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfAlternateGetName.restype = c_int
    PdfixLib.PdfAlternateGetName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateGetDescription.restype = c_int
    PdfixLib.PdfAlternateGetDescription.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateGetFileName.restype = c_int
    PdfixLib.PdfAlternateGetFileName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateSaveContent.restype = c_int
    PdfixLib.PdfAlternateSaveContent.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfAlternateRelease.restype = c_int
    PdfixLib.PdfAlternateRelease.argtypes = [c_void_p]
    PdfixLib.PdfHtmlAlternateSaveResource.restype = c_int
    PdfixLib.PdfHtmlAlternateSaveResource.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfFontGetFontName.restype = c_int
    PdfixLib.PdfFontGetFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetFaceName.restype = c_int
    PdfixLib.PdfFontGetFaceName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetFontState.restype = c_int
    PdfixLib.PdfFontGetFontState.argtypes = [c_void_p, POINTER(zz_PdfFontState)]
    PdfixLib.PdfFontGetSystemFontName.restype = c_int
    PdfixLib.PdfFontGetSystemFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetSystemFontCharset.restype = c_int
    PdfixLib.PdfFontGetSystemFontCharset.argtypes = [c_void_p]
    PdfixLib.PdfFontGetSystemFontBold.restype = c_int
    PdfixLib.PdfFontGetSystemFontBold.argtypes = [c_void_p]
    PdfixLib.PdfFontGetSystemFontItalic.restype = c_int
    PdfixLib.PdfFontGetSystemFontItalic.argtypes = [c_void_p]
    PdfixLib.PdfFontSaveToStream.restype = c_int
    PdfixLib.PdfFontSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfFormFieldGetType.restype = c_int
    PdfixLib.PdfFormFieldGetType.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetFlags.restype = c_int
    PdfixLib.PdfFormFieldGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldSetFlags.restype = c_int
    PdfixLib.PdfFormFieldSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfFormFieldGetValue.restype = c_int
    PdfixLib.PdfFormFieldGetValue.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldSetValue.restype = c_int
    PdfixLib.PdfFormFieldSetValue.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfFormFieldGetDefaultValue.restype = c_int
    PdfixLib.PdfFormFieldGetDefaultValue.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetFullName.restype = c_int
    PdfixLib.PdfFormFieldGetFullName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetTooltip.restype = c_int
    PdfixLib.PdfFormFieldGetTooltip.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetOptionCount.restype = c_int
    PdfixLib.PdfFormFieldGetOptionCount.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetOptionValue.restype = c_int
    PdfixLib.PdfFormFieldGetOptionValue.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetOptionCaption.restype = c_int
    PdfixLib.PdfFormFieldGetOptionCaption.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetAction.restype = c_void_p
    PdfixLib.PdfFormFieldGetAction.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetAAction.restype = c_void_p
    PdfixLib.PdfFormFieldGetAAction.argtypes = [c_void_p, c_int]
    PdfixLib.PdfFormFieldGetMaxLength.restype = c_int
    PdfixLib.PdfFormFieldGetMaxLength.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetWidgetExportValue.restype = c_int
    PdfixLib.PdfFormFieldGetWidgetExportValue.argtypes = [c_void_p, c_void_p, c_wchar_p, c_int]
    PdfixLib.PsImageDestroy.restype = c_int
    PdfixLib.PsImageDestroy.argtypes = [c_void_p]
    PdfixLib.PsImageSave.restype = c_int
    PdfixLib.PsImageSave.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfImageParams)]
    PdfixLib.PsImageSaveRect.restype = c_int
    PdfixLib.PsImageSaveRect.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfImageParams), POINTER(zz_PdfDevRect)]
    PdfixLib.PsImageSaveToStream.restype = c_int
    PdfixLib.PsImageSaveToStream.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfImageParams)]
    PdfixLib.PsImageSaveRectToStream.restype = c_int
    PdfixLib.PsImageSaveRectToStream.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfImageParams), POINTER(zz_PdfDevRect)]
    PdfixLib.PsImageGetPointColor.restype = c_int
    PdfixLib.PsImageGetPointColor.argtypes = [c_void_p, POINTER(zz_PdfDevPoint), POINTER(zz_PdfRGB)]
    PdfixLib.PdfPageGetCropBox.restype = c_int
    PdfixLib.PdfPageGetCropBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetMediaBox.restype = c_int
    PdfixLib.PdfPageGetMediaBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetRotate.restype = c_int
    PdfixLib.PdfPageGetRotate.argtypes = [c_void_p]
    PdfixLib.PdfPageGetDefaultMatrix.restype = c_int
    PdfixLib.PdfPageGetDefaultMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfPageGetNumber.restype = c_int
    PdfixLib.PdfPageGetNumber.argtypes = [c_void_p]
    PdfixLib.PdfPageAcquirePageMap.restype = c_void_p
    PdfixLib.PdfPageAcquirePageMap.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfPageReleasePageMap.restype = c_int
    PdfixLib.PdfPageReleasePageMap.argtypes = [c_void_p]
    PdfixLib.PdfPageAcquirePageView.restype = c_void_p
    PdfixLib.PdfPageAcquirePageView.argtypes = [c_void_p, c_double, c_int]
    PdfixLib.PdfPageReleasePageView.restype = c_int
    PdfixLib.PdfPageReleasePageView.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfPageGetNumAnnots.restype = c_int
    PdfixLib.PdfPageGetNumAnnots.argtypes = [c_void_p]
    PdfixLib.PdfPageGetAnnot.restype = c_void_p
    PdfixLib.PdfPageGetAnnot.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageRemoveAnnot.restype = c_int
    PdfixLib.PdfPageRemoveAnnot.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfPageAddTextAnnot.restype = c_void_p
    PdfixLib.PdfPageAddTextAnnot.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageAddLinkAnnot.restype = c_void_p
    PdfixLib.PdfPageAddLinkAnnot.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageAddTextMarkupAnnot.restype = c_void_p
    PdfixLib.PdfPageAddTextMarkupAnnot.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect), c_int]
    PdfixLib.PdfPageGetNumAnnotsAtPoint.restype = c_int
    PdfixLib.PdfPageGetNumAnnotsAtPoint.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdfPageGetAnnotAtPoint.restype = c_void_p
    PdfixLib.PdfPageGetAnnotAtPoint.argtypes = [c_void_p, POINTER(zz_PdfPoint), c_int]
    PdfixLib.PdfPageGetNumAnnotsAtRect.restype = c_int
    PdfixLib.PdfPageGetNumAnnotsAtRect.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetAnnotAtRect.restype = c_void_p
    PdfixLib.PdfPageGetAnnotAtRect.argtypes = [c_void_p, POINTER(zz_PdfRect), c_int]
    PdfixLib.PdfPageDrawContent.restype = c_int
    PdfixLib.PdfPageDrawContent.argtypes = [c_void_p, POINTER(zz_PdfPageRenderParams), c_int, c_void_p]
    PdfixLib.PdfPageGetNumMcidPageObjects.restype = c_int
    PdfixLib.PdfPageGetNumMcidPageObjects.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageGetMcidPageObject.restype = c_void_p
    PdfixLib.PdfPageGetMcidPageObject.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdePageMapGetElement.restype = c_void_p
    PdfixLib.PdePageMapGetElement.argtypes = [c_void_p]
    PdfixLib.PdePageMapGetWhitespace.restype = c_int
    PdfixLib.PdePageMapGetWhitespace.argtypes = [c_void_p, POINTER(zz_PdfWhitespaceParams), c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdePageMapGetBBox.restype = c_int
    PdfixLib.PdePageMapGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageViewGetDeviceWidth.restype = c_int
    PdfixLib.PdfPageViewGetDeviceWidth.argtypes = [c_void_p]
    PdfixLib.PdfPageViewGetDeviceHeight.restype = c_int
    PdfixLib.PdfPageViewGetDeviceHeight.argtypes = [c_void_p]
    PdfixLib.PdfPageViewGetDeviceMatrix.restype = c_int
    PdfixLib.PdfPageViewGetDeviceMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfPageViewRectToDevice.restype = c_int
    PdfixLib.PdfPageViewRectToDevice.argtypes = [c_void_p, POINTER(zz_PdfRect), POINTER(zz_PdfDevRect)]
    PdfixLib.PdfPageViewPointToDevice.restype = c_int
    PdfixLib.PdfPageViewPointToDevice.argtypes = [c_void_p, POINTER(zz_PdfPoint), POINTER(zz_PdfDevPoint)]
    PdfixLib.PdfBookmarkGetTitle.restype = c_int
    PdfixLib.PdfBookmarkGetTitle.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfBookmarkGetAppearance.restype = c_int
    PdfixLib.PdfBookmarkGetAppearance.argtypes = [c_void_p, POINTER(zz_PdfBookmarkAppearance)]
    PdfixLib.PdfBookmarkGetAction.restype = c_void_p
    PdfixLib.PdfBookmarkGetAction.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetNumChildren.restype = c_int
    PdfixLib.PdfBookmarkGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetChild.restype = c_void_p
    PdfixLib.PdfBookmarkGetChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdfBookmarkGetParent.restype = c_void_p
    PdfixLib.PdfBookmarkGetParent.argtypes = [c_void_p]
    PdfixLib.PsRegexDestroy.restype = c_int
    PdfixLib.PsRegexDestroy.argtypes = [c_void_p]
    PdfixLib.PsRegexSetPattern.restype = c_int
    PdfixLib.PsRegexSetPattern.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsRegexSearch.restype = c_int
    PdfixLib.PsRegexSearch.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsRegexGetText.restype = c_int
    PdfixLib.PsRegexGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsRegexGetPosition.restype = c_int
    PdfixLib.PsRegexGetPosition.argtypes = [c_void_p]
    PdfixLib.PsRegexGetLength.restype = c_int
    PdfixLib.PsRegexGetLength.argtypes = [c_void_p]
    PdfixLib.PsRegexGetNumMatches.restype = c_int
    PdfixLib.PsRegexGetNumMatches.argtypes = [c_void_p]
    PdfixLib.PsRegexGetMatchText.restype = c_int
    PdfixLib.PsRegexGetMatchText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PsStreamDestroy.restype = c_int
    PdfixLib.PsStreamDestroy.argtypes = [c_void_p]
    PdfixLib.PsStreamIsEof.restype = c_int
    PdfixLib.PsStreamIsEof.argtypes = [c_void_p]
    PdfixLib.PsStreamGetSize.restype = c_int
    PdfixLib.PsStreamGetSize.argtypes = [c_void_p]
    PdfixLib.PsStreamRead.restype = c_int
    PdfixLib.PsStreamRead.argtypes = [c_void_p, c_int, POINTER(c_ubyte), c_int]
    PdfixLib.PsStreamWrite.restype = c_int
    PdfixLib.PsStreamWrite.argtypes = [c_void_p, c_int, POINTER(c_ubyte), c_int]
    PdfixLib.PsStreamGetPos.restype = c_int
    PdfixLib.PsStreamGetPos.argtypes = [c_void_p]
    PdfixLib.PsStreamFlush.restype = c_int
    PdfixLib.PsStreamFlush.argtypes = [c_void_p]
    PdfixLib.PsStreamGetStream.restype = c_void_p
    PdfixLib.PsStreamGetStream.argtypes = [c_void_p]
    PdfixLib.PsStreamGetType.restype = c_int
    PdfixLib.PsStreamGetType.argtypes = [c_void_p]
    PdfixLib.PsMemoryStreamResize.restype = c_int
    PdfixLib.PsMemoryStreamResize.argtypes = [c_void_p, c_int]
    PdfixLib.PsProcStreamSetReadProc.restype = c_int
    PdfixLib.PsProcStreamSetReadProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsProcStreamSetWriteProc.restype = c_int
    PdfixLib.PsProcStreamSetWriteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsProcStreamSetDestroyProc.restype = c_int
    PdfixLib.PsProcStreamSetDestroyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsProcStreamSetGetSizeProc.restype = c_int
    PdfixLib.PsProcStreamSetGetSizeProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetType.restype = c_int
    PdfixLib.PdsStructElementGetType.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetActualText.restype = c_int
    PdfixLib.PdsStructElementGetActualText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetAlt.restype = c_int
    PdfixLib.PdsStructElementGetAlt.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetAbbreviation.restype = c_int
    PdfixLib.PdsStructElementGetAbbreviation.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetPageNumber.restype = c_int
    PdfixLib.PdsStructElementGetPageNumber.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetAttrObject.restype = c_void_p
    PdfixLib.PdsStructElementGetAttrObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetElementObject.restype = c_void_p
    PdfixLib.PdsStructElementGetElementObject.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetKidObject.restype = c_void_p
    PdfixLib.PdsStructElementGetKidObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetKidType.restype = c_int
    PdfixLib.PdsStructElementGetKidType.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetKidPageNumber.restype = c_int
    PdfixLib.PdsStructElementGetKidPageNumber.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetKidMcid.restype = c_int
    PdfixLib.PdsStructElementGetKidMcid.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetNumAttrObjects.restype = c_int
    PdfixLib.PdsStructElementGetNumAttrObjects.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetNumKids.restype = c_int
    PdfixLib.PdsStructElementGetNumKids.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetParentObject.restype = c_void_p
    PdfixLib.PdsStructElementGetParentObject.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetTitle.restype = c_int
    PdfixLib.PdsStructElementGetTitle.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetID.restype = c_int
    PdfixLib.PdsStructElementGetID.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsClassMapGetAttrObject.restype = c_void_p
    PdfixLib.PdsClassMapGetAttrObject.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsClassMapGetNumAttrObjects.restype = c_int
    PdfixLib.PdsClassMapGetNumAttrObjects.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsRoleMapDoesMap.restype = c_int
    PdfixLib.PdsRoleMapDoesMap.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdsRoleMapGetDirectMap.restype = c_int
    PdfixLib.PdsRoleMapGetDirectMap.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdsStructTreeGetClassMap.restype = c_void_p
    PdfixLib.PdsStructTreeGetClassMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetKidObject.restype = c_void_p
    PdfixLib.PdsStructTreeGetKidObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructTreeGetNumKids.restype = c_int
    PdfixLib.PdsStructTreeGetNumKids.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetRoleMap.restype = c_void_p
    PdfixLib.PdsStructTreeGetRoleMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeAcquireStructElement.restype = c_void_p
    PdfixLib.PdsStructTreeAcquireStructElement.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdsStructTreeReleaseStructElement.restype = c_int
    PdfixLib.PdsStructTreeReleaseStructElement.argtypes = [c_void_p, c_void_p]
    PdfixLib.PsMetadataSaveToStream.restype = c_int
    PdfixLib.PsMetadataSaveToStream.argtypes = [c_void_p, c_void_p]
    PdfixLib.PsMetadataLoadFromStream.restype = c_int
    PdfixLib.PsMetadataLoadFromStream.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfixDestroy.restype = c_int
    PdfixLib.PdfixDestroy.argtypes = [c_void_p]
    PdfixLib.PdfixAuthorize.restype = c_int
    PdfixLib.PdfixAuthorize.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfixIsAuthorized.restype = c_int
    PdfixLib.PdfixIsAuthorized.argtypes = [c_void_p]
    PdfixLib.PdfixIsAuthorizedPlatform.restype = c_int
    PdfixLib.PdfixIsAuthorizedPlatform.argtypes = [c_void_p, c_int]
    PdfixLib.PdfixIsAuthorizedOption.restype = c_int
    PdfixLib.PdfixIsAuthorizedOption.argtypes = [c_void_p, c_int]
    PdfixLib.PdfixGetErrorType.restype = c_int
    PdfixLib.PdfixGetErrorType.argtypes = [c_void_p]
    PdfixLib.PdfixGetError.restype = c_char_p
    PdfixLib.PdfixGetError.argtypes = [c_void_p]
    PdfixLib.PdfixSetError.restype = c_int
    PdfixLib.PdfixSetError.argtypes = [c_void_p, c_int, c_char_p]
    PdfixLib.PdfixGetVersionMajor.restype = c_int
    PdfixLib.PdfixGetVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfixGetVersionMinor.restype = c_int
    PdfixLib.PdfixGetVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfixGetVersionPatch.restype = c_int
    PdfixLib.PdfixGetVersionPatch.argtypes = [c_void_p]
    PdfixLib.PdfixOpenDoc.restype = c_void_p
    PdfixLib.PdfixOpenDoc.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfixOpenDocFromStream.restype = c_void_p
    PdfixLib.PdfixOpenDocFromStream.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfixCreateDigSig.restype = c_void_p
    PdfixLib.PdfixCreateDigSig.argtypes = [c_void_p]
    PdfixLib.PdfixCreateCustomDigSig.restype = c_void_p
    PdfixLib.PdfixCreateCustomDigSig.argtypes = [c_void_p]
    PdfixLib.PdfixCreateRegex.restype = c_void_p
    PdfixLib.PdfixCreateRegex.argtypes = [c_void_p]
    PdfixLib.PdfixCreateFileStream.restype = c_void_p
    PdfixLib.PdfixCreateFileStream.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfixCreateMemStream.restype = c_void_p
    PdfixLib.PdfixCreateMemStream.argtypes = [c_void_p]
    PdfixLib.PdfixCreateCustomStream.restype = c_void_p
    PdfixLib.PdfixCreateCustomStream.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfixRegisterEvent.restype = c_int
    PdfixLib.PdfixRegisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfixUnregisterEvent.restype = c_int
    PdfixLib.PdfixUnregisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfixSetRegex.restype = c_int
    PdfixLib.PdfixSetRegex.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdfixCreateImage.restype = c_void_p
    PdfixLib.PdfixCreateImage.argtypes = [c_void_p, c_int, c_int, c_int]
    PdfixLib.PdfixPluginDestroy.restype = c_int
    PdfixLib.PdfixPluginDestroy.argtypes = [c_void_p]
    PdfixLib.PdfixPluginInitialize.restype = c_int
    PdfixLib.PdfixPluginInitialize.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfixPluginGetVersionMajor.restype = c_int
    PdfixLib.PdfixPluginGetVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetVersionMinor.restype = c_int
    PdfixLib.PdfixPluginGetVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetVersionPatch.restype = c_int
    PdfixLib.PdfixPluginGetVersionPatch.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetPdfix.restype = c_void_p
    PdfixLib.PdfixPluginGetPdfix.argtypes = [c_void_p]
    PdfixLib.GetPdfix.restype = c_void_p

def Pdfix_destroy():
    global PdfixLib
    del PdfixLib
    PdfixLib = None

