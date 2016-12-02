"""
Setup module for libsbgn.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject

source distribution generation via
python setup.py sdist
"""

# Always prefer setuptools over distutils
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

    # The project's main homepage.
    url='https://github.com/matthiaskoenig/libsbgn-python',

    # Author details
    author='Matthias Koenig',
    author_email='konigmatt@googlemail.com',

    # Choose your license
    license='LGPL-v3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='SBGN libsbgn',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # exclude=['contrib', 'docs', 'tests*']
    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['enum34'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #    'sample': ['package_data.dat'],
    # },
    
    # include the package data (SBGN, XSD)
    include_package_data=True,

    # Prevent the package manager to install a python egg, 
    # instead you'll get a real directory with files in it.
    zip_safe=False,

)
