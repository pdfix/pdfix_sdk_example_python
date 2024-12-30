# AddTags.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath, stream_to_data
from pdfixsdk import *

pdfix = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# load template configuration from JSON file
tmpl = doc.GetTemplate()
if not tmpl:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

preflight = True
if preflight:
    # Auto-generate the template configuration using document Preflight
    # Add reference pages into preflight processor. It's usefull to pick only certain 
    # pages from a large documents. If no pages are added, all proges are processed
    # in the Update method
    for i in range(doc.GetNumPages()):
        tmpl.AddPage(i)
    tmpl.Update()

    # to save generated template into a JSON
    memStm = pdfix.CreateMemStream()
    tmpl.SaveToStream(memStm, kDataFormatJson, kSaveFull)
    templateBytes = bytearray(stream_to_data(memStm))
    memStm.Destroy()

else:
    # load the template from a pre-created JSON
    tmplStm = pdfix.CreateFileStream(inputPath + "/template.json", kPsReadOnly)
    if not tmpl.LoadFromStream(tmplStm, kDataFormatJson):
        raise Exception('Unable to open pdf : ' + pdfix.GetError())

tagsParams = PdfTagsParams()
if not doc.AddTags(tagsParams):
    raise Exception(pdfix.GetError())

if not doc.Save(outputPath + "/AddTags.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
