# Example Notebooks

Jupyter Notebook examples on how to use `libiap` to access IAP web services programmatically.

## Getting Started

```
cd notebooks
conda create -n iapnb python=3.8
conda activate iapnb
conda install -c conda-forge notebook
jupyter notebook
```

## Clearing Outputs 

Please note that if you are contributing, before commit, please clear notebook outputs.

```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/*.ipynb
```

- [How to clear the Jupyter Notebook outputs automatically?](https://medium.com/somosfit/version-control-on-jupyter-notebooks-6b67a0cf12a3)
