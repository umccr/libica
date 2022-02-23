# libica.openapi.v2.ProjectPermissionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_permission**](ProjectPermissionApi.md#create_project_permission) | **POST** /api/projects/{projectId}/permissions | Create a project permission.
[**get_project_permission**](ProjectPermissionApi.md#get_project_permission) | **GET** /api/projects/{projectId}/permissions/{permissionId} | Retrieve a project permission.
[**get_project_permissions**](ProjectPermissionApi.md#get_project_permissions) | **GET** /api/projects/{projectId}/permissions | Retrieve a list of project permissions.
[**update_project_permission**](ProjectPermissionApi.md#update_project_permission) | **PUT** /api/projects/{projectId}/permissions/{permissionId} | Update a project permission.


# **create_project_permission**
> ProjectPermission create_project_permission(project_id)

Create a project permission.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_permission_api
from libica.openapi.v2.model.create_project_permission import CreateProjectPermission
from libica.openapi.v2.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)
    project_id = "projectId_example" # str | 
    create_project_permission = CreateProjectPermission(
        role_project="NONE",
        role_flow="NONE",
        role_base="NONE",
        role_bench="NONE",
        membership_type="USER",
        user_id="user_id_example",
        email_address="email_address_example",
        workgroup_id="workgroup_id_example",
        upload_allowed=True,
        download_allowed=True,
    ) # CreateProjectPermission |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a project permission.
        api_response = api_instance.create_project_permission(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->create_project_permission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a project permission.
        api_response = api_instance.create_project_permission(project_id, create_project_permission=create_project_permission)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->create_project_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_project_permission** | [**CreateProjectPermission**](CreateProjectPermission.md)|  | [optional]

### Return type

[**ProjectPermission**](ProjectPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The project permission is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permission**
> ProjectPermission get_project_permission(project_id, permission_id)

Retrieve a project permission.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_permission_api
from libica.openapi.v2.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)
    project_id = "projectId_example" # str | 
    permission_id = "permissionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project permission.
        api_response = api_instance.get_project_permission(project_id, permission_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->get_project_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **permission_id** | **str**|  |

### Return type

[**ProjectPermission**](ProjectPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project permission is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permissions**
> ProjectPermissionList get_project_permissions(project_id)

Retrieve a list of project permissions.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_permission_api
from libica.openapi.v2.model.project_permission_list import ProjectPermissionList
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of project permissions.
        api_response = api_instance.get_project_permissions(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->get_project_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectPermissionList**](ProjectPermissionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project permissions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_permission**
> ProjectPermission update_project_permission(project_id, permission_id)

Update a project permission.

Fields which can be updated: - uploadAllowed - downloadAllowed - roleProject - roleFlow - roleBase - roleBench

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_permission_api
from libica.openapi.v2.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)
    project_id = "projectId_example" # str | 
    permission_id = "permissionId_example" # str | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)
    project_permission = ProjectPermission(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        role_project="NONE",
        role_flow="NONE",
        role_base="NONE",
        role_bench="NONE",
        membership_type="USER",
        user=User(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            username="username_example",
            email="email_example",
            firstname="firstname_example",
            lastname="lastname_example",
            active=True,
            tenant_administrator=True,
            job_title="job_title_example",
            greeting="MR",
            mobile_phone_number="mobile_phone_number_example",
            phone_number="phone_number_example",
            fax_number="fax_number_example",
            email_verified=True,
            two_factor_authentication=True,
            country=Country(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                code="code_example",
                name="name_example",
                region="region_example",
            ),
            address_line1="address_line1_example",
            address_line2="address_line2_example",
            address_line3="address_line3_example",
            postal_code="postal_code_example",
            city="city_example",
            state="state_example",
        ),
        email_address="email_address_example",
        workgroup=Workgroup(
            id="id_example",
            name="name_example",
            description="description_example",
        ),
        invitation_accepted=True,
        invitation_rejected=True,
        upload_allowed=True,
        download_allowed=True,
    ) # ProjectPermission |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a project permission.
        api_response = api_instance.update_project_permission(project_id, permission_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->update_project_permission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a project permission.
        api_response = api_instance.update_project_permission(project_id, permission_id, if_match=if_match, project_permission=project_permission)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPermissionApi->update_project_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **permission_id** | **str**|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]
 **project_permission** | [**ProjectPermission**](ProjectPermission.md)|  | [optional]

### Return type

[**ProjectPermission**](ProjectPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project permission is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

