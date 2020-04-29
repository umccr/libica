from setuptools import setup, find_packages
from libiap import __version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="libiap",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/umccr/libiap",
    license="TBA",  # FIXME
    author="UMCCR",
    author_email="services@umccr.org",
    description="Python SDK/Library for IAP",
    long_description=long_description,
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "pipdeptree",
            "sphinx",
        ],
        "test": [
            "pytest",
            "flake8",
        ],
    },
    install_requires=[
        "requests",
    ],
)
