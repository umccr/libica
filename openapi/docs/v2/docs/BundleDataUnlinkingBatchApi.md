# libica.openapi.v2.BundleDataUnlinkingBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle_data_unlinking_batch**](BundleDataUnlinkingBatchApi.md#create_bundle_data_unlinking_batch) | **POST** /api/bundles/{bundleId}/dataUnlinkingBatch | Create a bundle data unlinking batch.
[**get_bundle_data_unlinking_batch**](BundleDataUnlinkingBatchApi.md#get_bundle_data_unlinking_batch) | **GET** /api/bundles/{bundleId}/dataUnlinkingBatch/{batchId} | Retrieve a bundle data unlinking batch.
[**get_bundle_data_unlinking_batch_item**](BundleDataUnlinkingBatchApi.md#get_bundle_data_unlinking_batch_item) | **GET** /api/bundles/{bundleId}/dataUnlinkingBatch/{batchId}/items/{itemId} | Retrieve a bundle data unlinking batch item.
[**get_bundle_data_unlinking_batch_items**](BundleDataUnlinkingBatchApi.md#get_bundle_data_unlinking_batch_items) | **GET** /api/bundles/{bundleId}/dataUnlinkingBatch/{batchId}/items | Retrieve a list of bundle data unlinking batch items.


# **create_bundle_data_unlinking_batch**
> BundleDataUnlinkingBatch create_bundle_data_unlinking_batch(bundle_id, create_bundle_data_unlinking_batch)

Create a bundle data unlinking batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_unlinking_batch_api
from libica.openapi.v2.model.create_bundle_data_unlinking_batch import CreateBundleDataUnlinkingBatch
from libica.openapi.v2.model.bundle_data_unlinking_batch import BundleDataUnlinkingBatch
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
    api_instance = bundle_data_unlinking_batch_api.BundleDataUnlinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    create_bundle_data_unlinking_batch = CreateBundleDataUnlinkingBatch(
        items=[
            CreateBundleDataUnlinkingBatchItem(
                data_id="data_id_example",
            ),
        ],
    ) # CreateBundleDataUnlinkingBatch | 

    # example passing only required values which don't have defaults set
    try:
        # Create a bundle data unlinking batch.
        api_response = api_instance.create_bundle_data_unlinking_batch(bundle_id, create_bundle_data_unlinking_batch)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataUnlinkingBatchApi->create_bundle_data_unlinking_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **create_bundle_data_unlinking_batch** | [**CreateBundleDataUnlinkingBatch**](CreateBundleDataUnlinkingBatch.md)|  |

### Return type

[**BundleDataUnlinkingBatch**](BundleDataUnlinkingBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The bundle data unlinking batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_unlinking_batch**
> BundleDataUnlinkingBatch get_bundle_data_unlinking_batch(bundle_id, batch_id)

Retrieve a bundle data unlinking batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_unlinking_batch_api
from libica.openapi.v2.model.bundle_data_unlinking_batch import BundleDataUnlinkingBatch
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
    api_instance = bundle_data_unlinking_batch_api.BundleDataUnlinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bundle data unlinking batch.
        api_response = api_instance.get_bundle_data_unlinking_batch(bundle_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataUnlinkingBatchApi->get_bundle_data_unlinking_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **batch_id** | **str**|  |

### Return type

[**BundleDataUnlinkingBatch**](BundleDataUnlinkingBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle data unlinking batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_unlinking_batch_item**
> BundleDataUnlinkingBatchItem get_bundle_data_unlinking_batch_item(bundle_id, batch_id, item_id)

Retrieve a bundle data unlinking batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_unlinking_batch_api
from libica.openapi.v2.model.bundle_data_unlinking_batch_item import BundleDataUnlinkingBatchItem
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
    api_instance = bundle_data_unlinking_batch_api.BundleDataUnlinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bundle data unlinking batch item.
        api_response = api_instance.get_bundle_data_unlinking_batch_item(bundle_id, batch_id, item_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataUnlinkingBatchApi->get_bundle_data_unlinking_batch_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **batch_id** | **str**|  |
 **item_id** | **str**|  |

### Return type

[**BundleDataUnlinkingBatchItem**](BundleDataUnlinkingBatchItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle data unlinking batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_data_unlinking_batch_items**
> BundleDataUnlinkingBatchItemPagedList get_bundle_data_unlinking_batch_items(bundle_id, batch_id)

Retrieve a list of bundle data unlinking batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_unlinking_batch_api
from libica.openapi.v2.model.bundle_data_unlinking_batch_item_paged_list import BundleDataUnlinkingBatchItemPagedList
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
    api_instance = bundle_data_unlinking_batch_api.BundleDataUnlinkingBatchApi(api_client)
    bundle_id = "bundleId_example" # str | 
    batch_id = "batchId_example" # str | 
    status = [
        "INITIALISED",
    ] # [str] | The statuses to filter on. (optional)
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = "sort_example" # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of bundle data unlinking batch items.
        api_response = api_instance.get_bundle_data_unlinking_batch_items(bundle_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataUnlinkingBatchApi->get_bundle_data_unlinking_batch_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of bundle data unlinking batch items.
        api_response = api_instance.get_bundle_data_unlinking_batch_items(bundle_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataUnlinkingBatchApi->get_bundle_data_unlinking_batch_items: %s\n" % e)
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
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot; | [optional]

### Return type

[**BundleDataUnlinkingBatchItemPagedList**](BundleDataUnlinkingBatchItemPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle data unlinking batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

