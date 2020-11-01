# Release information

## update documentation
* make necessary updates to notebooks
* build documentation `cd docs_builder` and `make html`

## make release
* sort imports (`isort src/libsbgnpy`)
* code formating (`black src/libsbgnpy`)
* make sure all tests run (`tox --`)
* update release notes in `release-notes`
* commit changes
* bump version (`bumpversion patch` or `bumpversion` minor)
* `git push --tags` (triggers release)

* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.8
(test) pip install libsbgnpy
```
* merge pull request to master
