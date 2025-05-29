# libica.openapi.v3.ProjectDataCopyBatchApi

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_project_data_copy_batch import CreateProjectDataCopyBatch
from libica.openapi.v3.models.project_data_copy_batch import ProjectDataCopyBatch
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
    api_instance = libica.openapi.v3.ProjectDataCopyBatchApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project to which the data will be copied
    create_project_data_copy_batch = libica.openapi.v3.CreateProjectDataCopyBatch() # CreateProjectDataCopyBatch | 

    try:
        # Create a project data copy batch.
        api_response = api_instance.create_project_data_copy_batch(project_id, create_project_data_copy_batch)
        print("The response of ProjectDataCopyBatchApi->create_project_data_copy_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataCopyBatchApi->create_project_data_copy_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to which the data will be copied | 
 **create_project_data_copy_batch** | [**CreateProjectDataCopyBatch**](CreateProjectDataCopyBatch.md)|  | 

### Return type

[**ProjectDataCopyBatch**](ProjectDataCopyBatch.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_copy_batch import ProjectDataCopyBatch
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
    api_instance = libica.openapi.v3.ProjectDataCopyBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | 

    try:
        # Retrieve a project data copy batch.
        api_response = api_instance.get_project_data_copy_batch(project_id, batch_id)
        print("The response of ProjectDataCopyBatchApi->get_project_data_copy_batch:\n")
        pprint(api_response)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_copy_batch_item import ProjectDataCopyBatchItem
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
    api_instance = libica.openapi.v3.ProjectDataCopyBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | 
    item_id = 'item_id_example' # str | 

    try:
        # Retrieve a project data copy batch item.
        api_response = api_instance.get_project_data_copy_batch_item(project_id, batch_id, item_id)
        print("The response of ProjectDataCopyBatchApi->get_project_data_copy_batch_item:\n")
        pprint(api_response)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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
> ProjectDataCopyBatchItemPagedList get_project_data_copy_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size)

Retrieve a list of project data copy batch items.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_copy_batch_item_paged_list import ProjectDataCopyBatchItemPagedList
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
    api_instance = libica.openapi.v3.ProjectDataCopyBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | 
    status = ['status_example'] # List[str] | The statuses to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    try:
        # Retrieve a list of project data copy batch items.
        api_response = api_instance.get_project_data_copy_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size)
        print("The response of ProjectDataCopyBatchApi->get_project_data_copy_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataCopyBatchApi->get_project_data_copy_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**|  | 
 **status** | [**List[str]**](str.md)| The statuses to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 

### Return type

[**ProjectDataCopyBatchItemPagedList**](ProjectDataCopyBatchItemPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project data copy batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

