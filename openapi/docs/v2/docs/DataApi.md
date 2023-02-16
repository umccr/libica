# libica.openapi.v2.DataApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_download_url_for_data_without_project_context**](DataApi.md#create_download_url_for_data_without_project_context) | **POST** /api/data/{dataUrn}:createDownloadUrl | Retrieve a download URL for this data.
[**create_inline_view_url_for_data_without_project_context**](DataApi.md#create_inline_view_url_for_data_without_project_context) | **POST** /api/data/{dataUrn}:createInlineViewUrl | Retrieve an URL for this data to use for inline view in a browser.
[**get_data**](DataApi.md#get_data) | **GET** /api/data/{dataUrn} | Retrieve a data.


# **create_download_url_for_data_without_project_context**
> Download create_download_url_for_data_without_project_context(data_urn)

Retrieve a download URL for this data.

Can be used to download a file directly from the region where it is located, no connector is needed. Not applicable for Folder.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import data_api
from libica.openapi.v2.model.download import Download
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)
    data_urn = "dataUrn_example" # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a download URL for this data.
        api_response = api_instance.create_download_url_for_data_without_project_context(data_urn)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DataApi->create_download_url_for_data_without_project_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. |

### Return type

[**Download**](Download.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inline_view_url_for_data_without_project_context**
> InlineView create_inline_view_url_for_data_without_project_context(data_urn)

Retrieve an URL for this data to use for inline view in a browser.

Can be used to view a file directly from the region where it is located, no connector is needed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import data_api
from libica.openapi.v2.model.inline_view import InlineView
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)
    data_urn = "dataUrn_example" # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an URL for this data to use for inline view in a browser.
        api_response = api_instance.create_inline_view_url_for_data_without_project_context(data_urn)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DataApi->create_inline_view_url_for_data_without_project_context: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. |

### Return type

[**InlineView**](InlineView.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inline view URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data**
> Data get_data(data_urn)

Retrieve a data.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import data_api
from libica.openapi.v2.model.data import Data
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)
    data_urn = "dataUrn_example" # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a data.
        api_response = api_instance.get_data(data_urn)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DataApi->get_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. |

### Return type

[**Data**](Data.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

