# libica.openapi.v3.DataApi

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.download import Download
from libica.openapi.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v3.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v3.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.v3.DataApi(api_client)
    data_urn = 'data_urn_example' # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    try:
        # Retrieve a download URL for this data.
        api_response = api_instance.create_download_url_for_data_without_project_context(data_urn)
        print("The response of DataApi->create_download_url_for_data_without_project_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->create_download_url_for_data_without_project_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. | 

### Return type

[**Download**](Download.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.inline_view import InlineView
from libica.openapi.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v3.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v3.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.v3.DataApi(api_client)
    data_urn = 'data_urn_example' # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    try:
        # Retrieve an URL for this data to use for inline view in a browser.
        api_response = api_instance.create_inline_view_url_for_data_without_project_context(data_urn)
        print("The response of DataApi->create_inline_view_url_for_data_without_project_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->create_inline_view_url_for_data_without_project_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. | 

### Return type

[**InlineView**](InlineView.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.data import Data
from libica.openapi.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v3.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v3.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.v3.DataApi(api_client)
    data_urn = 'data_urn_example' # str | The format is urn:ilmn:ica:region:\\<ID of the region\\>:data:\\<ID of the data\\>#\\<optional data path\\>. The path can be omitted, in that case the hashtag (#) must also be omitted.

    try:
        # Retrieve a data.
        api_response = api_instance.get_data(data_urn)
        print("The response of DataApi->get_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->get_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_urn** | **str**| The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. | 

### Return type

[**Data**](Data.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

