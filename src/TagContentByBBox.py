# TagContentByBBox.py
# Tag one region of a page as a paragraph and another as a table.
# The caller supplies bounding boxes only. Objects outside a box are
# excluded for that pass so AddTags writes just that region.
#
# Input PDF (not resources/test.pdf): resources/tag_content_by_bbox.pdf
# Table and paragraph rects below come from that file's structure-element /BBox attributes.
# PDF user space: origin is the bottom-left, so top is greater than bottom.

from Utils import input_path, output_path
from pdfixsdk import *

INPUT_PDF = input_path.joinpath("tag_content_by_bbox.pdf").as_posix()
PAGE_NUM = 0

# Objects outside the region are skipped by CreateElements.
EXCLUDE = kStateNoRender | kStateExclude


def pdf_rect(left, bottom, right, top):
    rect = PdfRect()
    rect.left = left
    rect.bottom = bottom
    rect.right = right
    rect.top = top
    return rect


def rects_intersect(a, b):
    return (a.left < b.right) and (b.left < a.right) and (a.bottom < b.top) and (b.bottom < a.top)


# Paragraph to tag. text_style 0 keeps a plain paragraph.
# Set text_style to kTextH1 (or kTextH2..) to tag the same box as a heading.
paragraph = {
    "bbox": pdf_rect(50.72, 696.31, 400.04, 734.62),
    "tag": "P",
    "text_style": 0,
}


def cell(row, col, left, bottom, right, top, header_scope=kCellScopeNone,
         row_span=1, col_span=1, tag_id="", headers=None):
    """One table cell. Edit bbox, header_scope, and spans in the list below.

    header_scope:
      kCellScopeNone
      kCellScopeCol                 column header
      kCellScopeRow                 row header
      kCellScopeRow | kCellScopeCol both (corner)
    row_span / col_span greater than 1 belong on the origin cell.
    A covered slot still needs its own record with span 1, so the list
    length stays rows * cols.
    tag_id is the structure id of a header cell.
    headers lists those ids on a data cell. link_table_headers applies them
    with AddAssociatedHeader after the table exists.
    """
    return {
        "row": row,
        "col": col,
        "bbox": pdf_rect(left, bottom, right, top),
        "header_scope": header_scope,
        "row_span": row_span,
        "col_span": col_span,
        "tag_id": tag_id,
        "headers": list(headers or []),
    }


# 6x5 price table from resources/tag_content_by_bbox.pdf.
# Rects are the /BBox layout attributes on the Table, TH, and TD elements
# (left, bottom, right, top). Row-major: index = row * cols + col.
# Row 0 is tagged TH (column headers). Column 0 of the other rows is TH
# (row headers). The remaining cells are TD. Spans are 1.
table = {
    "bbox": pdf_rect(55, 458.78, 570, 667.89),
    "rows": 6,
    "cols": 5,
    "cells": [
        cell(0, 0, 68, 644.78, 89.81, 652.05, kCellScopeCol, tag_id="hc0"),
        cell(0, 1, 163.48, 644.78, 185.14, 652.17, kCellScopeCol, tag_id="hc1"),
        cell(0, 2, 268.36, 644.77, 295.37, 652.17, kCellScopeCol, tag_id="hc2"),
        cell(0, 3, 373.47, 642.93, 408.13, 652.17, kCellScopeCol, tag_id="hc3"),
        cell(0, 4, 478.21, 644.78, 519.02, 652.05, kCellScopeCol, tag_id="hc4"),
        cell(1, 0, 68.25, 606.78, 89.94, 614.08, kCellScopeRow, tag_id="hr1"),
        cell(1, 1, 164.09, 606.78, 179.2, 614.08, headers=["hc1", "hr1"]),
        cell(1, 2, 269.09, 606.78, 284.2, 614.08, headers=["hc2", "hr1"]),
        cell(1, 3, 374.09, 606.78, 389.2, 614.08, headers=["hc3", "hr1"]),
        cell(1, 4, 479.09, 606.78, 494.2, 614.08, headers=["hc4", "hr1"]),
        cell(2, 0, 68.25, 569.78, 89.75, 577.08, kCellScopeRow, tag_id="hr2"),
        cell(2, 1, 164.09, 569.78, 179.28, 577.08, headers=["hc1", "hr2"]),
        cell(2, 2, 269.09, 569.77, 284.28, 577.08, headers=["hc2", "hr2"]),
        cell(2, 3, 374.09, 569.78, 389.2, 577.08, headers=["hc3", "hr2"]),
        cell(2, 4, 479.09, 569.78, 494.2, 577.08, headers=["hc4", "hr2"]),
        cell(3, 0, 68.25, 532.78, 89.94, 540.08, kCellScopeRow, tag_id="hr3"),
        cell(3, 1, 163.29, 532.78, 179.2, 540.08, headers=["hc1", "hr3"]),
        cell(3, 2, 269.09, 532.78, 284.28, 540.08, headers=["hc2", "hr3"]),
        cell(3, 3, 374.09, 532.78, 389.28, 540.08, headers=["hc3", "hr3"]),
        cell(3, 4, 479.09, 532.78, 494.28, 540.08, headers=["hc4", "hr3"]),
        cell(4, 0, 68.25, 495.78, 89.75, 503.08, kCellScopeRow, tag_id="hr4"),
        cell(4, 1, 163.42, 495.77, 179.2, 503.08, headers=["hc1", "hr4"]),
        cell(4, 2, 269.09, 495.78, 284.28, 503.08, headers=["hc2", "hr4"]),
        cell(4, 3, 374.09, 495.78, 389.28, 503.08, headers=["hc3", "hr4"]),
        cell(4, 4, 479.09, 495.77, 494.2, 503.08, headers=["hc4", "hr4"]),
        cell(5, 0, 68.25, 458.78, 89.94, 466.08, kCellScopeRow, tag_id="hr5"),
        cell(5, 1, 163.42, 458.78, 179.2, 466.08, headers=["hc1", "hr5"]),
        cell(5, 2, 268.29, 458.78, 284.28, 466.08, headers=["hc2", "hr5"]),
        cell(5, 3, 373.29, 458.78, 389.28, 466.08, headers=["hc3", "hr5"]),
        cell(5, 4, 479.09, 458.78, 494.2, 466.08, headers=["hc4", "hr5"]),
    ],
}


def clip_content(content, bbox):
    """Mark objects inside bbox as default and the rest as excluded.

    A form stays included when any nested object hits the bbox, so the
    engine still walks that form and honors the flags on its children.
    Returns True when something in this content hits the bbox.
    """
    if content is None:
        return False
    any_hit = False
    for i in range(content.GetNumObjects()):
        obj = content.GetObject(i)
        if obj is None:
            continue
        if obj.GetObjectType() == kPdsPageForm:
            form = PdsForm(obj.obj)
            hit = clip_content(form.GetContent(), bbox)
        else:
            hit = rects_intersect(obj.GetBBox(), bbox)
        obj.SetStateFlags(kStateDefault if hit else EXCLUDE)
        any_hit = any_hit or hit
    return any_hit


def reset_content(content):
    if content is None:
        return
    for i in range(content.GetNumObjects()):
        obj = content.GetObject(i)
        if obj is None:
            continue
        if obj.GetObjectType() == kPdsPageForm:
            reset_content(PdsForm(obj.obj).GetContent())
        obj.SetStateFlags(kStateDefault)


def clip_annots(page, bbox):
    for i in range(page.GetNumAnnots()):
        annot = page.GetAnnot(i)
        if annot is None:
            continue
        hit = rects_intersect(annot.GetBBox(), bbox)
        annot.SetStateFlags(kStateDefault if hit else EXCLUDE)


def reset_annots(page):
    for i in range(page.GetNumAnnots()):
        annot = page.GetAnnot(i)
        if annot is not None:
            annot.SetStateFlags(kStateDefault)


def tag_region(page, parent, bbox, build_element):
    """Exclude content outside bbox, build one predefined element, write tags.

    parent is the structure element that receives the new tag as a child.
    Pass any existing PdsStructElement here instead of the Div this example
    creates, if the new tag should land somewhere else.
    Flags are restored even when tagging fails.
    """
    content = page.GetContent()
    clip_content(content, bbox)
    clip_annots(page, bbox)
    page_map = None
    try:
        page_map = page.AcquirePageMap()
        if page_map is None:
            raise Exception("Acquire PageMap fail: " + pdfix.GetError())
        if page_map.HasElements() and not page_map.RemoveElements():
            raise Exception(pdfix.GetError())

        build_element(page_map)

        if not page_map.CreateElements():
            raise Exception(pdfix.GetError())

        # standard_attrs writes the usual structure attributes.
        # headings 0 keeps the tag taken from the element, not from font size.
        params = PdfTagsParams()
        params.standard_attrs = 1
        params.headings = 0
        if not page_map.AddTags(parent, False, params):
            raise Exception(pdfix.GetError())
    finally:
        if page_map is not None:
            page_map.Release()
        reset_content(page.GetContent())
        reset_annots(page)


def build_paragraph(page_map):
    element = page_map.CreateElement(kPdeText, None)
    if element is None:
        raise Exception(pdfix.GetError())
    element.SetBBox(paragraph["bbox"])
    # Keep this block as one paragraph: do not join, split, or grow it.
    element.SetFlags(kElemNoJoin | kElemNoSplit | kElemNoExpand)
    element.SetTag(paragraph["tag"])
    if paragraph["text_style"]:
        PdeText(element.obj).SetTextStyle(paragraph["text_style"])


def build_table(page_map):
    rows = table["rows"]
    cols = table["cols"]
    cells = table["cells"]
    if len(cells) != rows * cols:
        raise Exception("Table needs one cell record per grid slot (rows * cols)")

    element = page_map.CreateElement(kPdeTable, None)
    if element is None:
        raise Exception(pdfix.GetError())
    pde_table = PdeTable(element.obj)
    pde_table.SetBBox(table["bbox"])
    pde_table.SetNumRows(rows)
    pde_table.SetNumCols(cols)
    # kElemInitial marks the grid as predefined. Every slot must have a cell.
    pde_table.SetFlags(kElemInitial)
    pde_table.SetTag("Table")

    for rec in cells:
        cell_elem = page_map.CreateElement(kPdeCell, pde_table)
        if cell_elem is None:
            raise Exception(pdfix.GetError())
        pde_cell = PdeCell(cell_elem.obj)
        pde_cell.SetRowNum(rec["row"])
        pde_cell.SetColNum(rec["col"])
        pde_cell.SetBBox(rec["bbox"])
        pde_cell.SetRowSpan(rec["row_span"])
        pde_cell.SetColSpan(rec["col_span"])
        if rec["header_scope"] != kCellScopeNone:
            pde_cell.SetHeader(True)
            pde_cell.SetHeaderScope(rec["header_scope"])
        if rec["tag_id"]:
            pde_cell.SetTagId(rec["tag_id"])


def struct_kids(parent):
    tree = parent.GetStructTree()
    kids = []
    for i in range(parent.GetNumChildren()):
        if parent.GetChildType(i) != kPdsStructChildElement:
            continue
        kid = tree.GetStructElementFromObject(parent.GetChildObject(i))
        if kid is not None:
            kids.append(kid)
    return kids


def link_table_headers(table_elem):
    """Attach the headers listed on each record in table["cells"].

    Call this only after AddTags. TH and TD must already exist, and each
    header cell must already have the id set in build_table. A data cell
    with headers ["hc2", "hr3"] receives those two elements, in that order.
    """
    rows = [struct_kids(tr) for tr in struct_kids(table_elem) if tr.GetType(True) == "TR"]

    by_id = {}
    for cells in rows:
        for cell_elem in cells:
            tag_id = cell_elem.GetId()
            if tag_id:
                by_id[tag_id] = cell_elem

    for rec in table["cells"]:
        if not rec["headers"]:
            continue
        cell_elem = rows[rec["row"]][rec["col"]]
        for header_id in rec["headers"]:
            header_elem = by_id.get(header_id)
            if header_elem is None:
                raise Exception("Header id not found: " + header_id)
            # -1 appends the header id. False leaves the cell as TD.
            if not cell_elem.AddAssociatedHeader(-1, header_elem, False):
                raise Exception(pdfix.GetError())


def document_element(struct_tree):
    """The single Document tag under the structure-tree root.

    Reuse one if it is already there. Otherwise create it at index 0.
    """
    for i in range(struct_tree.GetNumChildren()):
        obj = struct_tree.GetChildObject(i)
        if obj is None:
            continue
        elem = struct_tree.GetStructElementFromObject(obj)
        if elem is not None and elem.GetType(True) == "Document":
            return elem
    created = struct_tree.AddNewChild("Document", 0)
    if created is None:
        raise Exception(pdfix.GetError())
    return created


pdfix = GetPdfix()
if pdfix is None:
    raise Exception("Pdfix Initialization fail")

doc = pdfix.OpenDoc(INPUT_PDF, "")
if doc is None:
    raise Exception("Unable to open pdf: " + pdfix.GetError())

page = doc.AcquirePage(PAGE_NUM)
if page is None:
    raise Exception("Unable to acquire page: " + pdfix.GetError())

# Leave the existing structure tree in place.
struct_tree = doc.GetStructTree()
if struct_tree is None:
    struct_tree = doc.CreateStructTree()
if struct_tree is None:
    raise Exception(pdfix.GetError())

document = document_element(struct_tree)
# New tags are children of this Div, appended under Document.
# To use another parent, pass that PdsStructElement to tag_region instead.
dest = document.AddNewChild("Div", document.GetNumChildren())
if dest is None:
    raise Exception(pdfix.GetError())

tag_region(page, dest, paragraph["bbox"], build_paragraph)
tag_region(page, dest, table["bbox"], build_table)

# The table is the last child of dest. Link headers only after its TH/TD exist.
tagged = struct_kids(dest)
if not tagged or tagged[-1].GetType(True) != "Table":
    raise Exception("Tagged table was not created")
link_table_headers(tagged[-1])

page.Release()

if not doc.Save(output_path.joinpath("TagContentByBBox.pdf").as_posix(), kSaveFull):
    raise Exception(pdfix.GetError())

doc.Close()
