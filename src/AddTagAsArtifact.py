# AddTagAsArtifact.py

# import utils to load required shared libraries
from Utils import inputPath, outputPath
from pdfixsdk import *

# find any non-tagged objects in the page content and mark them as artifact
def MarkUntaggedObjectsAsArtifact(page:PdfPage):
    pDoc = page.GetDoc()
    content = page.GetContent()
    for i in range(content.GetNumObjects()):
        page_obj = content.GetObject(i)
        content_mark = page_obj.GetContentMark()
        if content_mark.GetTagArtifact() is not None and (content_mark.GetTagMcid() == -1):
            artifact_dict = pDoc.CreateDictObject(False)
            artifact_dict.Put("Type", pDoc.CreateNameObject(False, "Pagination"))
            artifact_dict.Put("Subtype", pDoc.CreateNameObject(False, "Footer"))
            content_mark.AddTag("Artifact", artifact_dict, False)
    page.SetContent()    

def RemoveParagraph(struct_elem:PdsStructElement):
    # remove last 2 P struct elements from struct tree
    count = 0
    for i in range(struct_elem.GetNumChildren()-1, -1):
        if struct_elem.GetChildType(i) == kPdsStructChildElement:
            kid_obj = struct_elem.GetChildObject(i)
            kid_elem = struct_elem.GetStructTree().GetStructElementFromObject(kid_obj)
            kid_type = kid_elem.GetType(True)
            if kid_type == "P":
                for j in range(kid_elem.GetNumChildren()-1, -1):
                    if not kid_elem.RemoveChild(j):
                        raise Exception()
            elif kid_type == "Figure":
                # remove figure if does not contain an alt text
                alt_len = kid_elem.GetAlt(None, 0)
                if alt_len == 0:
                    for j in range(kid_elem.GetNumChildren()-1, -1):
                        if not kid_elem.RemoveChild(j):
                            raise Exception()
            else:
                RemoveParagraph(kid_elem)
            # remove this element if it has no kids
            if kid_elem.GetNumChildren() == 0:
                struct_elem.RemoveChild(i)
        # remove only 2 paragraphs in this sample
        count += 1
        if count >= 2 : break
    


pdfix = GetPdfix()
if pdfix is None:
    raise Exception('Pdfix Initialization fail')

doc = pdfix.OpenDoc(inputPath + "/test.pdf", "")
if doc is None:
    raise Exception('Unable to open pdf : ' + pdfix.GetError())

# cleanup any previous structure tree
if not doc.RemoveTags():
    raise Exception(pdfix.GetError())

# autotag document first
tagsParams = PdfTagsParams()
if not doc.AddTags(tagsParams):
    raise Exception(pdfix.GetError())

# get the struct tree
struct_tree = doc.GetStructTree()
if struct_tree is None:
    raise Exception()

# tag text on the bottom of the page as artifact
for i in range(struct_tree.GetNumChildren()):
    kid_obj = struct_tree.GetChildObject(i)
    kid_elem = struct_tree.GetStructElementFromObject(kid_obj)
    RemoveParagraph(kid_elem)

# the struct tree was updates, save page content on each page to apply changes
for i in range(doc.GetNumPages()):
    page = doc.AcquirePage(i)
    MarkUntaggedObjectsAsArtifact(page)
    page.Release()

# save document
if not doc.Save(outputPath + "/AddTagAsArtifact.pdf", kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()