# libica.openapi.v2.ProjectDataCopyBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_data_copy_batch**](ProjectDataCopyBatchApi.md#create_project_data_copy_batch) | **POST** /api/projects/{projectId}/dataCopyBatch | Create a project data copy batch.
[**get_project_data_copy_batch**](ProjectDataCopyBatchApi.md#get_project_data_copy_batch) | **GET** /api/projects/{projectId}/dataCopyBatch/{batchId} | Retrieve a project data copy batch.
[**get_project_data_copy_batch_item**](ProjectDataCopyBatchApi.md#get_project_data_copy_batch_item) | **GET** /api/projects/{projectId}/dataCopyBatch/{batchId}/items/{itemId} | Retrieve a project data copy batch item.
[**get_project_data_copy_batch_items**](ProjectDataCopyBatchApi.md#get_project_data_copy_batch_items) | **GET** /api/projects/{projectId}/dataCopyBatch/{batchId}/items | Retrieve a list of project data copy batch items.


# **create_project_data_copy_batch**
> ProjectDataCopyBatch create_project_data_copy_batch(project_id, create_project_data_copy_batch)

Create a project data copy batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_copy_batch_api
from libica.openapi.v2.model.project_data_copy_batch import ProjectDataCopyBatch
from libica.openapi.v2.model.create_project_data_copy_batch import CreateProjectDataCopyBatch
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
    api_instance = project_data_copy_batch_api.ProjectDataCopyBatchApi(api_client)
    project_id = "projectId_example" # str | 
    create_project_data_copy_batch = CreateProjectDataCopyBatch(
        items=[
            CreateProjectDataCopyBatchItem(
                data_id="data_id_example",
            ),
        ],
        destination_folder_id="destination_folder_id_example",
        copy_user_tags=True,
        copy_technical_tags=True,
        copy_instrument_info=True,
        action_on_exist="RENAM",
    ) # CreateProjectDataCopyBatch | 

    # example passing only required values which don't have defaults set
    try:
        # Create a project data copy batch.
        api_response = api_instance.create_project_data_copy_batch(project_id, create_project_data_copy_batch)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataCopyBatchApi->create_project_data_copy_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_project_data_copy_batch** | [**CreateProjectDataCopyBatch**](CreateProjectDataCopyBatch.md)|  |

### Return type

[**ProjectDataCopyBatch**](ProjectDataCopyBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The project data copy batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_copy_batch**
> ProjectDataCopyBatch get_project_data_copy_batch(project_id, batch_id)

Retrieve a project data copy batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_copy_batch_api
from libica.openapi.v2.model.project_data_copy_batch import ProjectDataCopyBatch
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
    api_instance = project_data_copy_batch_api.ProjectDataCopyBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project data copy batch.
        api_response = api_instance.get_project_data_copy_batch(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataCopyBatchApi->get_project_data_copy_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |

### Return type

[**ProjectDataCopyBatch**](ProjectDataCopyBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data copy batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_copy_batch_item**
> ProjectDataCopyBatchItem get_project_data_copy_batch_item(project_id, batch_id, item_id)

Retrieve a project data copy batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_copy_batch_api
from libica.openapi.v2.model.project_data_copy_batch_item import ProjectDataCopyBatchItem
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
    api_instance = project_data_copy_batch_api.ProjectDataCopyBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project data copy batch item.
        api_response = api_instance.get_project_data_copy_batch_item(project_id, batch_id, item_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataCopyBatchApi->get_project_data_copy_batch_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |
 **item_id** | **str**|  |

### Return type

[**ProjectDataCopyBatchItem**](ProjectDataCopyBatchItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data copy batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_copy_batch_items**
> ProjectDataCopyBatchItemPagedList get_project_data_copy_batch_items(project_id, batch_id)

Retrieve a list of project data copy batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_copy_batch_api
from libica.openapi.v2.model.project_data_copy_batch_item_paged_list import ProjectDataCopyBatchItemPagedList
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
    api_instance = project_data_copy_batch_api.ProjectDataCopyBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 
    status = [
        "QUEUED",
    ] # [str] | The statuses to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of project data copy batch items.
        api_response = api_instance.get_project_data_copy_batch_items(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataCopyBatchApi->get_project_data_copy_batch_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of project data copy batch items.
        api_response = api_instance.get_project_data_copy_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataCopyBatchApi->get_project_data_copy_batch_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |
 **status** | **[str]**| The statuses to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot; | [optional]

### Return type

[**ProjectDataCopyBatchItemPagedList**](ProjectDataCopyBatchItemPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project data copy batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

