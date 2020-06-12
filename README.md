# libiap

Python SDK/Library for IAP -- https://umccr-illumina.github.io/libiap/

* [OpenAPI](https://umccr-illumina.github.io/libiap/openapi/)
* [PyDoc](https://umccr-illumina.github.io/libiap/libiap/)
* [Test Coverage](https://umccr-illumina.github.io/libiap/coverage/)


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
from libiap import libgds

for file in libgds.list_files(volume_name='my-gds-volume-name'):
    print(file)
```

- Using OpenAPI:
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

- More examples/tutorials available at [User Guide](https://umccr-illumina.github.io/libiap/user/)


## Development

- Pilot run or Integration Test:
```
export IAP_BASE_URL=<baseUrl>
export IAP_AUTH_TOKEN=<tok>
python pilot.py
```

- See [Developer Guide](https://umccr-illumina.github.io/libiap/developer/) for more notes


## License

MIT License and DISCLAIMER

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
