# libica.openapi.v2.ProjectBaseTableApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_base_tables**](ProjectBaseTableApi.md#get_base_tables) | **GET** /api/projects/{projectId}/base/tables | Retrieve a liste of base tables.
[**load_data**](ProjectBaseTableApi.md#load_data) | **POST** /api/projects/{projectId}/base/tables/{tableId}:loadData | Load data in a base table.


# **get_base_tables**
> ProjectBaseTableList get_base_tables(project_id)

Retrieve a liste of base tables.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_base_table_api
from libica.openapi.v2.model.project_base_table_list import ProjectBaseTableList
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
    api_instance = project_base_table_api.ProjectBaseTableApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a liste of base tables.
        api_response = api_instance.get_base_tables(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectBaseTableApi->get_base_tables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectBaseTableList**](ProjectBaseTableList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of base tables is successfully retrieved |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_data**
> BaseJob load_data(project_id, table_id)

Load data in a base table.

Load data in the specified table

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_base_table_api
from libica.openapi.v2.model.base_job import BaseJob
from libica.openapi.v2.model.load_data_in_base_request import LoadDataInBaseRequest
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
    api_instance = project_base_table_api.ProjectBaseTableApi(api_client)
    project_id = "projectId_example" # str | 
    table_id = "tableId_example" # str | 
    load_data_in_base_request = LoadDataInBaseRequest(
        allow_jagged_rows=False,
        allow_quoted_newlines=False,
        data_id="data_id_example",
        delimiter=",",
        encoding="UTF8",
        force_load=False,
        header_rows_to_skip=1,
        ignore_unknown_values=False,
        include_references=True,
        include_data_reference=True,
        include_sample_reference=True,
        include_pipeline_reference=True,
        include_pipeline_execution_reference=True,
        include_tenant_reference=True,
        null_marker="null_marker_example",
        number_of_errors_allowed=0,
        quote="quote_example",
        write_preference="APPENDTOTABLE",
    ) # LoadDataInBaseRequest | Load data request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Load data in a base table.
        api_response = api_instance.load_data(project_id, table_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectBaseTableApi->load_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Load data in a base table.
        api_response = api_instance.load_data(project_id, table_id, load_data_in_base_request=load_data_in_base_request)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectBaseTableApi->load_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **table_id** | **str**|  |
 **load_data_in_base_request** | [**LoadDataInBaseRequest**](LoadDataInBaseRequest.md)| Load data request | [optional]

### Return type

[**BaseJob**](BaseJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Base job to load data is created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

