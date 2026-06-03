import os
from pdfixsdk import *
from Utils import inputPath, outputPath


pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError('Pdfix initialization failed')

# open the document
doc = pdfix.OpenDoc(f"{inputPath}/tagged.pdf", "")
if doc is None:
    raise RuntimeError(f'Unable to open PDF: {pdfix.GetError()}')

# load first page cotnent and the first page object
page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f'Unable to acquire page: {pdfix.GetError()}')

content = page.GetContent()
pageObject = content.GetObject(0)

# get the page object MCID
mcid = pageObject.GetMcid()

# load the page object content mark and
# update the tag properties dictionary with new MCID
contentMark = pageObject.GetContentMark()
tagMcid = contentMark.GetTagMcid()
tagDict = contentMark.GetTagObject(tagMcid)
tagDict.PutNumber("MCID", mcid + 1)
contentMark.SetTagObject(tagMcid, tagDict, False)

# release page resources
page.Release()

# save and close document
if not doc.Save(f"{outputPath}/PageObjectMCID.pdf", kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
