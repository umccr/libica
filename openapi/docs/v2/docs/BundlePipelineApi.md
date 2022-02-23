# libica.openapi.v2.BundlePipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_pipelines**](BundlePipelineApi.md#get_bundle_pipelines) | **GET** /api/bundles/{bundleId}/pipelines | Retrieve a list of bundle pipelines.
[**link_pipeline_to_bundle**](BundlePipelineApi.md#link_pipeline_to_bundle) | **POST** /api/bundles/{bundleId}/pipelines/{pipelineId} | Link a pipeline to a bundle.
[**unlink_pipeline_from_bundle**](BundlePipelineApi.md#unlink_pipeline_from_bundle) | **DELETE** /api/bundles/{bundleId}/pipelines/{pipelineId} | Unlink a pipeline from a bundle.


# **get_bundle_pipelines**
> BundlePipelineList get_bundle_pipelines(bundle_id)

Retrieve a list of bundle pipelines.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_pipeline_api
from libica.openapi.v2.model.bundle_pipeline_list import BundlePipelineList
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
    api_instance = bundle_pipeline_api.BundlePipelineApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to retrieve pipelines for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of bundle pipelines.
        api_response = api_instance.get_bundle_pipelines(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundlePipelineApi->get_bundle_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to retrieve pipelines for |

### Return type

[**BundlePipelineList**](BundlePipelineList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle pipelines is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_pipeline_to_bundle**
> ProjectPipeline link_pipeline_to_bundle(bundle_id, pipeline_id)

Link a pipeline to a bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_pipeline_api
from libica.openapi.v2.model.project_pipeline import ProjectPipeline
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
    api_instance = bundle_pipeline_api.BundlePipelineApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline

    # example passing only required values which don't have defaults set
    try:
        # Link a pipeline to a bundle.
        api_response = api_instance.link_pipeline_to_bundle(bundle_id, pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundlePipelineApi->link_pipeline_to_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle |
 **pipeline_id** | **str**| The ID of the pipeline |

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully linked to the bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_pipeline_from_bundle**
> unlink_pipeline_from_bundle(bundle_id, pipeline_id)

Unlink a pipeline from a bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_pipeline_api
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
    api_instance = bundle_pipeline_api.BundlePipelineApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline

    # example passing only required values which don't have defaults set
    try:
        # Unlink a pipeline from a bundle.
        api_instance.unlink_pipeline_from_bundle(bundle_id, pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundlePipelineApi->unlink_pipeline_from_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle |
 **pipeline_id** | **str**| The ID of the pipeline |

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
**204** | The pipeline is successfully unlinked from the bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

