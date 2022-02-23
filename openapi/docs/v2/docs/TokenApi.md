# libica.openapi.v2.TokenApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jwt_token**](TokenApi.md#create_jwt_token) | **POST** /api/tokens | Generate a JWT using an API-key or Basic Authentication.
[**refresh_jwt_token**](TokenApi.md#refresh_jwt_token) | **POST** /api/tokens:refresh | Refresh a JWT using a not yet expired, still valid JWT.


# **create_jwt_token**
> Token create_jwt_token()

Generate a JWT using an API-key or Basic Authentication.

When using Basic Authentication, and you are member of several tenants, also provide the tenant request parameter to indicate for which tenant you want to authenticate. Note that Basic Authentication will not work for SSO (Single Sign On) enabled authentication.

### Example

* Api Key Authentication (ApiKeyAuth):
* Basic Authentication (BasicAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import token_api
from libica.openapi.v2.model.token import Token
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

# Configure HTTP basic authorization: BasicAuth
configuration = libica.openapi.v2.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)
    tenant = "tenant_example" # str, none_type | The name of your tenant in case you have access to multiple tenants. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a JWT using an API-key or Basic Authentication.
        api_response = api_instance.create_jwt_token(tenant=tenant)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling TokenApi->create_jwt_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str, none_type**| The name of your tenant in case you have access to multiple tenants. | [optional]

### Return type

[**Token**](Token.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JWT is successfully generated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_jwt_token**
> Token refresh_jwt_token()

Refresh a JWT using a not yet expired, still valid JWT.

When still having a valid JWT, this endpoint can be used to extend the validity.

### Example

* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import token_api
from libica.openapi.v2.model.token import Token
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

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh a JWT using a not yet expired, still valid JWT.
        api_response = api_instance.refresh_jwt_token()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling TokenApi->refresh_jwt_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JWT is successfully refreshed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

