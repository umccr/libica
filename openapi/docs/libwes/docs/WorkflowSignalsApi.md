# libica.openapi.libwes.WorkflowSignalsApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fail_signal**](WorkflowSignalsApi.md#fail_signal) | **PATCH** /v1/workflows/signals/{signalId}:fail | Fail a workflow signal
[**get_signal**](WorkflowSignalsApi.md#get_signal) | **GET** /v1/workflows/signals/{signalId} | Get the details of a workflow signal
[**list_signals**](WorkflowSignalsApi.md#list_signals) | **GET** /v1/workflows/signals | Get a list of workflow signals
[**succeed_signal**](WorkflowSignalsApi.md#succeed_signal) | **PATCH** /v1/workflows/signals/{signalId}:succeed | Succeed a workflow signal


# **fail_signal**
> WorkflowSignal fail_signal(signal_id, body=body)

Fail a workflow signal

Responds to a pending workflow signal with a failure result.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libwes
from libica.openapi.libwes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libwes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libwes.WorkflowSignalsApi(api_client)
    signal_id = 'signal_id_example' # str | ID of the workflow signal
body = libica.openapi.libwes.FailWorkflowSignalRequest() # FailWorkflowSignalRequest |  (optional)

    try:
        # Fail a workflow signal
        api_response = api_instance.fail_signal(signal_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowSignalsApi->fail_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_id** | **str**| ID of the workflow signal | 
 **body** | [**FailWorkflowSignalRequest**](FailWorkflowSignalRequest.md)|  | [optional] 

### Return type

[**WorkflowSignal**](WorkflowSignal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the failed signal. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The signal with the specified ID was not found. |  -  |
**409** | The workflow signal is no longer active. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signal**
> WorkflowSignal get_signal(signal_id)

Get the details of a workflow signal

Gets the details of a workflow signal with a given ID.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libwes
from libica.openapi.libwes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libwes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libwes.WorkflowSignalsApi(api_client)
    signal_id = 'signal_id_example' # str | ID of the workflow signal

    try:
        # Get the details of a workflow signal
        api_response = api_instance.get_signal(signal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowSignalsApi->get_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_id** | **str**| ID of the workflow signal | 

### Return type

[**WorkflowSignal**](WorkflowSignal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the workflow signal. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The signal with the specified ID was not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signals**
> WorkflowSignalList list_signals(tenant_id=tenant_id, include=include, page_size=page_size, page_token=page_token, sort=sort)

Get a list of workflow signals

Gets a list of workflow signals.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libwes
from libica.openapi.libwes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libwes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libwes.WorkflowSignalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | ID of the tenant (optional)
include = ['include_example'] # list[str] | Comma-separated list of properties to include in the response (optional)
page_size = 10 # int | Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. (optional) (default to 10)
page_token = 'page_token_example' # str | Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. (optional)
sort = 'timeCreated asc' # str | Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending). (optional) (default to 'timeCreated asc')

    try:
        # Get a list of workflow signals
        api_response = api_instance.list_signals(tenant_id=tenant_id, include=include, page_size=page_size, page_token=page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowSignalsApi->list_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| ID of the tenant | [optional] 
 **include** | [**list[str]**](str.md)| Comma-separated list of properties to include in the response | [optional] 
 **page_size** | **int**| Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified. | [optional] [default to 10]
 **page_token** | **str**| Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified. | [optional] 
 **sort** | **str**| Specifies the order to include list items as \&quot;_{fieldName}_ [asc|desc]\&quot;. The second field is optional and specifies the sort direction (\&quot;asc\&quot; for ascending or \&quot;desc\&quot; for descending). | [optional] [default to &#39;timeCreated asc&#39;]

### Return type

[**WorkflowSignalList**](WorkflowSignalList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of workflow signals that the user has access to. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **succeed_signal**
> WorkflowSignal succeed_signal(signal_id, body=body)

Succeed a workflow signal

Responds to a pending workflow signal with a successful result.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libwes
from libica.openapi.libwes.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libwes.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libwes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libwes.WorkflowSignalsApi(api_client)
    signal_id = 'signal_id_example' # str | ID of the workflow signal
body = libica.openapi.libwes.SucceedWorkflowSignalRequest() # SucceedWorkflowSignalRequest |  (optional)

    try:
        # Succeed a workflow signal
        api_response = api_instance.succeed_signal(signal_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowSignalsApi->succeed_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_id** | **str**| ID of the workflow signal | 
 **body** | [**SucceedWorkflowSignalRequest**](SucceedWorkflowSignalRequest.md)|  | [optional] 

### Return type

[**WorkflowSignal**](WorkflowSignal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the succeeded signal. |  -  |
**400** | Invalid request. |  -  |
**401** | Unauthorized |  -  |
**403** | Permission denied. |  -  |
**404** | The signal with the specified ID was not found. |  -  |
**409** | The workflow signal is no longer active. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

