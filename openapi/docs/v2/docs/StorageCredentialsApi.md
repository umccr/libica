# libica.openapi.v2.StorageCredentialsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_credential**](StorageCredentialsApi.md#create_storage_credential) | **POST** /api/storageCredentials | Create a new storage credential
[**get_storage_credential**](StorageCredentialsApi.md#get_storage_credential) | **GET** /api/storageCredentials/{storageCredentialId} | Retrieve a storage credential.
[**get_storage_credentials**](StorageCredentialsApi.md#get_storage_credentials) | **GET** /api/storageCredentials | Retrieve a list of storage credentials.
[**share_storage_credential**](StorageCredentialsApi.md#share_storage_credential) | **POST** /api/storageCredentials/{storageCredentialId}:share | Share your own storage credentials with tenant.
[**update_storage_credential_secrets**](StorageCredentialsApi.md#update_storage_credential_secrets) | **POST** /api/storageCredentials/{storageCredentialId}:updateSecrets | Update a storage credential&#39;s secrets.


# **create_storage_credential**
> StorageCredential create_storage_credential()

Create a new storage credential

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_credentials_api
from libica.openapi.v2.model.create_storage_credential import CreateStorageCredential
from libica.openapi.v2.model.storage_credential import StorageCredential
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
    api_instance = storage_credentials_api.StorageCredentialsApi(api_client)
    create_storage_credential = CreateStorageCredential(
        name="zBAMDTMv2D2ylmgd10Z3UB",
        type="AWS_USER",
        aws_credentials=AwsCredentials(
            access_key_id="+",
            secret_access_key="+",
        ),
    ) # CreateStorageCredential |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new storage credential
        api_response = api_instance.create_storage_credential(create_storage_credential=create_storage_credential)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->create_storage_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_storage_credential** | [**CreateStorageCredential**](CreateStorageCredential.md)|  | [optional]

### Return type

[**StorageCredential**](StorageCredential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The storage credential is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_credential**
> StorageCredential get_storage_credential(storage_credential_id)

Retrieve a storage credential.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_credentials_api
from libica.openapi.v2.model.storage_credential import StorageCredential
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
    api_instance = storage_credentials_api.StorageCredentialsApi(api_client)
    storage_credential_id = "storageCredentialId_example" # str | The ID of the storage credential to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a storage credential.
        api_response = api_instance.get_storage_credential(storage_credential_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->get_storage_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**| The ID of the storage credential to retrieve |

### Return type

[**StorageCredential**](StorageCredential.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storage credential is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_credentials**
> StorageCredentialList get_storage_credentials()

Retrieve a list of storage credentials.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_credentials_api
from libica.openapi.v2.model.storage_credential_list import StorageCredentialList
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
    api_instance = storage_credentials_api.StorageCredentialsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of storage credentials.
        api_response = api_instance.get_storage_credentials()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->get_storage_credentials: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageCredentialList**](StorageCredentialList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of storage credentials is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_storage_credential**
> share_storage_credential(storage_credential_id)

Share your own storage credentials with tenant.

Here you share your own storage credentials with all the other users in your tenant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_credentials_api
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
    api_instance = storage_credentials_api.StorageCredentialsApi(api_client)
    storage_credential_id = "storageCredentialId_example" # str | The ID of the storage credential to share

    # example passing only required values which don't have defaults set
    try:
        # Share your own storage credentials with tenant.
        api_instance.share_storage_credential(storage_credential_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->share_storage_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**| The ID of the storage credential to share |

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
**204** | The storage credential is successfully shared. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_credential_secrets**
> update_storage_credential_secrets(storage_credential_id)

Update a storage credential's secrets.

When your storage credentials change or get updated due to security reasons you need to update them here.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_credentials_api
from libica.openapi.v2.model.update_storage_credential_secrets import UpdateStorageCredentialSecrets
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
    api_instance = storage_credentials_api.StorageCredentialsApi(api_client)
    storage_credential_id = "storageCredentialId_example" # str | 
    update_storage_credential_secrets = UpdateStorageCredentialSecrets(
        aws_credentials=AwsCredentials(
            access_key_id="+",
            secret_access_key="+",
        ),
    ) # UpdateStorageCredentialSecrets |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a storage credential's secrets.
        api_instance.update_storage_credential_secrets(storage_credential_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->update_storage_credential_secrets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a storage credential's secrets.
        api_instance.update_storage_credential_secrets(storage_credential_id, update_storage_credential_secrets=update_storage_credential_secrets)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageCredentialsApi->update_storage_credential_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**|  |
 **update_storage_credential_secrets** | [**UpdateStorageCredentialSecrets**](UpdateStorageCredentialSecrets.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The storage credential secrets are successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

