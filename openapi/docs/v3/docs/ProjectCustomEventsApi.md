# libica.openapi.v3.ProjectCustomEventsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_event**](ProjectCustomEventsApi.md#create_custom_event) | **POST** /api/projects/{projectId}/customEvents | Create a new custom event.


# **create_custom_event**
> create_custom_event(project_id, create_custom_event)

Create a new custom event.

Warning: this endpoint allows to create custom events with a code larger than 20 characters (max 50), but the endpoint for creating a custom notification subscription (POST /api/projects/{projectId}/customNotificationSubscriptions) only accepts event codes up to 20 characters.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_custom_event import CreateCustomEvent
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
    api_instance = libica.openapi.v3.ProjectCustomEventsApi(api_client)
    project_id = 'project_id_example' # str | 
    create_custom_event = libica.openapi.v3.CreateCustomEvent() # CreateCustomEvent | 

    try:
        # Create a new custom event.
        api_instance.create_custom_event(project_id, create_custom_event)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The event is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

