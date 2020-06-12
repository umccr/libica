# libiap.openapi.libconsole.RegionsApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_regions**](RegionsApi.md#list_regions) | **GET** /v1/regions | Get a list of available regions


# **list_regions**
> list[Region] list_regions(instrument_type=instrument_type, version=version)

Get a list of available regions

Get a list of available regions

### Example

* Api Key Authentication (Basic):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.RegionsApi(api_client)
    instrument_type = 'instrument_type_example' # str | Instrument type (optional)
version = 'version_example' # str | Instrument version (optional)

    try:
        # Get a list of available regions
        api_response = api_instance.list_regions(instrument_type=instrument_type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegionsApi->list_regions: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.RegionsApi(api_client)
    instrument_type = 'instrument_type_example' # str | Instrument type (optional)
version = 'version_example' # str | Instrument version (optional)

    try:
        # Get a list of available regions
        api_response = api_instance.list_regions(instrument_type=instrument_type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegionsApi->list_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_type** | **str**| Instrument type | [optional] 
 **version** | **str**| Instrument version | [optional] 

### Return type

[**list[Region]**](Region.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Regions found and returned successfully. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

