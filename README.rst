libsbgn-python
=======================

Python bindings for SBGN based on the XML schema. Prelimenary bindings were generated with generateDS and than adapted to include GlyphClasses and ArcClasses.

* libsbgn.py - python bindings
* libsbgnTypes.py - SBGN type definitions (GlyphClasses, ArcClasses, Languages)
* examples.py - SBGN import and export example

Open Issues
* python package building & upload to pip
* XML schema validation of files against XSD file
* proper imports in python package
* split read example, write example, validate example
* test python 3 support (?enum vs. enum34 import)
* documentation sphynx

