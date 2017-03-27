# -*- coding: utf-8 -*-
"""
Write and read notes information.
Notes must be XML elements in a <notes>Tag</notes>


"""



from __future__ import print_function, absolute_import
import os
import libsbgnpy.libsbgn as libsbgn  # import the bindings
from libsbgnpy.libsbgnTypes import Language, ArcClass, GlyphClass, Extension, Notes
from libsbgnpy.utils import write_to_string


def write_glyph_notes(f):
    """ Set notes on element.
    
    :return: 
    """
    sbgn = libsbgn.sbgn()
    map = libsbgn.map()
    map.set_language(Language.PD)
    sbgn.set_map(map)

    # create a glyph with an id and class "macromolecule"
    g = libsbgn.glyph()
    g.set_id("g1")

    # define a label for this glyph
    label = libsbgn.label()
    label.set_text("INSR")

    bbox = libsbgn.bbox(x=100, y=100, w=80, h=40)
    g.set_bbox(bbox)
    map.add_glyph(g)

    # add notes
    g_notes = Notes()
    g_notes.set_xml_string('<body xmlns="http://www.w3.org/1999/xhtml">\n'
                          'This is an example note describing the INSR glyph.\n'
                          '</body>')
    g.set_notes(g_notes)

    # print all notes
    glyphs = map.get_glyph()
    for g in glyphs:
        notes = g.get_notes()
        print('\n*** {} {} ***'.format(g.get_id(), type(notes)))
        print(notes)

    sbgn.write_file(f)

def read_glyph_notes(f):
    """ Read notes from glyphs.
    
    :return: 
    """
    sbgn = libsbgn.parse(f)

    # map is a container for the glyphs and arcs
    map = sbgn.get_map()

    glyphs = map.get_glyph()
    for g in glyphs:
        notes = g.get_notes()
        print('\n*** {} {} ***'.format(g.get_id(), type(notes)))
        print(notes)


if __name__ == "__main__":
    f = 'sbgn/notes.sbgn'
    write_glyph_notes(f)

    read_glyph_notes(f)

