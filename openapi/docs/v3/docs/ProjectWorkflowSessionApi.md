# libica.openapi.v3.ProjectWorkflowSessionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_session_configurations**](ProjectWorkflowSessionApi.md#get_workflow_session_configurations) | **GET** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/configurations | Retrieve the configurations of a workflow session.
[**get_workflow_session_inputs**](ProjectWorkflowSessionApi.md#get_workflow_session_inputs) | **GET** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/inputs | Retrieve the inputs of a workflow session.
[**get_workflow_sessions**](ProjectWorkflowSessionApi.md#get_workflow_sessions) | **GET** /api/projects/{projectId}/workflowSessions | Retrieve the list of workflow sessions.
[**search_orchestrated_analyses**](ProjectWorkflowSessionApi.md#search_orchestrated_analyses) | **POST** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/analyses:search | Search analyses orchestrated by the workflow session.
[**search_workflow_sessions**](ProjectWorkflowSessionApi.md#search_workflow_sessions) | **POST** /api/projects/{projectId}/workflowSessions:search | Search workflow sessions.


# **get_workflow_session_configurations**
> WorkflowSessionConfigurationList get_workflow_session_configurations(project_id, workflow_session_id)

Retrieve the configurations of a workflow session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.workflow_session_configuration_list import WorkflowSessionConfigurationList
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
    api_instance = libica.openapi.v3.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    workflow_session_id = 'workflow_session_id_example' # str | The ID of the workflow session to retrieve the configuration for

    try:
        # Retrieve the configurations of a workflow session.
        api_response = api_instance.get_workflow_session_configurations(project_id, workflow_session_id)
        print("The response of ProjectWorkflowSessionApi->get_workflow_session_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workflow_session_id** | **str**| The ID of the workflow session to retrieve the configuration for | 

### Return type

[**WorkflowSessionConfigurationList**](WorkflowSessionConfigurationList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configurations of the workflow session are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_session_inputs**
> WorkflowSessionInputList get_workflow_session_inputs(project_id, workflow_session_id)

Retrieve the inputs of a workflow session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.workflow_session_input_list import WorkflowSessionInputList
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
    api_instance = libica.openapi.v3.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    workflow_session_id = 'workflow_session_id_example' # str | The ID of the workflow session to retrieve the inputs for

    try:
        # Retrieve the inputs of a workflow session.
        api_response = api_instance.get_workflow_session_inputs(project_id, workflow_session_id)
        print("The response of ProjectWorkflowSessionApi->get_workflow_session_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workflow_session_id** | **str**| The ID of the workflow session to retrieve the inputs for | 

### Return type

[**WorkflowSessionInputList**](WorkflowSessionInputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inputs of the workflow session are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_sessions**
> WorkflowSessionPagedListV3 get_workflow_sessions(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of workflow sessions.

This endpoint only returns V3 items. Use the search endpoint to get V4 items.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.workflow_session_paged_list_v3 import WorkflowSessionPagedListV3
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
    api_instance = libica.openapi.v3.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    reference = 'reference_example' # str | The reference to filter on. (optional)
    userreference = 'userreference_example' # str | The user-reference to filter on. (optional)
    status = 'status_example' # str | The status to filter on. (optional)
    usertag = 'usertag_example' # str | The user-tags to filter on. (optional)
    technicaltag = 'technicaltag_example' # str | The technical-tags to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  (optional)

    try:
        # Retrieve the list of workflow sessions.
        api_response = api_instance.get_workflow_sessions(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectWorkflowSessionApi->get_workflow_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **reference** | **str**| The reference to filter on. | [optional] 
 **userreference** | **str**| The user-reference to filter on. | [optional] 
 **status** | **str**| The status to filter on. | [optional] 
 **usertag** | **str**| The user-tags to filter on. | [optional] 
 **technicaltag** | **str**| The technical-tags to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  | [optional] 

### Return type

[**WorkflowSessionPagedListV3**](WorkflowSessionPagedListV3.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project workflow sessions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_orchestrated_analyses**
> WorkflowSessionAnalysisPagedListV4 search_orchestrated_analyses(project_id, workflow_session_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)

Search analyses orchestrated by the workflow session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_query_parameters import AnalysisQueryParameters
from libica.openapi.v3.models.workflow_session_analysis_paged_list_v4 import WorkflowSessionAnalysisPagedListV4
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
    api_instance = libica.openapi.v3.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    workflow_session_id = 'workflow_session_id_example' # str | 
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)
    analysis_query_parameters = libica.openapi.v3.AnalysisQueryParameters() # AnalysisQueryParameters |  (optional)

    try:
        # Search analyses orchestrated by the workflow session.
        api_response = api_instance.search_orchestrated_analyses(project_id, workflow_session_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)
        print("The response of ProjectWorkflowSessionApi->search_orchestrated_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->search_orchestrated_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workflow_session_id** | **str**|  | 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional] 
 **analysis_query_parameters** | [**AnalysisQueryParameters**](AnalysisQueryParameters.md)|  | [optional] 

### Return type

[**WorkflowSessionAnalysisPagedListV4**](WorkflowSessionAnalysisPagedListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of orchestrated analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_workflow_sessions**
> WorkflowSessionPagedListV4 search_workflow_sessions(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)

Search workflow sessions.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_query_parameters import AnalysisQueryParameters
from libica.openapi.v3.models.workflow_session_paged_list_v4 import WorkflowSessionPagedListV4
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
    api_instance = libica.openapi.v3.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  (optional)
    analysis_query_parameters = libica.openapi.v3.AnalysisQueryParameters() # AnalysisQueryParameters |  (optional)

    try:
        # Search workflow sessions.
        api_response = api_instance.search_workflow_sessions(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)
        print("The response of ProjectWorkflowSessionApi->search_workflow_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->search_workflow_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  | [optional] 
 **analysis_query_parameters** | [**AnalysisQueryParameters**](AnalysisQueryParameters.md)|  | [optional] 

### Return type

[**WorkflowSessionPagedListV4**](WorkflowSessionPagedListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project workflow sessions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

