# libica

Python SDK to programmatically call Illumina Connected Analytics (ICA) BioInformatics web services i.e. SDK for API https://ica-docs.readme.io/reference
- Workflow Execution Service (WES)
- Task Execution Service (TES)
- Genomic Data Store (GDS)
- Developer Console Service (DCS)
- Event Notification Service (ENS)

**Overview:**

- https://umccr-illumina.github.io/libica/
- Tested for Python 3.6, 3.7, 3.8, 3.9
- [Test Coverage](https://umccr-illumina.github.io/libica/coverage/)

## TL;DR

- Install through ``pip`` like so:
```commandline
pip install libica
```

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

More examples available at:
- [libica.openapi documentation](https://umccr-illumina.github.io/libica/openapi/)
- [PyDoc](https://umccr-illumina.github.io/libica/libica/)
- [Wiki](https://github.com/umccr-illumina/libica/wiki)

## Development

- Setup virtual environment and activate it

- Install dependencies
```commandline
make install
```

- To run unit tests suite
```commandline
make unit
make autounit
```

- To bring up _mock_ API _μ_-services
```commandline
make up
```

- To run integration tests suite (required services fully up)
```commandline
make it
```

- To run full test suite (required services fully up)
```commandline
make test
```

- Most of the dev pipelines are in [`Makefile`](Makefile) workflow


## License

MIT License and DISCLAIMER

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
