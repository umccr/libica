# libica.openapi.v3.ProjectPermissionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_permission**](ProjectPermissionApi.md#create_project_permission) | **POST** /api/projects/{projectId}/permissions | Create a project permission.
[**get_project_permission**](ProjectPermissionApi.md#get_project_permission) | **GET** /api/projects/{projectId}/permissions/{permissionId} | Retrieve a project permission.
[**get_project_permissions**](ProjectPermissionApi.md#get_project_permissions) | **GET** /api/projects/{projectId}/permissions | Retrieve a list of project permissions.
[**update_project_permission**](ProjectPermissionApi.md#update_project_permission) | **PUT** /api/projects/{projectId}/permissions/{permissionId} | Update a project permission.


# **create_project_permission**
> ProjectPermissionV4 create_project_permission(project_id, create_project_permission_v4)

Create a project permission.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Added 'Administrator' role for Bench.
The role attributes are strings instead of enums to support future additions in a backward compatible manner.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_project_permission_v4 import CreateProjectPermissionV4
from libica.openapi.v3.models.project_permission_v4 import ProjectPermissionV4
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
    api_instance = libica.openapi.v3.ProjectPermissionApi(api_client)
    project_id = 'project_id_example' # str | 
    create_project_permission_v4 = libica.openapi.v3.CreateProjectPermissionV4() # CreateProjectPermissionV4 | 

    try:
        # Create a project permission.
        api_response = api_instance.create_project_permission(project_id, create_project_permission_v4)
        print("The response of ProjectPermissionApi->create_project_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPermissionApi->create_project_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_project_permission_v4** | [**CreateProjectPermissionV4**](CreateProjectPermissionV4.md)|  | 

### Return type

[**ProjectPermissionV4**](ProjectPermissionV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The project permission is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permission**
> ProjectPermissionV4 get_project_permission(project_id, permission_id)

Retrieve a project permission.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Added 'Administrator' role for Bench.
The role attributes are strings instead of enums to support future additions in a backward compatible manner.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_permission_v4 import ProjectPermissionV4
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
    api_instance = libica.openapi.v3.ProjectPermissionApi(api_client)
    project_id = 'project_id_example' # str | 
    permission_id = 'permission_id_example' # str | 

    try:
        # Retrieve a project permission.
        api_response = api_instance.get_project_permission(project_id, permission_id)
        print("The response of ProjectPermissionApi->get_project_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPermissionApi->get_project_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **permission_id** | **str**|  | 

### Return type

[**ProjectPermissionV4**](ProjectPermissionV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project permission is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permissions**
> ProjectPermissionListV4 get_project_permissions(project_id)

Retrieve a list of project permissions.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Added 'Administrator' role for Bench.
The role attributes are strings instead of enums to support future additions in a backward compatible manner.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_permission_list_v4 import ProjectPermissionListV4
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
    api_instance = libica.openapi.v3.ProjectPermissionApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve a list of project permissions.
        api_response = api_instance.get_project_permissions(project_id)
        print("The response of ProjectPermissionApi->get_project_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPermissionApi->get_project_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**ProjectPermissionListV4**](ProjectPermissionListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project permissions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_permission**
> ProjectPermissionV4 update_project_permission(project_id, permission_id, project_permission_v4, if_match=if_match)

Update a project permission.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Added 'Administrator' role for Bench.
The role attributes are strings instead of enums to support future additions in a backward compatible manner.
Fields which can be updated:
- uploadAllowed
- downloadAllowed
- roleProject
- roleFlow
- roleBase
- roleBench

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_permission_v4 import ProjectPermissionV4
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
    api_instance = libica.openapi.v3.ProjectPermissionApi(api_client)
    project_id = 'project_id_example' # str | 
    permission_id = 'permission_id_example' # str | 
    project_permission_v4 = libica.openapi.v3.ProjectPermissionV4() # ProjectPermissionV4 | 
    if_match = 'if_match_example' # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    try:
        # Update a project permission.
        api_response = api_instance.update_project_permission(project_id, permission_id, project_permission_v4, if_match=if_match)
        print("The response of ProjectPermissionApi->update_project_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPermissionApi->update_project_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **permission_id** | **str**|  | 
 **project_permission_v4** | [**ProjectPermissionV4**](ProjectPermissionV4.md)|  | 
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional] 

### Return type

[**ProjectPermissionV4**](ProjectPermissionV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project permission is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

