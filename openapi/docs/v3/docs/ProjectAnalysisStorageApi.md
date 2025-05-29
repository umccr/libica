# libica.openapi.v3.ProjectAnalysisStorageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_analysis_storage_options**](ProjectAnalysisStorageApi.md#get_project_analysis_storage_options) | **GET** /api/projects/{projectId}/analysisStorages | Retrieve the list of project analysis storage options.


# **get_project_analysis_storage_options**
> AnalysisStorageListV4 get_project_analysis_storage_options(project_id)

Retrieve the list of project analysis storage options.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_storage_list_v4 import AnalysisStorageListV4
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
    api_instance = libica.openapi.v3.ProjectAnalysisStorageApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve the list of project analysis storage options.
        api_response = api_instance.get_project_analysis_storage_options(project_id)
        print("The response of ProjectAnalysisStorageApi->get_project_analysis_storage_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisStorageApi->get_project_analysis_storage_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**AnalysisStorageListV4**](AnalysisStorageListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analysis storage options is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

