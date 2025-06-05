# libica.openapi.v3.PipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_pipeline_file_content**](PipelineApi.md#download_pipeline_file_content) | **GET** /api/pipelines/{pipelineId}/files/{fileId}/content | Download the contents of a pipeline file.
[**get_pipeline**](PipelineApi.md#get_pipeline) | **GET** /api/pipelines/{pipelineId} | Retrieve a pipeline.
[**get_pipeline_configuration_parameters**](PipelineApi.md#get_pipeline_configuration_parameters) | **GET** /api/pipelines/{pipelineId}/configurationParameters | Retrieve configuration parameters for a pipeline.
[**get_pipeline_files**](PipelineApi.md#get_pipeline_files) | **GET** /api/pipelines/{pipelineId}/files | Retrieve files for a pipeline.
[**get_pipeline_html_documentation**](PipelineApi.md#get_pipeline_html_documentation) | **GET** /api/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_pipeline_input_parameters**](PipelineApi.md#get_pipeline_input_parameters) | **GET** /api/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a pipeline.
[**get_pipeline_reference_sets**](PipelineApi.md#get_pipeline_reference_sets) | **GET** /api/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a pipeline.
[**get_pipelines**](PipelineApi.md#get_pipelines) | **GET** /api/pipelines | Retrieve a list of pipelines.


# **download_pipeline_file_content**
> bytearray download_pipeline_file_content(pipeline_id, file_id)

Download the contents of a pipeline file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Download the contents of a pipeline file.
        api_response = api_instance.download_pipeline_file_content(pipeline_id, file_id)
        print("The response of PipelineApi->download_pipeline_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->download_pipeline_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 
 **file_id** | **str**| The ID of the pipeline file | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> PipelineV4 get_pipeline(pipeline_id)

Retrieve a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_v4 import PipelineV4
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline to retrieve

    try:
        # Retrieve a pipeline.
        api_response = api_instance.get_pipeline(pipeline_id)
        print("The response of PipelineApi->get_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve | 

### Return type

[**PipelineV4**](PipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_configuration_parameters**
> PipelineConfigurationParameterList get_pipeline_configuration_parameters(pipeline_id)

Retrieve configuration parameters for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | 

    try:
        # Retrieve configuration parameters for a pipeline.
        api_response = api_instance.get_pipeline_configuration_parameters(pipeline_id)
        print("The response of PipelineApi->get_pipeline_configuration_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_configuration_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**|  | 

### Return type

[**PipelineConfigurationParameterList**](PipelineConfigurationParameterList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_files**
> PipelineFileList get_pipeline_files(pipeline_id)

Retrieve files for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_file_list import PipelineFileList
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for

    try:
        # Retrieve files for a pipeline.
        api_response = api_instance.get_pipeline_files(pipeline_id)
        print("The response of PipelineApi->get_pipeline_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 

### Return type

[**PipelineFileList**](PipelineFileList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The files are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_html_documentation**
> PipelineHtmlDocumentation get_pipeline_html_documentation(pipeline_id)

Retrieve HTML documentation for a project pipeline.

Retrieve HTML documentation for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve HTML documentation from

    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_pipeline_html_documentation(pipeline_id)
        print("The response of PipelineApi->get_pipeline_html_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_html_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve HTML documentation from | 

### Return type

[**PipelineHtmlDocumentation**](PipelineHtmlDocumentation.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTML documentation is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_input_parameters**
> InputParameterList get_pipeline_input_parameters(pipeline_id)

Retrieve input parameters for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.input_parameter_list import InputParameterList
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline to retrieve input parameters for

    try:
        # Retrieve input parameters for a pipeline.
        api_response = api_instance.get_pipeline_input_parameters(pipeline_id)
        print("The response of PipelineApi->get_pipeline_input_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_input_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve input parameters for | 

### Return type

[**InputParameterList**](InputParameterList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input parameters is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_reference_sets**
> ReferenceSetList get_pipeline_reference_sets(pipeline_id)

Retrieve the reference sets of a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.reference_set_list import ReferenceSetList
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline to retrieve reference sets for

    try:
        # Retrieve the reference sets of a pipeline.
        api_response = api_instance.get_pipeline_reference_sets(pipeline_id)
        print("The response of PipelineApi->get_pipeline_reference_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_reference_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve reference sets for | 

### Return type

[**ReferenceSetList**](ReferenceSetList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of reference sets is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipelines**
> PipelineList get_pipelines()

Retrieve a list of pipelines.

Only lists pipelines that are owned by the user/tenant (not those to which a user is entitled).

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_list import PipelineList
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
    api_instance = libica.openapi.v3.PipelineApi(api_client)

    try:
        # Retrieve a list of pipelines.
        api_response = api_instance.get_pipelines()
        print("The response of PipelineApi->get_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipelines: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of pipelines is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

