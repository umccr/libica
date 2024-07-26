# libica.openapi.v2.ProjectDataMoveBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_data_move_batch**](ProjectDataMoveBatchApi.md#create_project_data_move_batch) | **POST** /api/projects/{projectId}/dataMoveBatch | Create a project data move batch.
[**get_project_data_move_batch**](ProjectDataMoveBatchApi.md#get_project_data_move_batch) | **GET** /api/projects/{projectId}/dataMoveBatch/{batchId} | Retrieve a project data move batch.
[**get_project_data_move_batch_item**](ProjectDataMoveBatchApi.md#get_project_data_move_batch_item) | **GET** /api/projects/{projectId}/dataMoveBatch/{batchId}/items/{itemId} | Retrieve a project data move batch item.
[**get_project_data_move_batch_items**](ProjectDataMoveBatchApi.md#get_project_data_move_batch_items) | **POST** /api/projects/{projectId}/dataMoveBatch/{batchId}/items:search | Retrieve a list of project data move batch items.


# **create_project_data_move_batch**
> ProjectDataMoveBatch create_project_data_move_batch(project_id, create_project_data_move_batch)

Create a project data move batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_move_batch_api
from libica.openapi.v2.model.create_project_data_move_batch import CreateProjectDataMoveBatch
from libica.openapi.v2.model.project_data_move_batch import ProjectDataMoveBatch
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
    api_instance = project_data_move_batch_api.ProjectDataMoveBatchApi(api_client)
    project_id = "projectId_example" # str | The ID of the project to which the data will be moved
    create_project_data_move_batch = CreateProjectDataMoveBatch(
        items=[
            CreateProjectDataMoveBatchItem(
                data_id="data_id_example",
            ),
        ],
        destination_folder_id="destination_folder_id_example",
    ) # CreateProjectDataMoveBatch | 

    # example passing only required values which don't have defaults set
    try:
        # Create a project data move batch.
        api_response = api_instance.create_project_data_move_batch(project_id, create_project_data_move_batch)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataMoveBatchApi->create_project_data_move_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to which the data will be moved |
 **create_project_data_move_batch** | [**CreateProjectDataMoveBatch**](CreateProjectDataMoveBatch.md)|  |

### Return type

[**ProjectDataMoveBatch**](ProjectDataMoveBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The project data move batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_move_batch**
> ProjectDataMoveBatch get_project_data_move_batch(project_id, batch_id)

Retrieve a project data move batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_move_batch_api
from libica.openapi.v2.model.project_data_move_batch import ProjectDataMoveBatch
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
    api_instance = project_data_move_batch_api.ProjectDataMoveBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project data move batch.
        api_response = api_instance.get_project_data_move_batch(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataMoveBatchApi->get_project_data_move_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |

### Return type

[**ProjectDataMoveBatch**](ProjectDataMoveBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data move batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_move_batch_item**
> ProjectDataMoveBatchItem get_project_data_move_batch_item(project_id, batch_id, item_id)

Retrieve a project data move batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_move_batch_api
from libica.openapi.v2.model.project_data_move_batch_item import ProjectDataMoveBatchItem
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
    api_instance = project_data_move_batch_api.ProjectDataMoveBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project data move batch item.
        api_response = api_instance.get_project_data_move_batch_item(project_id, batch_id, item_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataMoveBatchApi->get_project_data_move_batch_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |
 **item_id** | **str**|  |

### Return type

[**ProjectDataMoveBatchItem**](ProjectDataMoveBatchItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data move batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_move_batch_items**
> ProjectDataMoveBatchItemPagedList get_project_data_move_batch_items(project_id, batch_id)

Retrieve a list of project data move batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_move_batch_api
from libica.openapi.v2.model.project_data_move_batch_item_query_parameters import ProjectDataMoveBatchItemQueryParameters
from libica.openapi.v2.model.project_data_move_batch_item_paged_list import ProjectDataMoveBatchItemPagedList
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
    api_instance = project_data_move_batch_api.ProjectDataMoveBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | 
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    project_data_move_batch_item_query_parameters = ProjectDataMoveBatchItemQueryParameters(
        status=[
            "QUEUED",
        ],
    ) # ProjectDataMoveBatchItemQueryParameters |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of project data move batch items.
        api_response = api_instance.get_project_data_move_batch_items(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataMoveBatchApi->get_project_data_move_batch_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of project data move batch items.
        api_response = api_instance.get_project_data_move_batch_items(project_id, batch_id, page_offset=page_offset, page_token=page_token, page_size=page_size, project_data_move_batch_item_query_parameters=project_data_move_batch_item_query_parameters)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataMoveBatchApi->get_project_data_move_batch_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**|  |
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]
 **project_data_move_batch_item_query_parameters** | [**ProjectDataMoveBatchItemQueryParameters**](ProjectDataMoveBatchItemQueryParameters.md)|  | [optional]

### Return type

[**ProjectDataMoveBatchItemPagedList**](ProjectDataMoveBatchItemPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project data move batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

