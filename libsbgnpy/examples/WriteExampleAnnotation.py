# -*- coding: utf-8 -*-

from __future__ import print_function
from libsbgnpy.libsbgnTypes import Language, GlyphClass
from libsbgnpy.libsbgn import *

if __name__ == "__main__":
    f = "sbgn/test-output-annotation.sbgn"

    doc = sbgn()
    m = map()
    m.set_language(Language.PD)
    doc.set_map(m)
    
    # create a glyph with an id and class "macromolecule"
    g1 = glyph()
    g1.set_id("g1")
    g1.set_class(GlyphClass.MACROMOLECULE)

    # create a glyph with an id and class "annotation"
    g2 = glyph()
    g2.set_id("g2")
    g2.set_class(GlyphClass.ANNOTATION);

    co = calloutType()
    co.set_target(g1)

    p = point(x=160, y=200)
    co.set_point(p)
    g2.set_callout(co)

    # add the glyph to the map
    m.add_glyph(g1)
    m.add_glyph(g2)

    # define the bounding box of the glyph
    bbox1 = bbox(x=90, y=160, w=380, h=210)
    g1.set_bbox(bbox1)

    # define the bounding box of the annotation
    bbox2 = bbox(x=5, y=5, w=220, h=125)
    g2.set_bbox(bbox2)

    # define a label for this glyph
    label1 = label(text="LABEL")
    g1.set_label(label1)

    # define a label for this annotation
    label2 = label(text="INFO")
    g2.set_label(label2)

    # now write everything to disk
    doc.write_file(f)
