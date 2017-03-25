![libsbgn-python logo](docs/images/libsbgn-python-logo-small.png)  
[![Documentation Status](https://readthedocs.org/projects/libsbgn-python/badge/?version=latest)](http://libsbgn-python.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/matthiaskoenig/libsbgn-python.svg?branch=develop)](https://travis-ci.org/matthiaskoenig/libsbgn-python)
[![License (LGPL version 3)](https://img.shields.io/badge/license-LGPLv3.0-blue.svg?style=flat-square)](http://opensource.org/licenses/LGPL-3.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.192356.svg)](https://doi.org/10.5281/zenodo.192356)
[![Coverage Status](https://coveralls.io/repos/github/matthiaskoenig/libsbgn-python/badge.svg?branch=develop)](https://coveralls.io/github/matthiaskoenig/libsbgn-python?branch=develop)
# libsbgnpy : Python library for SBGN

Python library to work with [SBGN](http://sbgn.github.io/sbgn/). This library is based on the SBGN XML schema and supports reading, 
writing and validation of SBGN files. Python 2 and python 3 are supported. 
The initial library was generated using [generateDS](https://bitbucket.org/dkuhlman/generateds). Additional utility functions for 
reading, writing and rendering SBGN documents are provided.

Documentation with examples is available at [http://libsbgn-python.readthedocs.io/en/latest/](http://libsbgn-python.readthedocs.io/en/latest/).

* `libsbgn.py` python library
* `libsbgnTypes.py` SBGN type definitions (GlyphClasses, ArcClasses, Languages)
* `utils.py` SBGN utility function like writing & reading of files
* `render.py` SBGN rendering
* `tests` unittests
* `examples/` python examples
* `validation/` validation of SBGN files

To cite libsbgnpy use the following BibTex or equivalent

    @MISC{libsbgnpy,
      author        = {Matthias König},
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
The latest develop version can be installed via
```
pip install git+https://github.com/matthiaskoenig/libsbgn-python.git@develop
```

## Support
To report bugs, request features or asking questions please file an [issue](https://github.com/matthiaskoenig/libsbgn-python/issues).

## Contributing
Contributions are very welcome. The easiest way to fix a typo/bug or implement a feature is by 
following the [contribution guidelines](./CONTRIBUTING.rst).

## Software using libsbgnpy

* [Mimoza](http://mimoza.bordeaux.inria.fr/) takes a model in
SBML format and visualizes it in several formats (downloadable as a
COMBINE archive)

## License
* Source Code: [LGPLv3](http://opensource.org/licenses/LGPL-3.0)
* Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

## Python Language Bindings
The python language bindings were created from the XML schema using
generateDS and than adapted to include GlyphClasses and ArcClasses.
```
/usr/local/bin/generateDS.py -o "libsbgn.py" -s "libsbgnSubs.py" SBGN.xsd
```
The necessary constraints for GlyphClasses, ArcClasses and Languages were added and
some utility functions created.


## ChangeLog
**v0.1.6**
Improved testing and documentation

* New documentation: http://libsbgn-python.readthedocs.io/en/latest/index.html
* Some python 3 bugfixes
* Additional examples 
* Additional tests, coverage & switch to py-test
* pep8 fixes
* tox support and tox testing
* logo

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