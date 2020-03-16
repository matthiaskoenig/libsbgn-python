# Documentation Builder

## Requirements
```bash
cd docs_builder
pip install -r requirements-docs.txt
```

## Build documentation
```
cd docs_builder
make html
```

## Update jupyter notebooks
```
pip install jupyterlab
ipython kernel install --user --name libsbgn-python
```