# libica.openapi.v2.PipelineLanguageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nextflow_versions**](PipelineLanguageApi.md#get_nextflow_versions) | **GET** /api/pipelineLanguages/nextflow/versions | Retrieve a list of nextflow versions.


# **get_nextflow_versions**
> PipelineLanguageVersionList get_nextflow_versions()

Retrieve a list of nextflow versions.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_language_api
from libica.openapi.v2.model.pipeline_language_version_list import PipelineLanguageVersionList
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
    api_instance = pipeline_language_api.PipelineLanguageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of nextflow versions.
        api_response = api_instance.get_nextflow_versions()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineLanguageApi->get_nextflow_versions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelineLanguageVersionList**](PipelineLanguageVersionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of nextflow versions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

