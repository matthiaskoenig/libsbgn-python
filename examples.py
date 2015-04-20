# -*- coding: utf-8 -*-
"""
Use python bindings to SBGN (generated by generateDS) to interact
with SBGN maps.

generateDS.py -o libsbgn.py -s libsbgnSubs.py SBGN.xsd

@author: Matthias Koenig & Augustin Luna
Created on Mon Apr 20 19:02:22 2015

TODO: export write <?xml version="1.0" encoding="UTF-8"?>
TODO: export no sbgn: prefix
TODO: test export in vanted

TODO: encode class restrictions & test for the classes

TODO: git repository
TODO: documentation sphynx
TODO: python package

"""
from __future__ import print_function
import libsbgn         # import the bindings
print(libsbgn.__all__)

def print_bbox(b):
    print('x, y, w, h : ', b.get_x(), b.get_y(), b.get_w(), b.get_h())

#################################################################
# read SBGN
#################################################################
f_in = 'examples/adh.sbgn'

# sbgn and map
sbgn = libsbgn.parse(f_in)
map = sbgn.get_map()
print('***', map.get_language(), '***')

# bbox
'''
<bbox x="0" y="0" w="363" h="253"/>
'''
box = map.get_bbox()
print_bbox(box)

# glyphs
'''
<glyph class="simple chemical" id="glyph1">
		<label text="Ethanol"/> <!-- fontsize="" etc -->
		<!-- Line breaks are allowed in the text attribute -->
		<bbox x="40" y="120" w="60" h="60"/>
	</glyph>
'''
glyphs = map.get_glyph()
for g in glyphs:
    cls = g.get_class()
    print(cls, g.get_id())
    label =  g.get_label()
    if cls == 'simple chemical':   
        print('label: ', label.get_text())
        
    if cls == 'process':
        for p in g.get_port():
            print('port ', p.get_id(), p.get_x(), p.get_y())
    
    box = g.get_bbox()
    print_bbox(box)
    print

# arcs
'''
	<arc class="consumption" source="glyph_nad" target="pn1.1" id="a06">
		<start x="95" y="202" />
		<end x="136" y="180" />			
	</arc>
'''
arcs = map.get_arc()
for a in arcs:
    print(a.get_class(), a.get_source(), a.get_target(), a.get_id())
    start = a.get_start()
    print(start.x, start.y)
    end = a.get_end()
    print(end.x, end.y)


#################################################################
# write SBGN
#################################################################
from libsbgnTypes import Language, GlyphClass, ArcClass, Orientation
reload(libsbgn)

sbgn = libsbgn.sbgn()
map = libsbgn.map()
map.set_language(Language.PD)
sbgn.set_map(map)
print(map)

'''
<bbox x="0" y="0" w="363" h="253"/>
'''
# box = libsbgn.bbox()
# box.set_x(0)
# box.set_y(0)
# box.set_w(363)
# box.set_h(253)
box = libsbgn.bbox(x=0, y=0, w=363, h=253)
map.set_bbox(box)

'''
	<glyph class="simple chemical" id="glyph1">
		<label text="Ethanol"/> <!-- fontsize="" etc -->
		<!-- Line breaks are allowed in the text attribute -->
		<bbox x="40" y="120" w="60" h="60"/>
	</glyph>
'''
# glyphs with labels
g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph1')
g.set_label(libsbgn.label(text='Ethanol'))
g.set_bbox(libsbgn.bbox(x=40, y=120, w=60, h=60))
map.add_glyph(g)

g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph_ethanal')
g.set_label(libsbgn.label(text='Ethanal'))
g.set_bbox(libsbgn.bbox(x=220, y=110, w=60, h=60))
map.add_glyph(g)

g = libsbgn.glyph(class_=GlyphClass.MACROMOLECULE, id='glyph_adh1')
g.set_label(libsbgn.label(text='ADH1'))
g.set_bbox(libsbgn.bbox(x=106, y=20, w=108, h=60))
map.add_glyph(g)

g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph_h')
g.set_label(libsbgn.label(text='H+'))
g.set_bbox(libsbgn.bbox(x=220, y=190, w=60, h=60))
map.add_glyph(g)

g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph_nad')
g.set_label(libsbgn.label(text='NAD+'))
g.set_bbox(libsbgn.bbox(x=40, y=190, w=60, h=60))
map.add_glyph(g)

g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph_nadh')
g.set_label(libsbgn.label(text='NADH'))
g.set_bbox(libsbgn.bbox(x=300, y=150, w=60, h=60))
map.add_glyph(g)

# glyph with ports (process)
g = libsbgn.glyph(class_=GlyphClass.PROCESS, id='pn1', 
                  orientation=Orientation.HORIZONTAL)
g.set_bbox(libsbgn.bbox(x=148, y=168, w=24, h=24))
g.add_port(libsbgn.port(x=136, y=180, id="pn1.1"))
g.add_port(libsbgn.port(x=184, y=180, id="pn1.2"))
map.add_glyph(g)

# arcs
a = libsbgn.arc(class_=ArcClass.CONSUMPTION, source="glyph1", target="pn1.1", id="a01")
a.set_start(libsbgn.startType(x=98, y=160))
a.set_end(libsbgn.endType(x=98, y=160))
map.add_arc(a)

a = libsbgn.arc(class_=ArcClass.PRODUCTION, source="pn1.2", target="glyph_nadh", id="a02")
a.set_start(libsbgn.startType(x=184, y=180))
a.set_end(libsbgn.endType(x=300, y=180))
map.add_arc(a)

a = libsbgn.arc(class_=ArcClass.CATALYSIS, source="glyph_adh1", target="pn1", id="a03")
a.set_start(libsbgn.startType(x=160, y=80))
a.set_end(libsbgn.endType(x=160, y=168))
map.add_arc(a)

a = libsbgn.arc(class_=ArcClass.PRODUCTION, source="pn1.2", target="glyph_h", id="a04")
a.set_start(libsbgn.startType(x=184, y=180))
a.set_end(libsbgn.endType(x=224, y=202))
map.add_arc(a)

a = libsbgn.arc(class_=ArcClass.PRODUCTION, source="pn1.2", target="glyph_ethanal", id="a05")
a.set_start(libsbgn.startType(x=184, y=180))
a.set_end(libsbgn.endType(x=224, y=154))
map.add_arc(a)

a = libsbgn.arc(class_=ArcClass.CONSUMPTION, source="glyph_nad", target="pn1.1", id="a06")
a.set_start(libsbgn.startType(x=95, y=202))
a.set_end(libsbgn.endType(x=136, y=180))
map.add_arc(a)

# export(self, outfile, level, namespace_='sbgn:', name_='sbgn', namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', pretty_print=True)
f_out = open('examples/test.sbgn', 'w')
sbgn.export(f_out, level=0, namespace_='')
f_out.close()