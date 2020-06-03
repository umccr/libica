# libiap

Python SDK/Library for IAP -- https://umccr-illumina.github.io/libiap/

* [Test Coverage](https://umccr-illumina.github.io/libiap/coverage/)
* [PyDoc](https://umccr-illumina.github.io/libiap/libiap/)


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
