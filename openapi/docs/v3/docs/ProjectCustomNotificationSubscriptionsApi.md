# libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#create_custom_notification_subscription) | **POST** /api/projects/{projectId}/customNotificationSubscriptions | Create a custom notification subscription
[**delete_custom_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#delete_custom_notification_subscription) | **DELETE** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Delete a custom notification subscription
[**get_custom_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#get_custom_notification_subscription) | **GET** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Retrieve a notification subscription
[**get_custom_notification_subscriptions**](ProjectCustomNotificationSubscriptionsApi.md#get_custom_notification_subscriptions) | **GET** /api/projects/{projectId}/customNotificationSubscriptions | Retrieve notification subscriptions
[**update_custom_notification_subscription**](ProjectCustomNotificationSubscriptionsApi.md#update_custom_notification_subscription) | **PUT** /api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId} | Update a notification subscription


# **create_custom_notification_subscription**
> CustomNotificationSubscription create_custom_notification_subscription(project_id, create_custom_notification_subscription)

Create a custom notification subscription

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_custom_notification_subscription import CreateCustomNotificationSubscription
from libica.openapi.v3.models.custom_notification_subscription import CustomNotificationSubscription
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
    api_instance = libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = 'project_id_example' # str | 
    create_custom_notification_subscription = libica.openapi.v3.CreateCustomNotificationSubscription() # CreateCustomNotificationSubscription | The new subscription

    try:
        # Create a custom notification subscription
        api_response = api_instance.create_custom_notification_subscription(project_id, create_custom_notification_subscription)
        print("The response of ProjectCustomNotificationSubscriptionsApi->create_custom_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->create_custom_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_custom_notification_subscription** | [**CreateCustomNotificationSubscription**](CreateCustomNotificationSubscription.md)| The new subscription | 

### Return type

[**CustomNotificationSubscription**](CustomNotificationSubscription.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom notification subscription is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_notification_subscription**
> delete_custom_notification_subscription(project_id, subscription_id)

Delete a custom notification subscription

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = 'project_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | The ID of the custom notification subscription to delete

    try:
        # Delete a custom notification subscription
        api_instance.delete_custom_notification_subscription(project_id, subscription_id)
    except Exception as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->delete_custom_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **subscription_id** | **str**| The ID of the custom notification subscription to delete | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The custom notification subscription is successfully deleted |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_notification_subscription**
> CustomNotificationSubscription get_custom_notification_subscription(project_id, subscription_id)

Retrieve a notification subscription

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.custom_notification_subscription import CustomNotificationSubscription
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
    api_instance = libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project
    subscription_id = 'subscription_id_example' # str | The ID of the notification subscription

    try:
        # Retrieve a notification subscription
        api_response = api_instance.get_custom_notification_subscription(project_id, subscription_id)
        print("The response of ProjectCustomNotificationSubscriptionsApi->get_custom_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->get_custom_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project | 
 **subscription_id** | **str**| The ID of the notification subscription | 

### Return type

[**CustomNotificationSubscription**](CustomNotificationSubscription.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscription is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_notification_subscriptions**
> CustomNotificationSubscriptionList get_custom_notification_subscriptions(project_id)

Retrieve notification subscriptions

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.custom_notification_subscription_list import CustomNotificationSubscriptionList
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
    api_instance = libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project

    try:
        # Retrieve notification subscriptions
        api_response = api_instance.get_custom_notification_subscriptions(project_id)
        print("The response of ProjectCustomNotificationSubscriptionsApi->get_custom_notification_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->get_custom_notification_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project | 

### Return type

[**CustomNotificationSubscriptionList**](CustomNotificationSubscriptionList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscriptions are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_notification_subscription**
> CustomNotificationSubscription update_custom_notification_subscription(project_id, subscription_id, custom_notification_subscription, if_match=if_match)

Update a notification subscription

Fields which can be updated:
 - enabled
 - eventCode
 - filterExpression
 - notificationChannel


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.custom_notification_subscription import CustomNotificationSubscription
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
    api_instance = libica.openapi.v3.ProjectCustomNotificationSubscriptionsApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project
    subscription_id = 'subscription_id_example' # str | The ID of the custom notification subscription to update
    custom_notification_subscription = libica.openapi.v3.CustomNotificationSubscription() # CustomNotificationSubscription | The updated subscription
    if_match = 'if_match_example' # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    try:
        # Update a notification subscription
        api_response = api_instance.update_custom_notification_subscription(project_id, subscription_id, custom_notification_subscription, if_match=if_match)
        print("The response of ProjectCustomNotificationSubscriptionsApi->update_custom_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCustomNotificationSubscriptionsApi->update_custom_notification_subscription: %s\n" % e)
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification subscription is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

