# libiap.openapi.libtes.TasksApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /v1/tasks | Create a Task
[**get_task**](TasksApi.md#get_task) | **GET** /v1/tasks/{taskId} | Get the details of a Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /v1/tasks | Get a list of tasks
[**update_task**](TasksApi.md#update_task) | **PATCH** /v1/tasks/{taskId} | Update an existing task.


# **create_task**
> Task create_task(body=body)

Create a Task

Creates a task. Returns the ID associated with the new task. Also returns the task version ID associated with the new task, if provided. Substitutions can be defined in the following format: \"{{string}}\", and specified at launch time.

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
    api_instance = libiap.openapi.libtes.TasksApi(api_client)
    body = libiap.openapi.libtes.CreateTaskRequest() # CreateTaskRequest |  (optional)

    try:
        # Create a Task
        api_response = api_instance.create_task(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskRequest**](CreateTaskRequest.md)|  | [optional] 

### Return type

[**Task**](Task.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskSummary get_task(task_id)

Get the details of a Task

Gets the details of a Task for a given task ID.

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
    api_instance = libiap.openapi.libtes.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get the details of a Task
        api_response = api_instance.get_task(task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**TaskSummary**](TaskSummary.md)

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

# **list_tasks**
> TaskSummaryPagedItems list_tasks(names=names, acls=acls, page_size=page_size, sort=sort, page_token=page_token)

Get a list of tasks

Gets a list of tasks accessible by the current tenant ID.

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
    api_instance = libiap.openapi.libtes.TasksApi(api_client)
    names = 'names_example' # str | Name: Optional parameter to filter the returned list. Case-Sensitive (optional)
acls = 'acls_example' # str | Name: Optional parameter to filter the returned list. Case-Sensitive (optional)
page_size = 10 # int | Optional parameter to define the page size returned. Valid inputs range from 1-1000. (optional) (default to 10)
sort = 'timeCreated asc' # str | Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) (optional) (default to 'timeCreated asc')
page_token = 'page_token_example' # str | pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) (optional)

    try:
        # Get a list of tasks
        api_response = api_instance.list_tasks(names=names, acls=acls, page_size=page_size, sort=sort, page_token=page_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **str**| Name: Optional parameter to filter the returned list. Case-Sensitive | [optional] 
 **acls** | **str**| Name: Optional parameter to filter the returned list. Case-Sensitive | [optional] 
 **page_size** | **int**| Optional parameter to define the page size returned. Valid inputs range from 1-1000. | [optional] [default to 10]
 **sort** | **str**| Sort: Optional parameter to set the sort of the returned list. Valid fields include: name, timeCreated, timeModified.  The sort can be specified as asc or desc. (Default: asc.) | [optional] [default to &#39;timeCreated asc&#39;]
 **page_token** | **str**| pageToken: Optional parameter for navigation after initial listing. Valid values include firstPageToken,  nextPageToken, and previousPageToken (provided in the list response) | [optional] 

### Return type

[**TaskSummaryPagedItems**](TaskSummaryPagedItems.md)

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

# **update_task**
> Task update_task(task_id, body=body)

Update an existing task.

Updates the task with a given ID. The task's name, description can be updated. The task's name must remain unique.

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
    api_instance = libiap.openapi.libtes.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
body = libiap.openapi.libtes.UpdateTaskRequest() # UpdateTaskRequest | Details of the task to be updated. (optional)

    try:
        # Update an existing task.
        api_response = api_instance.update_task(task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **body** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| Details of the task to be updated. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

