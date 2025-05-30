# libica.openapi.v3.PipelineLanguageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nextflow_versions**](PipelineLanguageApi.md#get_nextflow_versions) | **GET** /api/pipelineLanguages/nextflow/versions | Retrieve a list of nextflow versions.


# **get_nextflow_versions**
> PipelineLanguageVersionList get_nextflow_versions()

Retrieve a list of nextflow versions.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_language_version_list import PipelineLanguageVersionList
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
    api_instance = libica.openapi.v3.PipelineLanguageApi(api_client)

    try:
        # Retrieve a list of nextflow versions.
        api_response = api_instance.get_nextflow_versions()
        print("The response of PipelineLanguageApi->get_nextflow_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineLanguageApi->get_nextflow_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PipelineLanguageVersionList**](PipelineLanguageVersionList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of nextflow versions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

