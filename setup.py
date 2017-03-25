#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup module for libsbgn-python.

source distribution generation via
python setup.py sdist
"""

# Always prefer setuptools over distutils
from __future__ import absolute_import, print_function
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import re

here = path.abspath(path.dirname(__file__))

# get the version
VERSIONFILE = "libsbgnpy/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='libsbgnpy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=verstr,

    description='libsbgn python bindings',
    long_description=long_description,
    url='https://github.com/matthiaskoenig/libsbgn-python',
    author='Matthias König',
    author_email='konigmatt@googlemail.com',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='SBGN, libsbgn',
    packages=find_packages(),
    install_requires=[
        'enum34',
        'requests',
        'lxml',
        'six'
    ],

    # include the package data (SBGN, XSD)
    include_package_data=True,

    # Prevent the package manager to install a python egg, 
    # instead you'll get a real directory with files in it.
    zip_safe=False,

)
