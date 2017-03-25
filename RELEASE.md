# Release info
Steps for release are
* update version number in develop branch
* update documentation & add changes to changelog
* merge all develop changes to master via pull request
* create release from master branch in github
* update zenodo information (DOI & citation)
* release on [pypi](https://pypi.python.org/pypi/libsbgnpy)
```
python setup.py sdist upload
```
* switch to develop branch and increase version number