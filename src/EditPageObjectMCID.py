from pdfixsdk import GetPdfix, kSaveFull

from Utils import input_path, output_path

pdfix = GetPdfix()
if pdfix is None:
    raise RuntimeError("Pdfix initialization failed")

# open the document
doc = pdfix.OpenDoc(input_path.joinpath("tagged.pdf").as_posix(), "")
if doc is None:
    raise RuntimeError(f"Unable to open PDF: {pdfix.GetError()}")

# load first page cotnent and the first page object
page = doc.AcquirePage(0)
if page is None:
    raise RuntimeError(f"Unable to acquire page: {pdfix.GetError()}")

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
if not doc.Save(output_path.joinpath("PageObjectMCID.pdf").as_posix(), kSaveFull):
    raise RuntimeError(pdfix.GetError())

doc.Close()
# pdfix.Destroy() not used: script exits when done. Call Destroy() only if the process
# keeps running but must release PDFix (see Initialization.py, License.py).
