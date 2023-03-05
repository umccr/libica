# libica.openapi.v2.EventLogApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /api/eventLog | Retrieve a list of event logs.


# **get_event_logs**
> EventLogList get_event_logs()

Retrieve a list of event logs.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import event_log_api
from libica.openapi.v2.model.event_log_list import EventLogList
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
    api_instance = event_log_api.EventLogApi(api_client)
    code = "code_example" # str | Code (optional)
    code_filter_type = "STARTS_WITH" # str | Code filter type (optional)
    category = "ERROR" # str | Category (optional)
    date_from = "dateFrom_example" # str | Date from. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    date_until = "dateUntil_example" # str | Date until. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    rows = 250 # int | Amount of rows to fetch. Maximum 250. Defaults to 250 (optional) if omitted the server will use the default value of 250

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of event logs.
        api_response = api_instance.get_event_logs(code=code, code_filter_type=code_filter_type, category=category, date_from=date_from, date_until=date_until, rows=rows)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code | [optional]
 **code_filter_type** | **str**| Code filter type | [optional]
 **category** | **str**| Category | [optional]
 **date_from** | **str**| Date from. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional]
 **date_until** | **str**| Date until. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional]
 **rows** | **int**| Amount of rows to fetch. Maximum 250. Defaults to 250 | [optional] if omitted the server will use the default value of 250

### Return type

[**EventLogList**](EventLogList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of event logs is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

