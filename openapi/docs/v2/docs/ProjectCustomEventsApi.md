# libica.openapi.v2.ProjectCustomEventsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_event**](ProjectCustomEventsApi.md#create_custom_event) | **POST** /api/projects/{projectId}/customEvents | Create a new custom event.


# **create_custom_event**
> create_custom_event(project_id, create_custom_event)

Create a new custom event.

Warning: this endpoint allows to create custom events with a code larger than 20 characters (max 50), but the endpoint for creating a custom notification subscription (POST /api/projects/{projectId}/customNotificationSubscriptions) only accepts event codes up to 20 characters.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_events_api
from libica.openapi.v2.model.create_custom_event import CreateCustomEvent
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
    api_instance = project_custom_events_api.ProjectCustomEventsApi(api_client)
    project_id = "projectId_example" # str | 
    create_custom_event = CreateCustomEvent(
        code="code_example",
        content={},
    ) # CreateCustomEvent | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new custom event.
        api_instance.create_custom_event(project_id, create_custom_event)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomEventsApi->create_custom_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_custom_event** | [**CreateCustomEvent**](CreateCustomEvent.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The event is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

