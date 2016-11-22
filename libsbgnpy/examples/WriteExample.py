# -*- coding: utf-8 -*-
from __future__ import print_function
import libsbgnpy.libsbgn as libsbgn 
from libsbgnpy.libsbgnTypes import GlyphClass

if __name__ == "__main__":
    f = "sbgn/test-output.sbgn"

    sbgn = libsbgn.sbgn()
    map = libsbgn.map()
    sbgn.set_map(map)

    # create a glyph with an id and class "macromolecule"
    g1 = libsbgn.glyph()
    g1.set_id("glyph1")
    g1.set_class(GlyphClass.MACROMOLECULE)

    # add the glyph to the map
    map.add_glyph(g1)

    # define the bounding box of the glyph
    bbox1 = libsbgn.bbox(x=125, y=60, w=100, h=40)
    g1.set_bbox(bbox1)
    
    # define a label for this glyph
    label1 = libsbgn.label()
    label1.set_text("P53")

    # now write everything to disk
    sbgn.write_file(f)
