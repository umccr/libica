# libica.openapi.v2.ProjectDataTransferApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_data_transfer**](ProjectDataTransferApi.md#abort_data_transfer) | **POST** /api/projects/{projectId}/dataTransfers/{dataTransferId}:abort | Abort a data transfer.
[**get_data_transfer**](ProjectDataTransferApi.md#get_data_transfer) | **GET** /api/projects/{projectId}/dataTransfers/{dataTransferId} | Retrieve a data transfer.
[**get_data_transfers**](ProjectDataTransferApi.md#get_data_transfers) | **GET** /api/projects/{projectId}/dataTransfers | Retrieve a list of data transfers.


# **abort_data_transfer**
> abort_data_transfer(project_id, data_transfer_id)

Abort a data transfer.

Endpoint for aborting a data transfer.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_transfer_api
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
    api_instance = project_data_transfer_api.ProjectDataTransferApi(api_client)
    project_id = "projectId_example" # str | 
    data_transfer_id = "dataTransferId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Abort a data transfer.
        api_instance.abort_data_transfer(project_id, data_transfer_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataTransferApi->abort_data_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_transfer_id** | **str**|  |

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
**204** | The data transfer is successfully aborted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_transfer**
> DataTransfer get_data_transfer(project_id, data_transfer_id)

Retrieve a data transfer.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_transfer_api
from libica.openapi.v2.model.data_transfer import DataTransfer
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
    api_instance = project_data_transfer_api.ProjectDataTransferApi(api_client)
    project_id = "projectId_example" # str | 
    data_transfer_id = "dataTransferId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a data transfer.
        api_response = api_instance.get_data_transfer(project_id, data_transfer_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataTransferApi->get_data_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_transfer_id** | **str**|  |

### Return type

[**DataTransfer**](DataTransfer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data transfer is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_transfers**
> DataTransfers get_data_transfers(project_id)

Retrieve a list of data transfers.

Retrieve a list of data transfers for the current app (session), excluding web browser transfers.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_transfer_api
from libica.openapi.v2.model.data_transfers import DataTransfers
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
    api_instance = project_data_transfer_api.ProjectDataTransferApi(api_client)
    project_id = "projectId_example" # str | 
    connector = "connector_example" # str | The ID of the connector to filter on. (optional)
    direction = "direction_example" # str | The direction to filter on. (optional)
    status = "status_example" # str | The status to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - reference - direction - connector - protocol - dataTransferred - status - statusMessage - duration  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of data transfers.
        api_response = api_instance.get_data_transfers(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataTransferApi->get_data_transfers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of data transfers.
        api_response = api_instance.get_data_transfers(project_id, connector=connector, direction=direction, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataTransferApi->get_data_transfers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **connector** | **str**| The ID of the connector to filter on. | [optional]
 **direction** | **str**| The direction to filter on. | [optional]
 **status** | **str**| The status to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - reference - direction - connector - protocol - dataTransferred - status - statusMessage - duration  | [optional]

### Return type

[**DataTransfers**](DataTransfers.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of data transfers is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

