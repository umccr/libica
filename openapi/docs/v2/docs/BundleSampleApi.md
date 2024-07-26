# libica.openapi.v2.BundleSampleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_samples**](BundleSampleApi.md#get_bundle_samples) | **GET** /api/bundles/{bundleId}/samples | Retrieve a list of bundle samples.
[**link_sample_to_bundle**](BundleSampleApi.md#link_sample_to_bundle) | **POST** /api/bundles/{bundleId}/samples/{sampleId} | Link a sample to a bundle.
[**unlink_sample_from_bundle**](BundleSampleApi.md#unlink_sample_from_bundle) | **DELETE** /api/bundles/{bundleId}/samples/{sampleId} | Unlink a sample from a bundle.


# **get_bundle_samples**
> BundleSamplePagedList get_bundle_samples(bundle_id)

Retrieve a list of bundle samples.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_sample_api
from libica.openapi.v2.model.bundle_sample_paged_list import BundleSamplePagedList
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
    api_instance = bundle_sample_api.BundleSampleApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to get bundle samples from
    search = "search_example" # str | To search through multiple fields of data. (optional)
    user_tags = "userTags_example" # str | The user tags to filter on. (optional)
    technical_tags = "technicalTags_example" # str | The technical tags to filter on. (optional)
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = "sort_example" # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\" The attributes for which sorting is supported: - timeCreated - timeModified - name - description - metadataValid - status (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of bundle samples.
        api_response = api_instance.get_bundle_samples(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleSampleApi->get_bundle_samples: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of bundle samples.
        api_response = api_instance.get_bundle_samples(bundle_id, search=search, user_tags=user_tags, technical_tags=technical_tags, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleSampleApi->get_bundle_samples: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to get bundle samples from |
 **search** | **str**| To search through multiple fields of data. | [optional]
 **user_tags** | **str**| The user tags to filter on. | [optional]
 **technical_tags** | **str**| The technical tags to filter on. | [optional]
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot; The attributes for which sorting is supported: - timeCreated - timeModified - name - description - metadataValid - status | [optional]

### Return type

[**BundleSamplePagedList**](BundleSamplePagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle samples are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_sample_to_bundle**
> link_sample_to_bundle(bundle_id, sample_id)

Link a sample to a bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_sample_api
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
    api_instance = bundle_sample_api.BundleSampleApi(api_client)
    bundle_id = "bundleId_example" # str | 
    sample_id = "sampleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Link a sample to a bundle.
        api_instance.link_sample_to_bundle(bundle_id, sample_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleSampleApi->link_sample_to_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **sample_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The sample is successfully linked to the bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_sample_from_bundle**
> unlink_sample_from_bundle(bundle_id, sample_id)

Unlink a sample from a bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_sample_api
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
    api_instance = bundle_sample_api.BundleSampleApi(api_client)
    bundle_id = "bundleId_example" # str | 
    sample_id = "sampleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink a sample from a bundle.
        api_instance.unlink_sample_from_bundle(bundle_id, sample_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleSampleApi->unlink_sample_from_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **sample_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The sample is successfully unlinked from the bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

