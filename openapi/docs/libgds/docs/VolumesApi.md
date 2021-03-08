# libica.openapi.libgds.VolumesApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume**](VolumesApi.md#create_volume) | **POST** /v1/volumes | Create a volume in GDS and receive temporary credentials for upload
[**delete_volume**](VolumesApi.md#delete_volume) | **DELETE** /v1/volumes/{volumeId} | Deletes a volume by Id
[**get_volume**](VolumesApi.md#get_volume) | **GET** /v1/volumes/{volumeId} | Get information for the specified volume ID or volume name
[**list_volumes**](VolumesApi.md#list_volumes) | **GET** /v1/volumes | Get a list of volumes


# **create_volume**
> CreateVolumeResponse create_volume(body, include=include)

Create a volume in GDS and receive temporary credentials for upload

Create a volume in GDS to hold folders and files. Returns upload credentials to the root folder of the volume when the include=objectStoreAccess parameter is used. You must create a volume prior to uploading files or folders.

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
    api_instance = libica.openapi.libgds.VolumesApi(api_client)
    body = libica.openapi.libgds.CreateVolumeRequest() # CreateVolumeRequest | 
include = 'include_example' # str | Comma-separated list of properties to include in the response ([include=[totalItemCount]).Example: include=totalItemCount (optional)

    try:
        # Create a volume in GDS and receive temporary credentials for upload
        api_response = api_instance.create_volume(body, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumesApi->create_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVolumeRequest**](CreateVolumeRequest.md)|  | 
 **include** | **str**| Comma-separated list of properties to include in the response ([include&#x3D;[totalItemCount]).Example: include&#x3D;totalItemCount | [optional] 

### Return type

[**CreateVolumeResponse**](CreateVolumeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new Volume. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new Volume doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> VolumeResponse delete_volume(volume_id, purge_object_store_data=purge_object_store_data)

Deletes a volume by Id

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
    api_instance = libica.openapi.libgds.VolumesApi(api_client)
    volume_id = 'volume_id_example' # str | Unique identifier for the Volume to be deleted.
purge_object_store_data = True # bool | Optional and for BYOB only. If true, the volume's data in object storage will be erased.              This field is ignored for non-BYOB volumes where the object store data is always removed upon deleting the volume. (optional)

    try:
        # Deletes a volume by Id
        api_response = api_instance.delete_volume(volume_id, purge_object_store_data=purge_object_store_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumesApi->delete_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| Unique identifier for the Volume to be deleted. | 
 **purge_object_store_data** | **bool**| Optional and for BYOB only. If true, the volume&#39;s data in object storage will be erased.              This field is ignored for non-BYOB volumes where the object store data is always removed upon deleting the volume. | [optional] 

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
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume**
> VolumeResponse get_volume(volume_id, tenant_id=tenant_id)

Get information for the specified volume ID or volume name

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
    api_instance = libica.openapi.libgds.VolumesApi(api_client)
    volume_id = 'volume_id_example' # str | Unique identifier for the volume to retrieve information for.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)

    try:
        # Get information for the specified volume ID or volume name
        api_response = api_instance.get_volume(volume_id, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumesApi->get_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| Unique identifier for the volume to retrieve information for. | 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 

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
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Volume not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volumes**
> VolumeListResponse list_volumes(page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, volume_configuration_name=volume_configuration_name)

Get a list of volumes

Get a list of volumes accessible by the current JWT token’s tenant ID in GDS. The default sort returned is alphabetical, ascending. The default page size is 10 items.

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
    api_instance = libica.openapi.libgds.VolumesApi(api_client)
    page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | START_DESC END_DESC (optional)
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
volume_configuration_name = 'volume_configuration_name_example' # str | Unique name of the volume configuration (optional)

    try:
        # Get a list of volumes
        api_response = api_instance.list_volumes(page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, volume_configuration_name=volume_configuration_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumesApi->list_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **include** | **str**| START_DESC END_DESC | [optional] 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **volume_configuration_name** | **str**| Unique name of the volume configuration | [optional] 

### Return type

[**VolumeListResponse**](VolumeListResponse.md)

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

