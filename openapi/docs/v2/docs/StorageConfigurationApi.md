# libica.openapi.v2.StorageConfigurationApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_configuration**](StorageConfigurationApi.md#create_storage_configuration) | **POST** /api/storageConfigurations | Create a new storage configuration
[**get_storage_configuration**](StorageConfigurationApi.md#get_storage_configuration) | **GET** /api/storageConfigurations/{storageConfigurationId} | Retrieve a storage configuration.
[**get_storage_configuration_details**](StorageConfigurationApi.md#get_storage_configuration_details) | **GET** /api/storageConfigurations/{storageConfigurationId}/details | Retrieve a storage configuration detail.
[**get_storage_configurations**](StorageConfigurationApi.md#get_storage_configurations) | **GET** /api/storageConfigurations | Retrieve a list of storage configurations.
[**share_storage_configuration**](StorageConfigurationApi.md#share_storage_configuration) | **POST** /api/storageConfigurations/{storageConfigurationId}:share | Share your own storage configuration with tenant.
[**validate_storage_configuration**](StorageConfigurationApi.md#validate_storage_configuration) | **POST** /api/storageConfigurations/{storageConfigurationId}:validate | Start validation of your storage configuration.


# **create_storage_configuration**
> StorageConfiguration create_storage_configuration(create_storage_configuration)

Create a new storage configuration

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
from libica.openapi.v2.model.storage_configuration import StorageConfiguration
from libica.openapi.v2.model.create_storage_configuration import CreateStorageConfiguration
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)
    create_storage_configuration = CreateStorageConfiguration(
        name="wwat4ikwowtta-2mh1lcafqw2zhes0",
        description="description_example",
        storage_credential_id="storage_credential_id_example",
        type="AWS_S3",
        aws_details=AWSDetails(
            bucket_name="bucket_name_example",
            key_prefix="jR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:",
            server_side_encryption_algorithm="server_side_encryption_algorithm_example",
            server_side_encryption_key="server_side_encryption_key_example",
        ),
        region_id="region_id_example",
    ) # CreateStorageConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new storage configuration
        api_response = api_instance.create_storage_configuration(create_storage_configuration)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->create_storage_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_storage_configuration** | [**CreateStorageConfiguration**](CreateStorageConfiguration.md)|  |

### Return type

[**StorageConfiguration**](StorageConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The storage configuration is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_configuration**
> StorageConfiguration get_storage_configuration(storage_configuration_id)

Retrieve a storage configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
from libica.openapi.v2.model.storage_configuration import StorageConfiguration
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)
    storage_configuration_id = "storageConfigurationId_example" # str | The ID of the storage configuration to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a storage configuration.
        api_response = api_instance.get_storage_configuration(storage_configuration_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->get_storage_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_configuration_id** | **str**| The ID of the storage configuration to retrieve |

### Return type

[**StorageConfiguration**](StorageConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storage configuration is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_configuration_details**
> StorageConfigurationDetails get_storage_configuration_details(storage_configuration_id)

Retrieve a storage configuration detail.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
from libica.openapi.v2.model.storage_configuration_details import StorageConfigurationDetails
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)
    storage_configuration_id = "storageConfigurationId_example" # str | The ID of the storage configuration to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a storage configuration detail.
        api_response = api_instance.get_storage_configuration_details(storage_configuration_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->get_storage_configuration_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_configuration_id** | **str**| The ID of the storage configuration to retrieve |

### Return type

[**StorageConfigurationDetails**](StorageConfigurationDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storage configuration detail is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_configurations**
> StorageConfigurationWithDetailsList get_storage_configurations()

Retrieve a list of storage configurations.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
from libica.openapi.v2.model.storage_configuration_with_details_list import StorageConfigurationWithDetailsList
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of storage configurations.
        api_response = api_instance.get_storage_configurations()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->get_storage_configurations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageConfigurationWithDetailsList**](StorageConfigurationWithDetailsList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of storage configurations is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_storage_configuration**
> share_storage_configuration(storage_configuration_id)

Share your own storage configuration with tenant.

Here you share your own storage configuration with all the other users in your tenant.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)
    storage_configuration_id = "storageConfigurationId_example" # str | The ID of the storage configuration to share

    # example passing only required values which don't have defaults set
    try:
        # Share your own storage configuration with tenant.
        api_instance.share_storage_configuration(storage_configuration_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->share_storage_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_configuration_id** | **str**| The ID of the storage configuration to share |

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
**204** | The storage configuration is successfully shared. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_storage_configuration**
> validate_storage_configuration(storage_configuration_id)

Start validation of your storage configuration.

Here you start the validation of your storage configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import storage_configuration_api
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
    api_instance = storage_configuration_api.StorageConfigurationApi(api_client)
    storage_configuration_id = "storageConfigurationId_example" # str | The ID of the storage configuration to validate

    # example passing only required values which don't have defaults set
    try:
        # Start validation of your storage configuration.
        api_instance.validate_storage_configuration(storage_configuration_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling StorageConfigurationApi->validate_storage_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_configuration_id** | **str**| The ID of the storage configuration to validate |

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
**204** | The storage configuration validation is successfully started. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

