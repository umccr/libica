2.2.0
-----
* Release date: 2023-02-06
* Updated for upstream ICA v2 API Release -- [28 February 2023 - ICA v2.13.0](https://help.ica.illumina.com/reference/r-releasenotes#28-february-2023-ica-v2.13.0)
* Updated for upstream ICA v1 API Release
* Dropped Python 3.6 support
* Added Python 3.11 support
* See [milestone 2.2.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/7?closed=1)

2.1.0
-----
* Release date: 2022-06-14
* Updated for upstream ICA v2 API Release -- [07 June 2022 - ICA v2.6.0 and CLI v2.3.0](https://help.ica.illumina.com/reference/r-releasenotes#07-june-2022-ica-v2.6.0-and-cli-v2.3.0)
* Updated for upstream ICA v1 API Release -- _apparently a couple of updates in GDS_
* Refactored and improved App package
* Added Python 3.10 support
* See [milestone 2.1.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/6?closed=1)

2.0.0
-----
* Release date: 2022-02-23
* New epic feature support to [ICA v2: API version 3](https://ica.illumina.com/ica/api/swagger/index.html)
* Upgraded to OpenAPI Generator version `5.4.0`
* Retain dual API versions support: ICA v1 & v2
* See [milestone 2.0.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/4?closed=1)

1.1.0
-----
* Release date: 2021-11-05
* Added App Package for reusable implementations
* See [milestone 1.1.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/5?closed=1)

1.0.0
-----
* Release date: 2021-10-22
* We run `libica` over a year, hence, it matures into major version 1.0
* This is also to keep track with ICA v1  
* [Updated to upstream ICA OpenAPI Swagger definitions PR#45](https://github.com/umccr-illumina/libica/pull/45)
* See [milestone 1.0.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/3?closed=1)

0.5.0
-----
* Release date: 2021-03-08
* Major package rename refactor from IAP to ICA  
* [Updated to upstream ICA OpenAPI Swagger definitions PR#33](https://github.com/umccr-illumina/libica/pull/33)
* Removed deprecated alpha modules
* See [milestone 0.5.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/2?closed=1)

0.4.0
-----
* Release date: 2020-11-09
* [Updated to upstream ICA OpenAPI Swagger definitions PR#22](https://github.com/umccr-illumina/libica/pull/22)
* Ignored generating TES heartbeat endpoint
* Added support for token alias
* Added deprecation warning for alpha modules
* See [milestone 0.4.0 for all related PRs](https://github.com/umccr-illumina/libica/milestone/1?closed=1)

0.3.0
-----
* Release date: 2020-08-06
* [Updated to upstream ICA OpenAPI Swagger definitions PR#17](https://github.com/umccr-illumina/libica/pull/17)
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
