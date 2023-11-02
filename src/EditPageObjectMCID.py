import os
from pdfixsdk.Pdfix import *
from Utils import inputPath, outputPath


pdfix = GetPdfix()

# open the document
doc = pdfix.OpenDoc(inputPath + "/tagged.pdf", "")

# load first page cotnent and the first page object
page = doc.AcquirePage(0)
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
doc.Save(outputPath + "/PageObjectMCID.pdf", kSaveFull)
doc.Close()
