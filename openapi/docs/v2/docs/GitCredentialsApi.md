# libica.openapi.v2.GitCredentialsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_git_credentials**](GitCredentialsApi.md#create_git_credentials) | **POST** /api/gitCredentials | Create a new git credential
[**get_git_credential**](GitCredentialsApi.md#get_git_credential) | **GET** /api/gitCredentials/{gitCredentialId} | Retrieve a git credential.
[**get_git_credentials**](GitCredentialsApi.md#get_git_credentials) | **GET** /api/gitCredentials | Retrieve a list of git credentials.
[**share_git_credential**](GitCredentialsApi.md#share_git_credential) | **POST** /api/gitCredentials/{gitCredentialId}:share | Share your own git credentials with tenant.
[**update_git_credentials**](GitCredentialsApi.md#update_git_credentials) | **POST** /api/gitCredentials/{gitCredentialId}:update | Update git credential


# **create_git_credentials**
> GitCredential create_git_credentials(create_git_credential)

Create a new git credential

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import git_credentials_api
from libica.openapi.v2.model.create_git_credential import CreateGitCredential
from libica.openapi.v2.model.git_credential import GitCredential
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
    api_instance = git_credentials_api.GitCredentialsApi(api_client)
    create_git_credential = CreateGitCredential(
        name="name_example",
        git_user_name="git_user_name_example",
        personal_accesstoken="26bUUGjjNSwg0_bs9ZayIM",
    ) # CreateGitCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new git credential
        api_response = api_instance.create_git_credentials(create_git_credential)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling GitCredentialsApi->create_git_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_git_credential** | [**CreateGitCredential**](CreateGitCredential.md)|  |

### Return type

[**GitCredential**](GitCredential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The git credential is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_credential**
> GitCredential get_git_credential(git_credential_id)

Retrieve a git credential.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import git_credentials_api
from libica.openapi.v2.model.git_credential import GitCredential
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
    api_instance = git_credentials_api.GitCredentialsApi(api_client)
    git_credential_id = "gitCredentialId_example" # str | The ID of the git credential to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a git credential.
        api_response = api_instance.get_git_credential(git_credential_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling GitCredentialsApi->get_git_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_credential_id** | **str**| The ID of the git credential to retrieve |

### Return type

[**GitCredential**](GitCredential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The git credential is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_credentials**
> GitCredentialList get_git_credentials()

Retrieve a list of git credentials.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import git_credentials_api
from libica.openapi.v2.model.git_credential_list import GitCredentialList
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
    api_instance = git_credentials_api.GitCredentialsApi(api_client)
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of git credentials.
        api_response = api_instance.get_git_credentials(page_offset=page_offset, page_token=page_token, page_size=page_size)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling GitCredentialsApi->get_git_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]

### Return type

[**GitCredentialList**](GitCredentialList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of git credentials is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_git_credential**
> share_git_credential(git_credential_id)

Share your own git credentials with tenant.

Here you share your own git credentials with all the other users in your tenant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import git_credentials_api
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
    api_instance = git_credentials_api.GitCredentialsApi(api_client)
    git_credential_id = "gitCredentialId_example" # str | The ID of the git credential to share

    # example passing only required values which don't have defaults set
    try:
        # Share your own git credentials with tenant.
        api_instance.share_git_credential(git_credential_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling GitCredentialsApi->share_git_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_credential_id** | **str**| The ID of the git credential to share |

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
**204** | The git credential is successfully shared. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_credentials**
> GitCredential update_git_credentials(git_credential_id, update_git_credential)

Update git credential

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import git_credentials_api
from libica.openapi.v2.model.update_git_credential import UpdateGitCredential
from libica.openapi.v2.model.git_credential import GitCredential
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
    api_instance = git_credentials_api.GitCredentialsApi(api_client)
    git_credential_id = "gitCredentialId_example" # str | 
    update_git_credential = UpdateGitCredential(
        git_user_name="git_user_name_example",
        personal_accesstoken="26bUUGjjNSwg0_bs9ZayIM",
    ) # UpdateGitCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Update git credential
        api_response = api_instance.update_git_credentials(git_credential_id, update_git_credential)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling GitCredentialsApi->update_git_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_credential_id** | **str**|  |
 **update_git_credential** | [**UpdateGitCredential**](UpdateGitCredential.md)|  |

### Return type

[**GitCredential**](GitCredential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The git credential is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

