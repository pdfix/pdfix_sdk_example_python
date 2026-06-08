# AddTags.py

from pdfixsdk import *

from Utils import input_path, output_path, stream_to_data

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

doc = pdfix.OpenDoc(input_path.joinpath("test.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# load template configuration from JSON file
tmpl = doc.GetTemplate()
if not tmpl:
    raise RuntimeError(f"Unable to get document template: {pdfix.GetError()}")

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
    if memStm is None:
        raise RuntimeError(pdfix.GetError())

    tmpl.SaveToStream(memStm, kDataFormatJson, kSaveFull)
    templateBytes = bytearray(stream_to_data(memStm))
    memStm.Destroy()

else:
    # load the template from a pre-created JSON
    tmplStm = pdfix.CreateFileStream(
        input_path.joinpath("template.json").as_posix(), kPsReadOnly
    )
    if tmplStm is None:
        raise RuntimeError(pdfix.GetError())

    if not tmpl.LoadFromStream(tmplStm, kDataFormatJson):
        raise RuntimeError(f"Unable to load template: {pdfix.GetError()}")

    tmplStm.Destroy()

tagsParams = PdfTagsParams()
if not doc.AddTags(tagsParams):
    raise RuntimeError(pdfix.GetError())

if not doc.Save(output_path.joinpath("AddTags.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
