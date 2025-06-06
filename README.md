# libica

[![Pull Request Build Status](https://github.com/umccr/libica/workflows/Pull%20Request%20Build/badge.svg)](https://github.com/umccr/libica/actions) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/libica?style=flat)](https://pypistats.org/packages/libica) 
[![PyPI](https://img.shields.io/pypi/v/libica?style=flat)](https://pypi.org/project/libica) 
[![PyPI - License](https://img.shields.io/pypi/l/libica?style=flat)](https://opensource.org/licenses/MIT)

Python SDK to programmatically call Illumina Connected Analytics (ICA) Genomic (multi-omics) data platform and BioInformatics web services.

- ICA API: https://help.ica.illumina.com/reference/r-api
- Install through ``pip`` like so:
```commandline
pip install libica
```

## Overview

- Tested for Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- [Test Coverage](https://umccr.github.io/libica/coverage/)
- SDK Guide: [PyDoc](https://umccr.github.io/libica/libica/)
- User Guide: https://umccr.github.io/libica/

## Roadmap

- See [changelog](https://github.com/umccr/libica/blob/main/CHANGELOG.md) and [closed milestones](https://github.com/umccr/libica/milestones?state=closed)
- See opening [milestones](https://github.com/umccr/libica/milestones) for current planning and next SDK release

## Release

There are two SDK Python packages, namely `v2` and `v3`. If you are a new starter, please use `v3` SDK package. If you are an existing user, please upgrade to `v3` when you can. Most of the time, this should be straight forward with minor tuning to application code. Since `v3` release, the SDK `v2` package now enter into maintenance mode and deprecate by 2026 Oct.

## Example

- See [examples](https://github.com/umccr/libica/tree/main/examples) directory for some example scripts
- See [wrapica](https://github.com/umccr/wrapica) and [icav2-cli-plugins](https://github.com/umccr/icav2-cli-plugins) for client application that build on top of SDK

## Notice

- MIT License and DISCLAIMER
- [The Advanced Genomics Collaboration (TAGC)](https://www.tagcaustralia.com)
