# libica.openapi.v2.MetadataModelApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_model**](MetadataModelApi.md#get_metadata_model) | **GET** /api/metadataModels/{metadataModelId} | Retrieve a metadata model. Only metadata models that the user has access to can be retrieved.
[**get_metadata_model_fields**](MetadataModelApi.md#get_metadata_model_fields) | **GET** /api/metadataModels/{metadataModelId}/fields | Retrieve the fields of a metadata model. Only metadata models that the user has access to can be retrieved.
[**get_metadata_models**](MetadataModelApi.md#get_metadata_models) | **GET** /api/metadataModels | Retrieve the metadata models for the tenant associated to the security context.
[**get_tenant_model**](MetadataModelApi.md#get_tenant_model) | **GET** /api/metadataModels/tenantModel | Retrieve the tenant model for the tenant associated to the security context.


# **get_metadata_model**
> MetadataModel get_metadata_model(metadata_model_id)

Retrieve a metadata model. Only metadata models that the user has access to can be retrieved.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import metadata_model_api
from libica.openapi.v2.model.metadata_model import MetadataModel
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
    api_instance = metadata_model_api.MetadataModelApi(api_client)
    metadata_model_id = "metadataModelId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a metadata model. Only metadata models that the user has access to can be retrieved.
        api_response = api_instance.get_metadata_model(metadata_model_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling MetadataModelApi->get_metadata_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_model_id** | **str**|  |

### Return type

[**MetadataModel**](MetadataModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata model is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_model_fields**
> FieldList get_metadata_model_fields(metadata_model_id)

Retrieve the fields of a metadata model. Only metadata models that the user has access to can be retrieved.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import metadata_model_api
from libica.openapi.v2.model.field_list import FieldList
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
    api_instance = metadata_model_api.MetadataModelApi(api_client)
    metadata_model_id = "metadataModelId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the fields of a metadata model. Only metadata models that the user has access to can be retrieved.
        api_response = api_instance.get_metadata_model_fields(metadata_model_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling MetadataModelApi->get_metadata_model_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_model_id** | **str**|  |

### Return type

[**FieldList**](FieldList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata model fields are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_models**
> MetadataModelList get_metadata_models()

Retrieve the metadata models for the tenant associated to the security context.

Retrieve the metadata models for the tenant associated to the security context. This call returns a list of metadata models for the tenant in a non-hierarchical way. Instead of a model having a list of child models all models except the root model have a parent model identifier. This can be used to reconstruct the hierarchy.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import metadata_model_api
from libica.openapi.v2.model.metadata_model_list import MetadataModelList
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
    api_instance = metadata_model_api.MetadataModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the metadata models for the tenant associated to the security context.
        api_response = api_instance.get_metadata_models()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling MetadataModelApi->get_metadata_models: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataModelList**](MetadataModelList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata models are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_model**
> Model get_tenant_model()

Retrieve the tenant model for the tenant associated to the security context.

Retrieve the tenant model for the tenant associated to the security context. The tenant model is a hierarchical structure where the top level tenant holds a list of child models (which in turn can hold child models).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import metadata_model_api
from libica.openapi.v2.model.model import Model
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
    api_instance = metadata_model_api.MetadataModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the tenant model for the tenant associated to the security context.
        api_response = api_instance.get_tenant_model()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling MetadataModelApi->get_tenant_model: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Model**](Model.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tenant model is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

