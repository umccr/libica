# libiap.openapi.libtes.TaskRunsApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_task_run**](TaskRunsApi.md#abort_task_run) | **PUT** /v1/tasks/runs/{runId}:abort | Abort a task run
[**create_task_run**](TaskRunsApi.md#create_task_run) | **POST** /v1/tasks/runs | Create and launch a task run
[**get_task_run**](TaskRunsApi.md#get_task_run) | **GET** /v1/tasks/runs/{runId} | Get the status of a task run
[**list_task_runs**](TaskRunsApi.md#list_task_runs) | **GET** /v1/tasks/runs | Get a list of task runs


# **abort_task_run**
> TaskRunSummary abort_task_run(run_id)

Abort a task run

Aborts a task run for a given task run ID. The task run is required to have a status of \"Pending\" or \"Running\".

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libtes
from libiap.openapi.libtes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libtes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libtes.TaskRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Abort a task run
        api_response = api_instance.abort_task_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskRunsApi->abort_task_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 

### Return type

[**TaskRunSummary**](TaskRunSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_run**
> TaskRun create_task_run(body=body)

Create and launch a task run

Creates and launches a task run. Returns the ID and status associated with the new task run.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libtes
from libiap.openapi.libtes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libtes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libtes.TaskRunsApi(api_client)
    body = libiap.openapi.libtes.CreateTaskRunRequest() # CreateTaskRunRequest |  (optional)

    try:
        # Create and launch a task run
        api_response = api_instance.create_task_run(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskRunsApi->create_task_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskRunRequest**](CreateTaskRunRequest.md)|  | [optional] 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_run**
> TaskRun get_task_run(run_id)

Get the status of a task run

Gets the status of a task run for a given task run ID.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libtes
from libiap.openapi.libtes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libtes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libtes.TaskRunsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Get the status of a task run
        api_response = api_instance.get_task_run(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskRunsApi->get_task_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_runs**
> TaskRunSummaryPagedItems list_task_runs(sort=sort, names=names, status=status, versions=versions, acls=acls, page_size=page_size, page_token=page_token)

Get a list of task runs

Get a list of task runs accessible by the current tenant ID.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libtes
from libiap.openapi.libtes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libtes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libtes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libtes.TaskRunsApi(api_client)
    sort = 'sort_example' # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, status, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional)
names = 'names_example' # str |  (optional)
status = 'status_example' # str |  (optional)
versions = 'versions_example' # str |  (optional)
acls = 'acls_example' # str |  (optional)
page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) (default to 10)
page_token = 'page_token_example' # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    try:
        # Get a list of task runs
        api_response = api_instance.list_task_runs(sort=sort, names=names, status=status, versions=versions, acls=acls, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskRunsApi->list_task_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, status, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) | [optional] 
 **names** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **versions** | **str**|  | [optional] 
 **acls** | **str**|  | [optional] 
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] [default to 10]
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional] 

### Return type

[**TaskRunSummaryPagedItems**](TaskRunSummaryPagedItems.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

