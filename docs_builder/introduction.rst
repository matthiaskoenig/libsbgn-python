Introduction
===============
.. image:: ./images/libsbgn-python-logo-small.png

Overview
------------
Python library to work with `SBGN <http://sbgn.github.io/sbgn/>`_. This library is based on the SBGN XML schema and supports reading,
writing and validation of SBGN files. Python 2 and python 3 are supported.
The initial library was generated using `generateDS <https://bitbucket.org/dkuhlman/generateds>`_. Additional utility functions for
reading, writing and rendering SBGN documents are provided.

To cite libsbgnpy use the following BibTex or equivalent::

    @MISC{libsbgnpy,
      author        = {Matthias König},
      title         = {libsbgnpy: Python library for SBGN},
      month         = {Mar.},
      year          = {2017},
      doi           = "{10.5281/zenodo.192356}",
      url           = "{http://dx.doi.org/10.5281/zenodo.438137}",
      howpublished  = {https://github.com/matthiaskoenig/libsbgn-python/blob/master/README.md}
    }

Source code is available from
`https://github.com/matthiaskoenig/libsbgn-python
<https://github.com/matthiaskoenig/libsbgn-python>`_.

To report bugs, request features or asking questions please file an
`issue
<https://github.com/matthiaskoenig/libsbgn-python/issues>`_.

Installation
------------
The libsbgn-python package is available from `pypi
<https://github.com/matthiaskoenig/libsbgn-python>`_ and can be installed via::

    pip install libsbgnpy

The latest develop version can be installed via::

    pip install git+https://github.com/matthiaskoenig/libsbgn-python.git@develop
