3.1
-----
* Release date: 2025-07-31
* Updated for upstream ICA API Release -- [2025 June 02 - ICA v2.36.1](https://help.ica.illumina.com/reference/software-release-notes/2025#id-2025-june-23-ica-v2.36.1)
* See [milestone 3.1 for all related PRs](https://github.com/umccr/libica/milestone/13?closed=1)

3.0
-----
* Release date: 2025-06-06
* Made the major SDK v3 update with Pydantic-based Python code generator.
* Retained SDK v2 package as Long-term support (LTS) maintenance mode.
* Deprecated ICA v1 packages.
* Updated for upstream ICA API Release -- [2025 June 02 - ICA v2.36.0](https://help.ica.illumina.com/reference/software-release-notes/2025#id-2025-june-2-ica-v2.36.0)
* See [milestone 3.0 for all related PRs](https://github.com/umccr/libica/milestone/12?closed=1)

2.5.0
-----
* Release date: 2024-07-31
* Updated for upstream ICA v2 API Release -- [2024 July 10 - ICA v2.27.1](https://help.ica.illumina.com/reference/software-release-notes/2024#id-2024-july-10-ica-v2.27.1)
* Updated for upstream ICA v1 API Release
* See [milestone 2.5.0 for all related PRs](https://github.com/umccr/libica/milestone/11?closed=1)

2.4.0
-----
* Release date: 2024-03-06
* Updated for upstream ICA v2 API Release -- [2024 February 28 - ICA v2.23.0](https://help.ica.illumina.com/reference/software-release-notes/2024#id-2024-february-28-ica-v2.23.0)
* Updated for upstream ICA v1 API Release
* See [milestone 2.4.0 for all related PRs](https://github.com/umccr/libica/milestone/10?closed=1)

2.3.0
-----
* Release date: 2023-10-10
* Updated for upstream ICA v2 API Release -- [2023 October 3 - ICA v2.19.0](https://help.ica.illumina.com/reference/software-release-notes/2023#id-2023-october-3-ica-v2.19.0)
* Updated for upstream ICA v1 API Release
* See [milestone 2.3.0 for all related PRs](https://github.com/umccr/libica/milestone/9?closed=1)

2.2.1
-----
* Release date: 2023-03-25
* Added generating GDS PreSigned URL with override options 
* See [milestone 2.2.1 for all related PRs](https://github.com/umccr/libica/milestone/8?closed=1)

2.2.0
-----
* Release date: 2023-02-06
* Updated for upstream ICA v2 API Release -- [28 February 2023 - ICA v2.13.0](https://help.ica.illumina.com/reference/software-release-notes/2023#id-2023-february-28-ica-v2.13.0)
* Updated for upstream ICA v1 API Release
* Dropped Python 3.6 support
* Added Python 3.11 support
* See [milestone 2.2.0 for all related PRs](https://github.com/umccr/libica/milestone/7?closed=1)

2.1.0
-----
* Release date: 2022-06-14
* Updated for upstream ICA v2 API Release -- [07 June 2022 - ICA v2.6.0 and CLI v2.3.0](https://help.ica.illumina.com/reference/software-release-notes/2022#id-2022-june-07-ica-v2.6.0-and-cli-v2.3.0-1)
* Updated for upstream ICA v1 API Release -- _apparently a couple of updates in GDS_
* Refactored and improved App package
* Added Python 3.10 support
* See [milestone 2.1.0 for all related PRs](https://github.com/umccr/libica/milestone/6?closed=1)

2.0.0
-----
* Release date: 2022-02-23
* New epic feature support to [ICA v2: API version 3](https://ica.illumina.com/ica/api/swagger/index.html)
* Upgraded to OpenAPI Generator version `5.4.0`
* Retain dual API versions support: ICA v1 & v2
* See [milestone 2.0.0 for all related PRs](https://github.com/umccr/libica/milestone/4?closed=1)

1.1.0
-----
* Release date: 2021-11-05
* Added App Package for reusable implementations
* See [milestone 1.1.0 for all related PRs](https://github.com/umccr/libica/milestone/5?closed=1)

1.0.0
-----
* Release date: 2021-10-22
* We run `libica` over a year, hence, it matures into major version 1.0
* This is also to keep track with ICA v1  
* [Updated to upstream ICA OpenAPI Swagger definitions PR#45](https://github.com/umccr/libica/pull/45)
* See [milestone 1.0.0 for all related PRs](https://github.com/umccr/libica/milestone/3?closed=1)

0.5.0
-----
* Release date: 2021-03-08
* Major package rename refactor from IAP to ICA  
* [Updated to upstream ICA OpenAPI Swagger definitions PR#33](https://github.com/umccr/libica/pull/33)
* Removed deprecated alpha modules
* See [milestone 0.5.0 for all related PRs](https://github.com/umccr/libica/milestone/2?closed=1)

0.4.0
-----
* Release date: 2020-11-09
* [Updated to upstream ICA OpenAPI Swagger definitions PR#22](https://github.com/umccr/libica/pull/22)
* Ignored generating TES heartbeat endpoint
* Added support for token alias
* Added deprecation warning for alpha modules
* See [milestone 0.4.0 for all related PRs](https://github.com/umccr/libica/milestone/1?closed=1)

0.3.0
-----
* Release date: 2020-08-06
* [Updated to upstream ICA OpenAPI Swagger definitions PR#17](https://github.com/umccr/libica/pull/17)
* Deprecated Sphinx in favour mkdocs and Wiki for documentation
* Added HAProxy for improved integration tests

0.2.0
-----
* Release date: 2020-06-12
* Added [openapi-generator](https://github.com/OpenAPITools/openapi-generator) auto generated SDK
* Added [Prism](https://stoplight.io/open-source/prism/) for integration test mock server
* Added `syncapi.sh` script and `Makefile` workflow for repeatable auto SDK generation

0.1.0
-----
* Release date: 2020-05-01
* Initial release with implementation to all GET API calls
