# libica.openapi.libgds.JobsApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_job**](JobsApi.md#abort_job) | **POST** /v1/jobs/{jobId}:abort | Abort a job in GDS.
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{jobId} | Get information about a job in GDS.
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /v1/jobs | Get a list of jobs for a given folder


# **abort_job**
> JobResponse abort_job(job_id)

Abort a job in GDS.

Abort the specified job ID.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.JobsApi(api_client)
    job_id = 'job_id_example' # str | Unique identifier for the job to be aborted.

    try:
        # Abort a job in GDS.
        api_response = api_instance.abort_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->abort_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique identifier for the job to be aborted. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Job not found. |  -  |
**409** | Conflict. |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobResponse get_job(job_id, tenant_id=tenant_id, include_errors=include_errors)

Get information about a job in GDS.

Get information for the specified job ID.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.JobsApi(api_client)
    job_id = 'job_id_example' # str | Unique identifier for the job to retrieve.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
include_errors = True # bool |  (optional)

    try:
        # Get information about a job in GDS.
        api_response = api_instance.get_job(job_id, tenant_id=tenant_id, include_errors=include_errors)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique identifier for the job to retrieve. | 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **include_errors** | **bool**|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Job not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobListResponse list_jobs(folder_id, job_statuses=job_statuses, page_size=page_size, page_token=page_token, include=include)

Get a list of jobs for a given folder

Given a folder id, get a list of jobs accessible by the JWT. The default sort returned is by job progress status. The default page size is 10 items

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.JobsApi(api_client)
    folder_id = 'folder_id_example' # str | 
job_statuses = 'job_statuses_example' # str | Optional field that specifies comma-separated JobStatuses to include in the list (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl (optional)

    try:
        # Get a list of jobs for a given folder
        api_response = api_instance.list_jobs(folder_id, job_statuses=job_statuses, page_size=page_size, page_token=page_token, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **job_statuses** | **str**| Optional field that specifies comma-separated JobStatuses to include in the list | [optional] 
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **include** | **str**| Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl | [optional] 

### Return type

[**JobListResponse**](JobListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

