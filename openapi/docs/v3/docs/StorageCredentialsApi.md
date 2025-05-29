# libica.openapi.v3.StorageCredentialsApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_credential**](StorageCredentialsApi.md#create_storage_credential) | **POST** /api/storageCredentials | Create a new storage credential
[**get_storage_credential**](StorageCredentialsApi.md#get_storage_credential) | **GET** /api/storageCredentials/{storageCredentialId} | Retrieve a storage credential.
[**get_storage_credentials**](StorageCredentialsApi.md#get_storage_credentials) | **GET** /api/storageCredentials | Retrieve a list of storage credentials.
[**share_storage_credential**](StorageCredentialsApi.md#share_storage_credential) | **POST** /api/storageCredentials/{storageCredentialId}:share | Share your own storage credentials with tenant.
[**update_storage_credential_secrets**](StorageCredentialsApi.md#update_storage_credential_secrets) | **POST** /api/storageCredentials/{storageCredentialId}:updateSecrets | Update a storage credential&#39;s secrets.


# **create_storage_credential**
> StorageCredential create_storage_credential(create_storage_credential)

Create a new storage credential

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_storage_credential import CreateStorageCredential
from libica.openapi.v3.models.storage_credential import StorageCredential
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
    api_instance = libica.openapi.v3.StorageCredentialsApi(api_client)
    create_storage_credential = libica.openapi.v3.CreateStorageCredential() # CreateStorageCredential | 

    try:
        # Create a new storage credential
        api_response = api_instance.create_storage_credential(create_storage_credential)
        print("The response of StorageCredentialsApi->create_storage_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageCredentialsApi->create_storage_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_storage_credential** | [**CreateStorageCredential**](CreateStorageCredential.md)|  | 

### Return type

[**StorageCredential**](StorageCredential.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.storage_credential import StorageCredential
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
    api_instance = libica.openapi.v3.StorageCredentialsApi(api_client)
    storage_credential_id = 'storage_credential_id_example' # str | The ID of the storage credential to retrieve

    try:
        # Retrieve a storage credential.
        api_response = api_instance.get_storage_credential(storage_credential_id)
        print("The response of StorageCredentialsApi->get_storage_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageCredentialsApi->get_storage_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**| The ID of the storage credential to retrieve | 

### Return type

[**StorageCredential**](StorageCredential.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.storage_credential_list import StorageCredentialList
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
    api_instance = libica.openapi.v3.StorageCredentialsApi(api_client)

    try:
        # Retrieve a list of storage credentials.
        api_response = api_instance.get_storage_credentials()
        print("The response of StorageCredentialsApi->get_storage_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageCredentialsApi->get_storage_credentials: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StorageCredentialList**](StorageCredentialList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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
    api_instance = libica.openapi.v3.StorageCredentialsApi(api_client)
    storage_credential_id = 'storage_credential_id_example' # str | The ID of the storage credential to share

    try:
        # Share your own storage credentials with tenant.
        api_instance.share_storage_credential(storage_credential_id)
    except Exception as e:
        print("Exception when calling StorageCredentialsApi->share_storage_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**| The ID of the storage credential to share | 

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
**204** | The storage credential is successfully shared. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_credential_secrets**
> update_storage_credential_secrets(storage_credential_id, update_storage_credential_secrets)

Update a storage credential's secrets.

When your storage credentials change or get updated due to security reasons you need to update them here.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.update_storage_credential_secrets import UpdateStorageCredentialSecrets
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
    api_instance = libica.openapi.v3.StorageCredentialsApi(api_client)
    storage_credential_id = 'storage_credential_id_example' # str | 
    update_storage_credential_secrets = libica.openapi.v3.UpdateStorageCredentialSecrets() # UpdateStorageCredentialSecrets | 

    try:
        # Update a storage credential's secrets.
        api_instance.update_storage_credential_secrets(storage_credential_id, update_storage_credential_secrets)
    except Exception as e:
        print("Exception when calling StorageCredentialsApi->update_storage_credential_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_credential_id** | **str**|  | 
 **update_storage_credential_secrets** | [**UpdateStorageCredentialSecrets**](UpdateStorageCredentialSecrets.md)|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The storage credential secrets are successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

