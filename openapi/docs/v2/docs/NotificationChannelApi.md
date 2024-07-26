# libica.openapi.v2.NotificationChannelApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](NotificationChannelApi.md#create_notification_channel) | **POST** /api/notificationChannels | Create a notification channel
[**delete_notification_channel**](NotificationChannelApi.md#delete_notification_channel) | **DELETE** /api/notificationChannels/{channelId} | Delete a notification channel
[**get_notification_channel**](NotificationChannelApi.md#get_notification_channel) | **GET** /api/notificationChannels/{channelId} | Retrieve a notification channel
[**get_notification_channels**](NotificationChannelApi.md#get_notification_channels) | **GET** /api/notificationChannels | Retrieve notification channels
[**update_notification_channel**](NotificationChannelApi.md#update_notification_channel) | **PUT** /api/notificationChannels/{channelId} | Update a notification channel


# **create_notification_channel**
> NotificationChannel create_notification_channel(create_notification_channel)

Create a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import notification_channel_api
from libica.openapi.v2.model.notification_channel import NotificationChannel
from libica.openapi.v2.model.create_notification_channel import CreateNotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)
    create_notification_channel = CreateNotificationChannel(
        enabled=True,
        type="MAIL",
        address="address_example",
        aws_region="aws_region_example",
    ) # CreateNotificationChannel | The new channel

    # example passing only required values which don't have defaults set
    try:
        # Create a notification channel
        api_response = api_instance.create_notification_channel(create_notification_channel)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->create_notification_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification_channel** | [**CreateNotificationChannel**](CreateNotificationChannel.md)| The new channel |

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The notification channel is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> delete_notification_channel(channel_id)

Delete a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import notification_channel_api
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)
    channel_id = "channelId_example" # str | The ID of the notification channel to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a notification channel
        api_instance.delete_notification_channel(channel_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->delete_notification_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| The ID of the notification channel to delete |

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
**204** | The notification channel is successfully deleted |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channel**
> NotificationChannel get_notification_channel(channel_id)

Retrieve a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import notification_channel_api
from libica.openapi.v2.model.notification_channel import NotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)
    channel_id = "channelId_example" # str | The ID of the notification channel to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a notification channel
        api_response = api_instance.get_notification_channel(channel_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->get_notification_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| The ID of the notification channel to retrieve |

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification channel is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channels**
> NotificationChannelList get_notification_channels()

Retrieve notification channels

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import notification_channel_api
from libica.openapi.v2.model.notification_channel_list import NotificationChannelList
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve notification channels
        api_response = api_instance.get_notification_channels()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->get_notification_channels: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationChannelList**](NotificationChannelList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification channels are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_channel**
> NotificationChannel update_notification_channel(channel_id, notification_channel)

Update a notification channel

This will affect all subscriptions which use this address!Fields which can be updated:  - enabled  - address  - awsRegion 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import notification_channel_api
from libica.openapi.v2.model.notification_channel import NotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)
    channel_id = "channelId_example" # str | The ID of the notification channel to update
    notification_channel = NotificationChannel(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        enabled=True,
        type="MAIL",
        address="address_example",
        aws_region="aws_region_example",
    ) # NotificationChannel | The updated channel
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a notification channel
        api_response = api_instance.update_notification_channel(channel_id, notification_channel)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->update_notification_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a notification channel
        api_response = api_instance.update_notification_channel(channel_id, notification_channel, if_match=if_match)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling NotificationChannelApi->update_notification_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| The ID of the notification channel to update |
 **notification_channel** | [**NotificationChannel**](NotificationChannel.md)| The updated channel |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification channel is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

