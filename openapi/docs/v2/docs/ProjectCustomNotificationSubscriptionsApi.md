# libica.openapi.v2.ProjectCustomNotificationSubscriptionsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#create_notification_subscription) | **POST** /api/projects/{projectId}/customNotificationSubscriptions | Create a custom notification subscription
[**delete_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#delete_notification_subscription) | **DELETE** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Delete a custom notification subscription
[**get_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#get_notification_subscription) | **GET** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Retrieve a notification subscription
[**get_notification_subscriptions**](ProjectCustomNotificationSubscriptionsApi.md#get_notification_subscriptions) | **GET** /api/projects/{projectId}/customNotificationSubscriptions | Retrieve notification subscriptions
[**update_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#update_notification_subscription) | **PUT** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Update a notification subscription


# **create_notification_subscription**
> CustomNotificationSubscription create_notification_subscription(project_id, create_custom_notification_subscription)

Create a custom notification subscription

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_notification_subscriptions_api
from libica.openapi.v2.model.custom_notification_subscription import CustomNotificationSubscription
from libica.openapi.v2.model.create_custom_notification_subscription import CreateCustomNotificationSubscription
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
    api_instance = project_custom_notification_subscriptions_api.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = "projectId_example" # str | 
    create_custom_notification_subscription = CreateCustomNotificationSubscription(
        custom_event_code="custom_event_code_example",
        filter_expression="filter_expression_example",
        enabled=True,
        notification_channel_id="notification_channel_id_example",
    ) # CreateCustomNotificationSubscription | The new subscription

    # example passing only required values which don't have defaults set
    try:
        # Create a custom notification subscription
        api_response = api_instance.create_notification_subscription(project_id, create_custom_notification_subscription)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->create_notification_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_custom_notification_subscription** | [**CreateCustomNotificationSubscription**](CreateCustomNotificationSubscription.md)| The new subscription |

### Return type

[**CustomNotificationSubscription**](CustomNotificationSubscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom notification subscription is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_subscription**
> delete_notification_subscription(project_id, subscription_id)

Delete a custom notification subscription

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_notification_subscriptions_api
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
    api_instance = project_custom_notification_subscriptions_api.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = "projectId_example" # str | 
    subscription_id = "subscriptionId_example" # str | The ID of the custom notification subscription to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom notification subscription
        api_instance.delete_notification_subscription(project_id, subscription_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->delete_notification_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **subscription_id** | **str**| The ID of the custom notification subscription to delete |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The custom notification subscription is successfully deleted |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_subscription**
> CustomNotificationSubscription get_notification_subscription(project_id, subscription_id)

Retrieve a notification subscription

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_notification_subscriptions_api
from libica.openapi.v2.model.custom_notification_subscription import CustomNotificationSubscription
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
    api_instance = project_custom_notification_subscriptions_api.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = "projectId_example" # str | The ID of the project
    subscription_id = "subscriptionId_example" # str | The ID of the notification subscription

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a notification subscription
        api_response = api_instance.get_notification_subscription(project_id, subscription_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->get_notification_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project |
 **subscription_id** | **str**| The ID of the notification subscription |

### Return type

[**CustomNotificationSubscription**](CustomNotificationSubscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscription is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_subscriptions**
> CustomNotificationSubscriptionList get_notification_subscriptions(project_id)

Retrieve notification subscriptions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_notification_subscriptions_api
from libica.openapi.v2.model.custom_notification_subscription_list import CustomNotificationSubscriptionList
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
    api_instance = project_custom_notification_subscriptions_api.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = "projectId_example" # str | The ID of the project

    # example passing only required values which don't have defaults set
    try:
        # Retrieve notification subscriptions
        api_response = api_instance.get_notification_subscriptions(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->get_notification_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project |

### Return type

[**CustomNotificationSubscriptionList**](CustomNotificationSubscriptionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscriptions are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_subscription**
> CustomNotificationSubscription update_notification_subscription(project_id, subscription_id, custom_notification_subscription)

Update a notification subscription

Fields which can be updated:  - enabled  - eventCode  - filterExpression  - notificationChannel 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_custom_notification_subscriptions_api
from libica.openapi.v2.model.custom_notification_subscription import CustomNotificationSubscription
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
    api_instance = project_custom_notification_subscriptions_api.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = "projectId_example" # str | The ID of the project
    subscription_id = "subscriptionId_example" # str | The ID of the custom notification subscription to update
    custom_notification_subscription = CustomNotificationSubscription(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        custom_event_code="custom_event_code_example",
        filter_expression="filter_expression_example",
        enabled=True,
        notification_channel=NotificationChannel(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            enabled=True,
            type="MAIL",
            address="address_example",
        ),
    ) # CustomNotificationSubscription | The updated subscription
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a notification subscription
        api_response = api_instance.update_notification_subscription(project_id, subscription_id, custom_notification_subscription)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->update_notification_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a notification subscription
        api_response = api_instance.update_notification_subscription(project_id, subscription_id, custom_notification_subscription, if_match=if_match)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->update_notification_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project |
 **subscription_id** | **str**| The ID of the custom notification subscription to update |
 **custom_notification_subscription** | [**CustomNotificationSubscription**](CustomNotificationSubscription.md)| The updated subscription |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]

### Return type

[**CustomNotificationSubscription**](CustomNotificationSubscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscription is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

