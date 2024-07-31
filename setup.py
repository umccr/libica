from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="libica",
    version="2.5.0",
    url="https://github.com/umccr-illumina/libica",
    license="MIT",
    author="UMCCR and Contributors",
    author_email="services@umccr.org",
    description="Python SDK for Illumina Connected Analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests**", "**test**", "docs")),
    project_urls={
        "Bug Tracker": "https://github.com/umccr-illumina/libica/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    extras_require={
        "dev": [
            "pipdeptree",
            "twine",
            "setuptools",
            "wheel",
            "build",
            "pdoc3",
            "mkdocs",
            "mkdocs-material",
            "openapi-spec-validator",
            "pre-commit",
            "detect-secrets",
            "black",
            "ggshield"
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "flake8",
            "mockito",
            "tox",
            "nose2",
        ],
    },
    install_requires=[
        "requests",
        "python-dateutil",
        "six",
        "urllib3",
        "certifi",
        "PyYAML",
        "boto3",
        "botocore",
    ],
)
