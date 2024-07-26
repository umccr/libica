# libica

[//]: # (FIXME commented out PR Build status as it don't get run for some reason...)
[//]: # ([![Pull Request Build Status]&#40;https://github.com/umccr-illumina/libica/workflows/Pull%20Request%20Build/badge.svg&#41;]&#40;https://github.com/umccr-illumina/libica/actions&#41; )
[![PyPI - Downloads](https://img.shields.io/pypi/dm/libica?style=flat)](https://pypistats.org/packages/libica) 
[![PyPI](https://img.shields.io/pypi/v/libica?style=flat)](https://pypi.org/project/libica) 
[![PyPI - License](https://img.shields.io/pypi/l/libica?style=flat)](https://opensource.org/licenses/MIT)

Python SDK to programmatically call Illumina Connected Analytics (ICA) Genomic (multi-omics) data platform and BioInformatics web services. This SDK supports both ICA v1 and v2 APIs:

- ICAv1 API: https://illumina.gitbook.io/ica-v1/reference/r-api
- ICAv2 API: https://help.ica.illumina.com/reference/r-api
- Install through ``pip`` like so:
```commandline
pip install libica
```

## Overview

- Tested for Python 3.8, 3.9, 3.10, 3.11, 3.12
- See [ChangeLog](https://github.com/umccr-illumina/libica/blob/main/CHANGELOG.md) and [Milestones](https://github.com/umccr-illumina/libica/milestones?state=closed)
- [Test Coverage](https://umccr-illumina.github.io/libica/coverage/)
- [Wiki](https://github.com/umccr-illumina/libica/wiki)
- SDK Guide: [PyDoc](https://umccr-illumina.github.io/libica/libica/)
- User Guide: https://umccr-illumina.github.io/libica/

## Getting started with SDK for ICA v2

See [pilot.py](https://github.com/umccr-illumina/libica/blob/main/examples/pilot.py)

```python
# List all data in a project
import os
from contextlib import closing

from libica.openapi.v2 import Configuration, ApiClient, ApiException
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList

if __name__ == '__main__':

    project_id = os.environ['ICAV2_PROJECT_ID']
    file_path = [""]  # empty will list everything under project

    icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
    ica_url = "https://ica.illumina.com/ica/rest"

    configuration = Configuration(
        host=ica_url,
        access_token=icav2_access_token,
    )
    # configuration.debug = True  # uncomment to debug API call logging

    api_client = ApiClient(
        configuration=configuration,
        header_name="Content-Type",
        header_value="application/vnd.illumina.v3+json",
    )

    with closing(api_client) as ctx_api_client:
        project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)

        try:
            page_token = ""
            while True:
                project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                    project_id=project_id,
                    file_path=file_path,
                    page_size=str(1000),
                    page_token=page_token,
                )

                for item in project_data_paged_list.items:
                    project_data: ProjectData = item
                    print((
                        project_data.data.id,  # fil.<ID> (or) fol.<ID>
                        project_data.data.details.path,
                        project_data.data.details.data_type,
                    ))

                page_token = project_data_paged_list.next_page_token
                if not project_data_paged_list.next_page_token:
                    break

        except ApiException as e:
            print(e)
```

You may consider **Using App Package** (see below).

## Getting started with SDK for ICA v1

- Export ICA base URL and JWT Bearer token:
```
export ICA_BASE_URL=<baseUrl>
export ICA_ACCESS_TOKEN=<tok>
```

- Generate Bearer JWT token using [ICA CLI](https://sapac.support.illumina.com/sequencing/sequencing_software/illumina-connected-analytics.html) like so:
```commandline
ica tokens create --help
```

- Somewhere in your Python code:
```python
import os
from libica.openapi import libwes
from libica.openapi.libwes import WorkflowList, WorkflowCompact

ica_base_url = os.getenv("ICA_BASE_URL")
ica_access_token = os.getenv("ICA_ACCESS_TOKEN")

configuration = libwes.Configuration(
    host=ica_base_url,
    api_key={
        'Authorization': ica_access_token
    },
    api_key_prefix={
        'Authorization': "Bearer"
    },
)

with libwes.ApiClient(configuration) as api_client:

    wfl_api: libwes.WorkflowsApi = libwes.WorkflowsApi(api_client)
    try:
        page_token = None
        while True:
            wfl_list: WorkflowList = wfl_api.list_workflows(page_size=100, page_token=page_token)
            # print(wfl_list)
            for item in wfl_list.items:
                wfl: WorkflowCompact = item
                print(wfl.id)
                print(wfl.name)
            page_token = wfl_list.next_page_token
            if not wfl_list.next_page_token:
                break
    except libwes.ApiException as e:
        print(e)
```

## Using [App Package](https://umccr-illumina.github.io/libica/libica/app/index.html)

> NOTE: `libica.app` package contains reusable modules that are based on use cases around UMCCR [Data Portal backend](https://github.com/umccr/data-portal-apis), [Workflows automation and orchestration](https://github.com/umccr/data-portal-apis/tree/dev/docs/pipeline) implementations. Hence, it may be a specific domain logic implementation. However, it may still be reusable for your use cases. Starter examples are as follows.

### App for ICA v2

See [pilotapp.py](https://github.com/umccr-illumina/libica/blob/main/examples/pilotapp.py)

Example: `ProjectDataOps` app to list project files, download a file, etc...

```python
from contextlib import closing

from libica.app import AppHelper
from libica.app.dataops import ProjectDataOps
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.model.project_data import ProjectData

# --- Use AppHelper to build SDK API client

app_helper = AppHelper(debug=False)
project_id = app_helper.get_icav2_cli_session_project_id()

cli_session_api_client: ApiClient = app_helper \
    .build_icav2_configuration_with_cli_session() \
    .get_icav2_api_client()

# --- Construct ProjectDataOps from dataops module

project_dataops = ProjectDataOps(project_id=project_id, api_client=cli_session_api_client)

# --- List all files under given project's folder

# If you do not cd into the folder, it will list all files under the project
project_dataops.cd("/test_folder/")

for item in project_dataops.list_files():
    project_data: ProjectData = item
    print((
        project_data.data.id,  # fil.<ID> (or) fol.<ID>
        project_data.data.details.path,
        project_data.data.details.data_type,
        project_data.data.details.name,
        project_data.data.details.status,
        project_data.data.details.file_size_in_bytes,
        project_data.data.details.time_created,
    ))

# --- Download csv file from given project and file path

file_path = "/test_folder/SampleSheet.csv"
print(f"Downloading {file_path} from project_id {project_id}")
project_dataops.cd(file_path=file_path)
ntf = project_dataops.download_file()
with closing(ntf) as cf:
    with open(cf.name, 'r') as f:
        for line in f.readlines():
            print(line)
```

For more, see PyDoc: 
- https://umccr-illumina.github.io/libica/libica/app/dataops.html

### App for ICA v1

Example: Configuration Object Builder

```python
from libica.app import configuration
from libica.openapi import libgds

gds_config = configuration(
  lib=libgds,  # pass in library of interest e.g. libwes, libtes, etc 
  secret_name=["FROM_AWS_SECRET_MANAGER_THAT_STORE_ICA_ACCESS_TOKEN"],
  base_url="https://use1.platform.illumina.com",  # overwrite if not https://aps2.platform.illumina.com
  debug=False,  # True if you like to debug API calls, False by default anyway, just for demo
)

with libgds.ApiClient(gds_config) as api_client:
    ...
```

Example: Listing Files from GDS

```python
from typing import List

from libica.app import gds
from libica.openapi import libgds

vol, path = gds.parse_path("gds://development/some/folder/path/")
files: List[libgds.FileResponse] = gds.get_file_list(volume_name=vol, path=path)

for file in files:
  print(f"{file.name}, {file.volume_name}, {file.path}, {file.presigned_url}")
```

## Development

- Setup virtual environment and activate it

- Install dev dependencies
```commandline
make install
```

- To bring up _mock_ API _μ_-services
```commandline
make up
```

- To run tests suites
```commandline
make unit
make autounit
```

- To run full suite, smoke test
```commandline
make test
```

### AutoGen Workflow

- SDK is autogenerated from OpenAPI (Swagger) definitions
- There are few tools required for this autogen workflow to work.
    1. [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) -- used to generate code and doc
    2. [redocly/cli](https://github.com/Redocly/redocly-cli) -- validate definitions
- These tools are Node.js app, hence, required build tools `node`, `npm`, `npx` and `yarn` as follows.
```commandline
node -v
v20.15.1

npm i -g yarn
yarn -v
4.3.1

yarn install

npx openapi-generator-cli help
npx redocly lint --help
```
- API mock server `prism` is set up through docker compose as follows.

```
docker --version
Docker version 27.0.3, build 7d4bcd8
```

```
make up
make ps
make test_ica_mock
make test_icav2_mock
docker compose logs
```
- All the autogen config and arrangement refer to [`syncapi.sh`](https://github.com/umccr-illumina/libica/blob/main/syncapi.sh) and [`syncapi2.sh`](https://github.com/umccr-illumina/libica/blob/main/syncapi2.sh) which is called through [`Makefile`](https://github.com/umccr-illumina/libica/blob/main/Makefile) targets.

#### Generator Version

- See generator [version compatibility](https://github.com/OpenAPITools/openapi-generator#11---compatibility)
- Select generator version as follows:

```
npx openapi-generator-cli version-manager list
```

## Notice

- MIT License and DISCLAIMER
- [The Advanced Genomics Collaboration (TAGC)](https://www.tagcaustralia.com)
