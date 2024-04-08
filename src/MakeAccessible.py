# MakeAccessible.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk.Pdfix import *

pdfix  = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# preflight document for better tagging structure (optional)
tmpl = doc.GetTemplate()
for i in range(0, doc.GetNumPages()):
    tmpl.AddPage(i)
tmpl.Update()

# set the document title and language
title = "Document title"
lang = "en-US"

# run make accessibile
# single MakeAccessible method has been deprecated. You should call individual methods fixing
# problems with document acessibility. The set of methods in this example should be customized 
# for the needs of the document

# clear document structure
doc.RemoveTags()

# embed fonts
doc.EmbedFonts(True)

# add missing unicode
doc.AddFontMissingUnicode()

# prepare template for document preflight
tmpl = doc.GetTemplate()

for i in range(doc.GetNumPages()):
    page = doc.AcquirePage(i)

    # flatten form XObjects 
    page.FlattenFormXObjects()

    # add page to template process
    tmpl.AddPage(i)

    page.Release()

# run preflight on the document template
tmpl.Update()

# add tags
tagParams = PdfTagsParams()
doc.AddTags(tagParams)

# set language
doc.SetLang("en")

# set doc ua part
doc.SetPdfStandard(kPdfStandardPdfUA, "1")

# create bookmarkd
doc.CreateBookmarks()

# other accessibility fixes are available using commands. see user guide for reference

if not doc.Save(outputPath + "/MakeAccessible.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
