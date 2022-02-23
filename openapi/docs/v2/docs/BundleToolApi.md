# libica.openapi.v2.BundleToolApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_tools**](BundleToolApi.md#get_bundle_tools) | **GET** /api/bundles/{bundleId}/tools | Retrieve a list of bundle tools.
[**get_tools_eligible_for_linking_to_bundle**](BundleToolApi.md#get_tools_eligible_for_linking_to_bundle) | **GET** /api/bundles/{bundleId}/tools/eligibleForLinking | Retrieve a list of tools eligible for linking to the bundle.
[**link_tool_to_bundle**](BundleToolApi.md#link_tool_to_bundle) | **POST** /api/bundles/{bundleId}/tools/{toolId} | Link a tool to a bundle
[**unlink_tool_from_bundle**](BundleToolApi.md#unlink_tool_from_bundle) | **DELETE** /api/bundles/{bundleId}/tools/{toolId} | Unlink a tool from this bundle.


# **get_bundle_tools**
> BundleToolsList get_bundle_tools(bundle_id)

Retrieve a list of bundle tools.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_tool_api
from libica.openapi.v2.model.bundle_tools_list import BundleToolsList
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to get tools from

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of bundle tools.
        api_response = api_instance.get_bundle_tools(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleToolApi->get_bundle_tools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to get tools from |

### Return type

[**BundleToolsList**](BundleToolsList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle tools is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tools_eligible_for_linking_to_bundle**
> CwlToolDefinitionList get_tools_eligible_for_linking_to_bundle(bundle_id)

Retrieve a list of tools eligible for linking to the bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_tool_api
from libica.openapi.v2.model.cwl_tool_definition_list import CwlToolDefinitionList
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to get the eligible tools for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of tools eligible for linking to the bundle.
        api_response = api_instance.get_tools_eligible_for_linking_to_bundle(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleToolApi->get_tools_eligible_for_linking_to_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to get the eligible tools for |

### Return type

[**CwlToolDefinitionList**](CwlToolDefinitionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tools is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_tool_to_bundle**
> link_tool_to_bundle(bundle_id, tool_id)

Link a tool to a bundle

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_tool_api
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to link the tool to
    tool_id = "toolId_example" # str | The ID of the tool to link

    # example passing only required values which don't have defaults set
    try:
        # Link a tool to a bundle
        api_instance.link_tool_to_bundle(bundle_id, tool_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleToolApi->link_tool_to_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to link the tool to |
 **tool_id** | **str**| The ID of the tool to link |

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
**204** | The tool is successfully linked to the bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_tool_from_bundle**
> unlink_tool_from_bundle(bundle_id, tool_id)

Unlink a tool from this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_tool_api
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)
    bundle_id = "bundleId_example" # str | 
    tool_id = "toolId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink a tool from this bundle.
        api_instance.unlink_tool_from_bundle(bundle_id, tool_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleToolApi->unlink_tool_from_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **tool_id** | **str**|  |

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
**204** | The tool is successfully unlinked from this bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

