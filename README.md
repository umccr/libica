# libiap

Python SDK/Library for [IAP](https://iap-docs.readme.io/docs) -- https://umccr-illumina.github.io/libiap/

- Tested for Python 3.6, 3.7, 3.8
- [Test Coverage](https://umccr-illumina.github.io/libiap/coverage/)

## TL;DR

- Install through ``pip`` like so:
```commandline
pip install libiap
```

- Export IAP base URL and auth token:
```
export IAP_BASE_URL=<baseUrl>
export IAP_AUTH_TOKEN=<tok>
```

- Somewhere in your Python code:
```python
import os
from libiap.openapi import libwes
from libiap.openapi.libwes import WorkflowList, WorkflowCompact

iap_auth_token = os.getenv("IAP_AUTH_TOKEN")
iap_base_url = os.getenv("IAP_BASE_URL")

configuration = libwes.Configuration(
    host=iap_base_url,
    api_key={
        'Authorization': iap_auth_token
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
- [libiap.openapi documentation](https://umccr-illumina.github.io/libiap/openapi/)
- [PyDoc](https://umccr-illumina.github.io/libiap/libiap/)
- [Wiki](https://github.com/umccr-illumina/libiap/wiki)

## Development

- Setup virtual environment and activate it

- Install dependencies
```commandline
make install
```

- To run unit tests suite
```commandline
make unit
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
