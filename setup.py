from setuptools import setup, find_packages
from libica import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="libica",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/umccr-illumina/libica",
    license="MIT",
    author="UMCCR and Contributors",
    author_email="services@umccr.org",
    description="Python SDK for Illumina Connected Analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    extras_require={
        "dev": [
            "pipdeptree",
            "twine",
            "setuptools",
            "wheel",
            "pdoc3",
            "mkdocs",
            "mkdocs-material",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "flake8",
            "mockito",
        ],
    },
    install_requires=[
        "requests",
        "python-dateutil",
        "six",
        "urllib3",
        "certifi",
    ],
)
