# libica.openapi.v2.ConnectorApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_connector**](ConnectorApi.md#cancel_connector) | **POST** /api/connectors/{connectorId}:cancel | Cancel a connector.
[**create_connector**](ConnectorApi.md#create_connector) | **POST** /api/connectors | Create a connector.
[**create_download_rule**](ConnectorApi.md#create_download_rule) | **POST** /api/connectors/{connectorId}/downloadRules | Create a download rule.
[**create_upload_rule**](ConnectorApi.md#create_upload_rule) | **POST** /api/connectors/{connectorId}/uploadRules | Create an upload rule.
[**delete_download_rule**](ConnectorApi.md#delete_download_rule) | **DELETE** /api/connectors/{connectorId}/downloadRules/{downloadRuleId} | Delete a download rule.
[**delete_upload_rule**](ConnectorApi.md#delete_upload_rule) | **DELETE** /api/connectors/{connectorId}/uploadRules/{uploadRuleId} | Delete an upload rule.
[**disable_connector**](ConnectorApi.md#disable_connector) | **POST** /api/connectors/{connectorId}:disable | Disable a connector.
[**enable_connector**](ConnectorApi.md#enable_connector) | **POST** /api/connectors/{connectorId}:enable | Enable a connector.
[**get_connector**](ConnectorApi.md#get_connector) | **GET** /api/connectors/{connectorId} | Retrieve a connector.
[**get_connectors**](ConnectorApi.md#get_connectors) | **GET** /api/connectors | Retrieve a list of connectors.
[**get_download_rule**](ConnectorApi.md#get_download_rule) | **GET** /api/connectors/{connectorId}/downloadRules/{downloadRuleId} | Retrieve a download rule.
[**get_download_rules**](ConnectorApi.md#get_download_rules) | **GET** /api/connectors/{connectorId}/downloadRules | Retrieve a list of download rules.
[**get_upload_rule**](ConnectorApi.md#get_upload_rule) | **GET** /api/connectors/{connectorId}/uploadRules/{uploadRuleId} | Retrieve an upload rule.
[**get_upload_rules**](ConnectorApi.md#get_upload_rules) | **GET** /api/connectors/{connectorId}/uploadRules | Retrieve a list of upload rules.
[**update_download_rule**](ConnectorApi.md#update_download_rule) | **PUT** /api/connectors/{connectorId}/downloadRules/{downloadRuleId} | Update a download rule.
[**update_upload_rule**](ConnectorApi.md#update_upload_rule) | **PUT** /api/connectors/{connectorId}/uploadRules/{uploadRuleId} | Update an upload rule.


# **cancel_connector**
> cancel_connector(connector_id)

Cancel a connector.

Endpoint for cancelling a connector. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a connector.
        api_instance.cancel_connector(connector_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->cancel_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

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
**204** | The connector is successfully cancelled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connector**
> Connector create_connector()

Create a connector.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.create_connector import CreateConnector
from libica.openapi.v2.model.connector import Connector
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
    api_instance = connector_api.ConnectorApi(api_client)
    create_connector = CreateConnector(
        code="code_example",
        active=True,
        country_id="country_id_example",
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        address_line3="address_line3_example",
        postal_code="postal_code_example",
        city="city_example",
        state="state_example",
        description="description_example",
        mode="DOWNLOAD",
        max_bandwidth=0.01,
        max_concurrent_transfers=2,
        os="WINDOWS",
    ) # CreateConnector | The connector to create. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a connector.
        api_response = api_instance.create_connector(create_connector=create_connector)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->create_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connector** | [**CreateConnector**](CreateConnector.md)| The connector to create. | [optional]

### Return type

[**Connector**](Connector.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The connector is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download_rule**
> DownloadRule create_download_rule(connector_id)

Create a download rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.create_download_rule import CreateDownloadRule
from libica.openapi.v2.model.download_rule import DownloadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    create_download_rule = CreateDownloadRule(
        code="code_example",
        active=True,
        description="description_example",
        sequence=0,
        format_code="format_code_example",
        project_name="project_name_example",
        target_local_folder="target_local_folder_example",
        file_name_expression="file_name_expression_example",
    ) # CreateDownloadRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a download rule.
        api_response = api_instance.create_download_rule(connector_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->create_download_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a download rule.
        api_response = api_instance.create_download_rule(connector_id, create_download_rule=create_download_rule)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->create_download_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **create_download_rule** | [**CreateDownloadRule**](CreateDownloadRule.md)|  | [optional]

### Return type

[**DownloadRule**](DownloadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The download rule is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_rule**
> UploadRule create_upload_rule(connector_id)

Create an upload rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.create_upload_rule import CreateUploadRule
from libica.openapi.v2.model.upload_rule import UploadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    create_upload_rule = CreateUploadRule(
        code="code_example",
        active=True,
        description="description_example",
        local_folder="local_folder_example",
        file_pattern="file_pattern_example",
        data_format_id="data_format_id_example",
        project_id="project_id_example",
    ) # CreateUploadRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an upload rule.
        api_response = api_instance.create_upload_rule(connector_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->create_upload_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an upload rule.
        api_response = api_instance.create_upload_rule(connector_id, create_upload_rule=create_upload_rule)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->create_upload_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **create_upload_rule** | [**CreateUploadRule**](CreateUploadRule.md)|  | [optional]

### Return type

[**UploadRule**](UploadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upload rule is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_download_rule**
> delete_download_rule(connector_id, download_rule_id)

Delete a download rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    download_rule_id = "downloadRuleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a download rule.
        api_instance.delete_download_rule(connector_id, download_rule_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->delete_download_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **download_rule_id** | **str**|  |

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
**204** | The download rule is successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upload_rule**
> delete_upload_rule(connector_id, upload_rule_id)

Delete an upload rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    upload_rule_id = "uploadRuleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an upload rule.
        api_instance.delete_upload_rule(connector_id, upload_rule_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->delete_upload_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **upload_rule_id** | **str**|  |

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
**204** | The upload rule is successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_connector**
> disable_connector(connector_id)

Disable a connector.

Endpoint for disabling a connector. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disable a connector.
        api_instance.disable_connector(connector_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->disable_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

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
**204** | The connector is successfully disabled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_connector**
> enable_connector(connector_id)

Enable a connector.

Endpoint for enabling a connector. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enable a connector.
        api_instance.enable_connector(connector_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->enable_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

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
**204** | The connector is successfully enabled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> Connector get_connector(connector_id)

Retrieve a connector.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.connector import Connector
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a connector.
        api_response = api_instance.get_connector(connector_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

### Return type

[**Connector**](Connector.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connector is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors**
> ConnectorList get_connectors()

Retrieve a list of connectors.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.connector_list import ConnectorList
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
    api_instance = connector_api.ConnectorApi(api_client)
    active_only = True # bool | When true only the active connectors will be returned. When false (default value) all connectors wil be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of connectors.
        api_response = api_instance.get_connectors(active_only=active_only)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_only** | **bool**| When true only the active connectors will be returned. When false (default value) all connectors wil be returned. | [optional]

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of connectors is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_rule**
> DownloadRule get_download_rule(connector_id, download_rule_id)

Retrieve a download rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.download_rule import DownloadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    download_rule_id = "downloadRuleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a download rule.
        api_response = api_instance.get_download_rule(connector_id, download_rule_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_download_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **download_rule_id** | **str**|  |

### Return type

[**DownloadRule**](DownloadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download rule is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_rules**
> DownloadRuleList get_download_rules(connector_id)

Retrieve a list of download rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.download_rule_list import DownloadRuleList
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of download rules.
        api_response = api_instance.get_download_rules(connector_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_download_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

### Return type

[**DownloadRuleList**](DownloadRuleList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download rules are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_rule**
> UploadRule get_upload_rule(connector_id, upload_rule_id)

Retrieve an upload rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.upload_rule import UploadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    upload_rule_id = "uploadRuleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an upload rule.
        api_response = api_instance.get_upload_rule(connector_id, upload_rule_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_upload_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **upload_rule_id** | **str**|  |

### Return type

[**UploadRule**](UploadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload rule is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_rules**
> UploadRuleList get_upload_rules(connector_id)

Retrieve a list of upload rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.upload_rule_list import UploadRuleList
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of upload rules.
        api_response = api_instance.get_upload_rules(connector_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->get_upload_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |

### Return type

[**UploadRuleList**](UploadRuleList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload rules are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_download_rule**
> DownloadRule update_download_rule(connector_id, download_rule_id)

Update a download rule.

Fields which can be updated:  - code  - active  - description  - sequence  - formatCode  - projectName  - targetLocalFolder  - protocol  - fileNameExpression  - disableHashing

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.download_rule import DownloadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    download_rule_id = "downloadRuleId_example" # str | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)
    download_rule = DownloadRule(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        code="code_example",
        active=True,
        description="description_example",
        sequence=0,
        format_code="format_code_example",
        project_name="project_name_example",
        target_local_folder="target_local_folder_example",
        file_name_expression="file_name_expression_example",
    ) # DownloadRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a download rule.
        api_response = api_instance.update_download_rule(connector_id, download_rule_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->update_download_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a download rule.
        api_response = api_instance.update_download_rule(connector_id, download_rule_id, if_match=if_match, download_rule=download_rule)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->update_download_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **download_rule_id** | **str**|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]
 **download_rule** | [**DownloadRule**](DownloadRule.md)|  | [optional]

### Return type

[**DownloadRule**](DownloadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download rule is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_upload_rule**
> UploadRule update_upload_rule(connector_id, upload_rule_id)

Update an upload rule.

Fields which can be updated:  - code  - active  - description  - localFolder  - filePattern  - dataFormat 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import connector_api
from libica.openapi.v2.model.upload_rule import UploadRule
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
    api_instance = connector_api.ConnectorApi(api_client)
    connector_id = "connectorId_example" # str | 
    upload_rule_id = "uploadRuleId_example" # str | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)
    upload_rule = UploadRule(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        code="code_example",
        active=True,
        description="description_example",
        local_folder="local_folder_example",
        file_pattern="file_pattern_example",
        data_format=DataFormat(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            code="code_example",
            description="description_example",
            mime_type="mime_type_example",
        ),
        project=Project(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            name="name_example",
            active=True,
            short_description="short_description_example",
            information="information_example",
            region=Region(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                code="code_example",
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
                city_name="city_name_example",
            ),
            billing_mode="PROJECT",
            data_sharing_enabled=True,
            tags=ProjectTag(
                technical_tags=[
                    "technical_tags_example",
                ],
                user_tags=[
                    "user_tags_example",
                ],
            ),
            storage_bundle=StorageBundle(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                bundle_name="bundle_name_example",
                entitlement_name="entitlement_name_example",
                region=Region(
                    id="id_example",
                    time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    owner_id="owner_id_example",
                    tenant_id="tenant_id_example",
                    tenant_name="tenant_name_example",
                    code="code_example",
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
                    city_name="city_name_example",
                ),
            ),
            self_managed_storage_configuration=StorageConfiguration(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                name="name_example",
                description="description_example",
                type="AWS_S3",
                status="INITIALIZING",
                error_message="error_message_example",
                region=Region(
                    id="id_example",
                    time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    owner_id="owner_id_example",
                    tenant_id="tenant_id_example",
                    tenant_name="tenant_name_example",
                    code="code_example",
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
                    city_name="city_name_example",
                ),
                is_default=True,
            ),
            metadata_model=MetadataModel(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                name="name_example",
                description="description_example",
                state="DRAFT",
                parent_model_id="parent_model_id_example",
            ),
            application=Application(
                id="id_example",
                name="name_example",
                type="MAIN",
                display_name="display_name_example",
            ),
        ),
    ) # UploadRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an upload rule.
        api_response = api_instance.update_upload_rule(connector_id, upload_rule_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->update_upload_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an upload rule.
        api_response = api_instance.update_upload_rule(connector_id, upload_rule_id, if_match=if_match, upload_rule=upload_rule)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ConnectorApi->update_upload_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  |
 **upload_rule_id** | **str**|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]
 **upload_rule** | [**UploadRule**](UploadRule.md)|  | [optional]

### Return type

[**UploadRule**](UploadRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload rule is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

