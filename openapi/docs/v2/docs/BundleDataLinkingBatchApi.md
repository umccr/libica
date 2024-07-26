# libica.openapi.v2.BundleDataLinkingBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle_data_linking_batch**](BundleDataLinkingBatchApi.md#create_bundle_data_linking_batch) | **POST** /api/bundles/{bundleId}/dataLinkingBatch | Create a bundle data linking batch.
[**get_bundle_data_linking_batch**](BundleDataLinkingBatchApi.md#get_bundle_data_linking_batch) | **GET** /api/bundles/{bundleId}/dataLinkingBatch/{batchId} | Retrieve a bundle data linking batch.
[**get_bundle_data_linking_batch_item**](BundleDataLinkingBatchApi.md#get_bundle_data_linking_batch_item) | **GET** /api/bundles/{bundleId}/dataLinkingBatch/{batchId}/items/{itemId} | Retrieve a bundle data linking batch item.
[**get_bundle_data_linking_batch_items**](BundleDataLinkingBatchApi.md#get_bundle_data_linking_batch_items) | **GET** /api/bundles/{bundleId}/dataLinkingBatch/{batchId}/items | Retrieve a list of bundle data linking batch items.


# **create_bundle_data_linking_batch**
> BundleDataLinkingBatch create_bundle_data_linking_batch(bundle_id, create_bundle_data_linking_batch)

Create a bundle data linking batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_linking_batch_api
from libica.openapi.v2.model.create_bundle_data_linking_batch import CreateBundleDataLinkingBatch
from libica.openapi.v2.model.bundle_data_linking_batch import BundleDataLinkingBatch
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
    api_instance = bundle_data_linking_batch_api.BundleDataLinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    create_bundle_data_linking_batch = CreateBundleDataLinkingBatch(
        items=[
            CreateBundleDataLinkingBatchItem(
                data_id="data_id_example",
            ),
        ],
    ) # CreateBundleDataLinkingBatch | 

    # example passing only required values which don't have defaults set
    try:
        # Create a bundle data linking batch.
        api_response = api_instance.create_bundle_data_linking_batch(bundle_id, create_bundle_data_linking_batch)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataLinkingBatchApi->create_bundle_data_linking_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **create_bundle_data_linking_batch** | [**CreateBundleDataLinkingBatch**](CreateBundleDataLinkingBatch.md)|  |

### Return type

[**BundleDataLinkingBatch**](BundleDataLinkingBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The bundle data linking batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_linking_batch**
> BundleDataLinkingBatch get_bundle_data_linking_batch(bundle_id, batch_id)

Retrieve a bundle data linking batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_linking_batch_api
from libica.openapi.v2.model.bundle_data_linking_batch import BundleDataLinkingBatch
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
    api_instance = bundle_data_linking_batch_api.BundleDataLinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bundle data linking batch.
        api_response = api_instance.get_bundle_data_linking_batch(bundle_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataLinkingBatchApi->get_bundle_data_linking_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **batch_id** | **str**|  |

### Return type

[**BundleDataLinkingBatch**](BundleDataLinkingBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle data linking batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_linking_batch_item**
> BundleDataLinkingBatchItem get_bundle_data_linking_batch_item(bundle_id, batch_id, item_id)

Retrieve a bundle data linking batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_linking_batch_api
from libica.openapi.v2.model.bundle_data_linking_batch_item import BundleDataLinkingBatchItem
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
    api_instance = bundle_data_linking_batch_api.BundleDataLinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bundle data linking batch item.
        api_response = api_instance.get_bundle_data_linking_batch_item(bundle_id, batch_id, item_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataLinkingBatchApi->get_bundle_data_linking_batch_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **batch_id** | **str**|  |
 **item_id** | **str**|  |

### Return type

[**BundleDataLinkingBatchItem**](BundleDataLinkingBatchItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle data linking batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_linking_batch_items**
> BundleDataLinkingBatchItemPagedList get_bundle_data_linking_batch_items(bundle_id, batch_id)

Retrieve a list of bundle data linking batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_linking_batch_api
from libica.openapi.v2.model.bundle_data_linking_batch_item_paged_list import BundleDataLinkingBatchItemPagedList
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
    api_instance = bundle_data_linking_batch_api.BundleDataLinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 
    status = [
        "INITIALISED",
    ] # [str] | The statuses to filter on. (optional)
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of bundle data linking batch items.
        api_response = api_instance.get_bundle_data_linking_batch_items(bundle_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataLinkingBatchApi->get_bundle_data_linking_batch_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of bundle data linking batch items.
        api_response = api_instance.get_bundle_data_linking_batch_items(bundle_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataLinkingBatchApi->get_bundle_data_linking_batch_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **batch_id** | **str**|  |
 **status** | **[str]**| The statuses to filter on. | [optional]
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]

### Return type

[**BundleDataLinkingBatchItemPagedList**](BundleDataLinkingBatchItemPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle data linking batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

