[![Build Status](https://travis-ci.org/matthiaskoenig/libsbgn-python.svg?branch=develop)](https://travis-ci.org/matthiaskoenig/libsbgn-python)
[![License (LGPL version 3)](https://img.shields.io/badge/license-LGPLv3.0-blue.svg?style=flat-square)](http://opensource.org/licenses/LGPL-3.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.192356.svg)](https://doi.org/10.5281/zenodo.192356)
[![Coverage Status](https://coveralls.io/repos/github/matthiaskoenig/libsbgn-python/badge.svg?branch=develop)](https://coveralls.io/github/matthiaskoenig/libsbgn-python?branch=develop)
# libsbgnpy : Python bindings for SBGN

Python bindings for SBGN based on the XML schema.
Initial bindings were generated with generateDS. The necessary constraints for GlyphClasses, ArcClasses and Languages were added and some utility functions created. Python examples for reading and writing can be found in the examples folder. Currently, validation against schema files is not implemented.

* `libsbgn.py` python bindings
* `libsbgnTypes.py` SBGN type definitions (GlyphClasses, ArcClasses, Languages)
* `libsbgnUtils.py` SBGN helper functions
* `tests` unittests
* `examples/` python examples
* `validation/` validation of SBGN files

libsbgnpy supports py2 and py3.

To cite libsbgnpy use the following BibTex or equivalent

    @MISC{libsbgnpy,
      author        = {Matthias Koenig},
      title         = {libsbgnpy: Python bindings for SBGN},
      month         = {Dec.},
      year          = {2016},
      doi           = "{10.5281/zenodo.192356}",
      url           = "{http://dx.doi.org/10.5281/zenodo.192356}",
      howpublished  = {https://github.com/matthiaskoenig/libsbgn-python/blob/master/README.md}
    }

## Installation

The package is available from [pypi](https://pypi.python.org/pypi/libsbgnpy)
```
pip install libsbgnpy
```

## Support

For bugs, feature requests and support file an [issue](https://github.com/matthiaskoenig/libsbgn-python/issues).


## Software using libsbgnpy

* [Mimoza](http://mimoza.bordeaux.inria.fr/) takes a model in
SBML format and visualizes it in several formats (downloadable as a
COMBINE archive)

## Usage example

```python
import libsbgnpy.libsbgn as libsbgn 
from libsbgnpy.libsbgnTypes import Language, GlyphClass, ArcClass, Orientation

# create empty sbgn
sbgn = libsbgn.sbgn()

# create map, set language and set in sbgn
map = libsbgn.map()
map.set_language(Language.PD)
sbgn.set_map(map)

# create a bounding box for the map
# <bbox x="0" y="0" w="363" h="253"/>
# [1] de novo and set all attributes
# box = libsbgn.bbox()
# box.set_x(0)
# box.set_y(0)
# box.set_w(363)
# box.set_h(253)
# [2] de novo with attributes at creation
box = libsbgn.bbox(x=0, y=0, w=363, h=253)
map.set_bbox(box)

# create some glyphs
# class attribute is named 'class_' ! in glyphs and arcs
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
# create arcs and set the start and end points
a = libsbgn.arc(class_=ArcClass.CONSUMPTION, source="glyph1", target="pn1.1", id="a01")
a.set_start(libsbgn.startType(x=98, y=160))
a.set_end(libsbgn.endType(x=136, y=180))
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

# write everything to a file
sbgn.write_file('sbgn/test.sbgn')
```

## License
* Source Code: [LGPLv3](http://opensource.org/licenses/LGPL-3.0)
* Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

## Python Language Bindings
The python language bindings were created from the XML schema using
generateDS and than adapted to include GlyphClasses and ArcClasses.
```
/usr/local/bin/generateDS.py -o "libsbgn.py" -s "libsbgnSubs.py" SBGN.xsd
```

## ChangeLog
**v0.1.5**

* py3 support bugfixes
* SBGN validation with XSD schema
* update of bindings from latest schema
* bug fix in writing some attributes

**v0.1.4**

* support for py2.6, 2.7, 3.4, 3.5
* continuous integration with travis

**v0.1.3**

* unittests added
* x, y, w, d handled as float instead int according to specification


**v0.1.2**

* initial release