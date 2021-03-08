# libica.openapi.libgds.VolumeConfigurationsApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume_configuration**](VolumeConfigurationsApi.md#create_volume_configuration) | **POST** /v1/volumeconfigurations | Create a volume configuration in GDS.
[**delete_volume_configuration**](VolumeConfigurationsApi.md#delete_volume_configuration) | **DELETE** /v1/volumeconfigurations/{volumeConfigurationName} | Deletes a volume configuration by Id or name
[**get_volume_configuration**](VolumeConfigurationsApi.md#get_volume_configuration) | **GET** /v1/volumeconfigurations/{volumeConfigurationName} | Get information for the specified volume configuration name or Id
[**list_volume_configurations**](VolumeConfigurationsApi.md#list_volume_configurations) | **GET** /v1/volumeconfigurations | Get a list of volumes
[**validate_volume_configuration**](VolumeConfigurationsApi.md#validate_volume_configuration) | **POST** /v1/volumeconfigurations/{volumeConfigurationName}:validate | Validate a volume configuration


# **create_volume_configuration**
> VolumeConfigurationResponse create_volume_configuration(body)

Create a volume configuration in GDS.

Create a volume configuration in GDS. This contains the object store details that will be used to create volumes.

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
    api_instance = libica.openapi.libgds.VolumeConfigurationsApi(api_client)
    body = libica.openapi.libgds.CreateVolumeConfigurationRequest() # CreateVolumeConfigurationRequest | 

    try:
        # Create a volume configuration in GDS.
        api_response = api_instance.create_volume_configuration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeConfigurationsApi->create_volume_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVolumeConfigurationRequest**](CreateVolumeConfigurationRequest.md)|  | 

### Return type

[**VolumeConfigurationResponse**](VolumeConfigurationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new Volume Configuration. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new Volume configuration name doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume_configuration**
> VolumeResponse delete_volume_configuration(volume_configuration_name)

Deletes a volume configuration by Id or name

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
    api_instance = libica.openapi.libgds.VolumeConfigurationsApi(api_client)
    volume_configuration_name = 'volume_configuration_name_example' # str | Unique name of the Volume Configuration to be deleted.

    try:
        # Deletes a volume configuration by Id or name
        api_response = api_instance.delete_volume_configuration(volume_configuration_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeConfigurationsApi->delete_volume_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_configuration_name** | **str**| Unique name of the Volume Configuration to be deleted. | 

### Return type

[**VolumeResponse**](VolumeResponse.md)

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
**404** | Volume not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_configuration**
> VolumeConfigurationResponse get_volume_configuration(volume_configuration_name)

Get information for the specified volume configuration name or Id

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
    api_instance = libica.openapi.libgds.VolumeConfigurationsApi(api_client)
    volume_configuration_name = 'volume_configuration_name_example' # str | Unique name of the volume configuration to retrieve information for.

    try:
        # Get information for the specified volume configuration name or Id
        api_response = api_instance.get_volume_configuration(volume_configuration_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeConfigurationsApi->get_volume_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_configuration_name** | **str**| Unique name of the volume configuration to retrieve information for. | 

### Return type

[**VolumeConfigurationResponse**](VolumeConfigurationResponse.md)

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
**404** | Volume configuration not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volume_configurations**
> VolumeConfigurationListResponse list_volume_configurations(online_status=online_status, page_size=page_size, page_token=page_token, include=include)

Get a list of volumes

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
    api_instance = libica.openapi.libgds.VolumeConfigurationsApi(api_client)
    online_status = 'online_status_example' # str | Optional field that specifies the Online Status for Volume configurations included in the list.  If provided, the value must be Initializing, Ok, or Error. (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | START_DESC END_DESC (optional)

    try:
        # Get a list of volumes
        api_response = api_instance.list_volume_configurations(online_status=online_status, page_size=page_size, page_token=page_token, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeConfigurationsApi->list_volume_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **online_status** | **str**| Optional field that specifies the Online Status for Volume configurations included in the list.  If provided, the value must be Initializing, Ok, or Error. | [optional] 
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **include** | **str**| START_DESC END_DESC | [optional] 

### Return type

[**VolumeConfigurationListResponse**](VolumeConfigurationListResponse.md)

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
**404** | Not Found |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_volume_configuration**
> VolumeConfigurationResponse validate_volume_configuration(volume_configuration_name)

Validate a volume configuration

Validate an existing volume configuration.

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
    api_instance = libica.openapi.libgds.VolumeConfigurationsApi(api_client)
    volume_configuration_name = 'volume_configuration_name_example' # str | Unique name of the volume configuration to be validated.

    try:
        # Validate a volume configuration
        api_response = api_instance.validate_volume_configuration(volume_configuration_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeConfigurationsApi->validate_volume_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_configuration_name** | **str**| Unique name of the volume configuration to be validated. | 

### Return type

[**VolumeConfigurationResponse**](VolumeConfigurationResponse.md)

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
**404** | Volume configuration not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

