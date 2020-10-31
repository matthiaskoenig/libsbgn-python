libsbgnpy : Python library for SBGN
====================================

.. image:: https://github.com/matthiaskoenig/libsbgn-python/workflows/CI-CD/badge.svg
   :target: https://github.com/matthiaskoenig/libsbgn-python/actions?query=CI-CD
   :alt: GitHub Actions CI/CD Status

.. image:: https://img.shields.io/pypi/v/libsbgnpy.svg
   :target: https://pypi.org/project/libsbgnpy/
   :alt: Current PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/libsbgnpy.svg
   :target: https://pypi.org/project/libsbgnpy/
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/libsbgnpy.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3

.. image:: https://codecov.io/gh/matthiaskoenig/libsbgn-python/branch/develop/graph/badge.svg
   :target: https://codecov.io/gh/matthiaskoenig/libsbgn-python
   :alt: Codecov

.. image:: https://readthedocs.org/projects/libsbgn-python/badge/?version=latest
   :target: https://libsbgn-python.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.597155.svg
   :target: https://doi.org/10.5281/zenodo.597155
   :alt: Zenodo DOI

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Black


Python library to work with the Systems Biology Graphical Notation (`SBGN <http://sbgn.github.io/sbgn/>`__). This library is based on the SBGN XML schema and supports reading, 
writing and validation of SBGN files.

The initial library was generated using `generateDS <https://pypi.org/project/generateDS/>`__. Additional utility functions for reading, writing, and rendering SBGN documents are provided.

Documentation with examples is available at `https://libsbgn-python.readthedocs.io <https://libsbgn-python.readthedocs.io>`__.

* ``libsbgn.py`` python library
* ``libsbgnTypes.py`` SBGN type definitions (GlyphClasses, ArcClasses, Languages)
* ``utils.py`` SBGN utility function like writing & reading of files
* ``render.py`` SBGN rendering
* ``test/`` unittests
* ``examples/`` python examples
* ``validation/`` validation of SBGN files


How to cite
===========
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.597155.svg
   :target: https://doi.org/10.5281/zenodo.597155
   :alt: Zenodo DOI

Installation
============
``libsbgnpy`` is available from `pypi <https://pypi.python.org/pypi/libsbgnpy>`__ and
can be installed via::

    pip install libsbgnpy

Support
=======
To report bugs, request features or asking questions please file an `issue <https://github.com/matthiaskoenig/libsbgn-python/issues/new>`__.

License
=======

* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The libsbgnpy source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054).


Software using libsbgnpy
========================
* `Mimoza <http://mimoza.bordeaux.inria.fr/>`__ takes a model in
SBML format and visualizes it in several formats (downloadable as a
COMBINE archive).


Python Language Bindings
========================
The python language bindings were created from the XML schema using
generateDS and than adapted to include GlyphClasses and ArcClasses.::

    /usr/local/bin/generateDS.py -o "libsbgn.py" -s "libsbgnSubs.py" SBGN.xsd

The necessary constraints for GlyphClasses, ArcClasses and Languages were added and
some utility functions created.

© 2016-2020 Matthias König
