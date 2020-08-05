# libiap.openapi.libconsole.TokensApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](TokensApi.md#create_token) | **POST** /v1/tokens | Creates a JWT token to call IAP services.
[**get_token_details**](TokensApi.md#get_token_details) | **GET** /v1/tokens/details | Get current tokens info require authorization Bearer token
[**refresh_token**](TokensApi.md#refresh_token) | **POST** /v1/tokens:refresh | Refresh session psToken.
[**revoke_token**](TokensApi.md#revoke_token) | **DELETE** /v1/tokens | Revokes an access token.


# **create_token**
> TokenResponse create_token(x_api_key=x_api_key, client_id=client_id, api_key=api_key, domain=domain, data=data, scopes=scopes, acl=acl, mem=mem, cwid=cwid, return_session_token=return_session_token)

Creates a JWT token to call IAP services.

This endpoint creates a JWT token to call IAP services. Authorization can be a Bearer psToken,  Basic Base64 encoded username:password or Basic with apiKey.

### Example

* Api Key Authentication (Basic):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    x_api_key = 'x_api_key_example' # str | Api Key can be passed in header to generate a JWT. (optional)
client_id = 'client_id_example' # str | Optionally pass client Id from calling app to set as authorized party on JWT. (optional)
api_key = 'api_key_example' # str | OBSOLETE: api key should now be passed as as an X-API-Key header. (optional)
domain = 'domain_example' # str | Optionally pass the domain name you are logging into (optional)
data = 'data_example' # str | Data is a custom meta data field that will be applied to the session field in the JWT payload. (optional)
scopes = ['scopes_example'] # list[str] | Scopes can be passed in during token generation to limit the token to particular scopes. (optional)
acl = ['acl_example'] # list[str] | Defines the access control list to be applied to the JWT. (optional)
mem = ['mem_example'] # list[str] | Defines the membership list to be applied to the JWT. (optional)
cwid = 'cwid_example' # str | Set the current workgroup on the token. Used for aligning resources to a workgroup. (optional)
return_session_token = True # bool | By default, this endpoint returns a JWT token. You can specify returnSessionToken=true to get an Illumina psToken instead. (optional)

    try:
        # Creates a JWT token to call IAP services.
        api_response = api_instance.create_token(x_api_key=x_api_key, client_id=client_id, api_key=api_key, domain=domain, data=data, scopes=scopes, acl=acl, mem=mem, cwid=cwid, return_session_token=return_session_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->create_token: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    x_api_key = 'x_api_key_example' # str | Api Key can be passed in header to generate a JWT. (optional)
client_id = 'client_id_example' # str | Optionally pass client Id from calling app to set as authorized party on JWT. (optional)
api_key = 'api_key_example' # str | OBSOLETE: api key should now be passed as as an X-API-Key header. (optional)
domain = 'domain_example' # str | Optionally pass the domain name you are logging into (optional)
data = 'data_example' # str | Data is a custom meta data field that will be applied to the session field in the JWT payload. (optional)
scopes = ['scopes_example'] # list[str] | Scopes can be passed in during token generation to limit the token to particular scopes. (optional)
acl = ['acl_example'] # list[str] | Defines the access control list to be applied to the JWT. (optional)
mem = ['mem_example'] # list[str] | Defines the membership list to be applied to the JWT. (optional)
cwid = 'cwid_example' # str | Set the current workgroup on the token. Used for aligning resources to a workgroup. (optional)
return_session_token = True # bool | By default, this endpoint returns a JWT token. You can specify returnSessionToken=true to get an Illumina psToken instead. (optional)

    try:
        # Creates a JWT token to call IAP services.
        api_response = api_instance.create_token(x_api_key=x_api_key, client_id=client_id, api_key=api_key, domain=domain, data=data, scopes=scopes, acl=acl, mem=mem, cwid=cwid, return_session_token=return_session_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Api Key can be passed in header to generate a JWT. | [optional] 
 **client_id** | **str**| Optionally pass client Id from calling app to set as authorized party on JWT. | [optional] 
 **api_key** | **str**| OBSOLETE: api key should now be passed as as an X-API-Key header. | [optional] 
 **domain** | **str**| Optionally pass the domain name you are logging into | [optional] 
 **data** | **str**| Data is a custom meta data field that will be applied to the session field in the JWT payload. | [optional] 
 **scopes** | [**list[str]**](str.md)| Scopes can be passed in during token generation to limit the token to particular scopes. | [optional] 
 **acl** | [**list[str]**](str.md)| Defines the access control list to be applied to the JWT. | [optional] 
 **mem** | [**list[str]**](str.md)| Defines the membership list to be applied to the JWT. | [optional] 
 **cwid** | **str**| Set the current workgroup on the token. Used for aligning resources to a workgroup. | [optional] 
 **return_session_token** | **bool**| By default, this endpoint returns a JWT token. You can specify returnSessionToken&#x3D;true to get an Illumina psToken instead. | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Token is created successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_details**
> TokenDetailResponse get_token_details()

Get current tokens info require authorization Bearer token

Get token details

### Example

* Api Key Authentication (Basic):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    
    try:
        # Get current tokens info require authorization Bearer token
        api_response = api_instance.get_token_details()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->get_token_details: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    
    try:
        # Get current tokens info require authorization Bearer token
        api_response = api_instance.get_token_details()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->get_token_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenDetailResponse**](TokenDetailResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token details returned successfully |  -  |
**401** | The token provided is unauthorized. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> TokenResponse refresh_token(body=body)

Refresh session psToken.

This endpoint extends the session for the psToken.

### Example

* Api Key Authentication (Basic):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    body = libiap.openapi.libconsole.AccessTokenRequest() # AccessTokenRequest | Access token request accepts a psToken in the access_token field in the body of the request. (optional)

    try:
        # Refresh session psToken.
        api_response = api_instance.refresh_token(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->refresh_token: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    body = libiap.openapi.libconsole.AccessTokenRequest() # AccessTokenRequest | Access token request accepts a psToken in the access_token field in the body of the request. (optional)

    try:
        # Refresh session psToken.
        api_response = api_instance.refresh_token(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokensApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenRequest**](AccessTokenRequest.md)| Access token request accepts a psToken in the access_token field in the body of the request. | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Token was refreshed successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The token is no longer able to be refreshed. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(body=body)

Revokes an access token.

This endpoint revokes the access token that is passed in.

### Example

* Api Key Authentication (Basic):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    body = libiap.openapi.libconsole.AccessTokenRequest() # AccessTokenRequest | Access token request accepts either a psToken or a JWT in the access_token field in the body of the request. (optional)

    try:
        # Revokes an access token.
        api_instance.revoke_token(body=body)
    except ApiException as e:
        print("Exception when calling TokensApi->revoke_token: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libconsole
from libiap.openapi.libconsole.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Basic
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: Bearer
configuration = libiap.openapi.libconsole.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libconsole.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libconsole.TokensApi(api_client)
    body = libiap.openapi.libconsole.AccessTokenRequest() # AccessTokenRequest | Access token request accepts either a psToken or a JWT in the access_token field in the body of the request. (optional)

    try:
        # Revokes an access token.
        api_instance.revoke_token(body=body)
    except ApiException as e:
        print("Exception when calling TokensApi->revoke_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenRequest**](AccessTokenRequest.md)| Access token request accepts either a psToken or a JWT in the access_token field in the body of the request. | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Succeeded and the token has been revoked. |  -  |
**400** | An invalid or missing input parameter will result in a bad request.\&quot; |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

