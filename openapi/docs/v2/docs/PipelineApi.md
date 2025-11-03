# libica.openapi.v2.PipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_pipeline**](PipelineApi.md#archive_pipeline) | **POST** /api/pipelines/{pipelineId}:archive | Archive a pipeline.
[**deprecate_pipeline**](PipelineApi.md#deprecate_pipeline) | **POST** /api/pipelines/{pipelineId}:deprecate | Deprecate a pipeline.
[**download_pipeline_file_content**](PipelineApi.md#download_pipeline_file_content) | **GET** /api/pipelines/{pipelineId}/files/{fileId}/content | Download the contents of a pipeline file.
[**get_pipeline**](PipelineApi.md#get_pipeline) | **GET** /api/pipelines/{pipelineId} | Retrieve a pipeline.
[**get_pipeline_configuration_parameters**](PipelineApi.md#get_pipeline_configuration_parameters) | **GET** /api/pipelines/{pipelineId}/configurationParameters | Retrieve configuration parameters for a pipeline.
[**get_pipeline_files**](PipelineApi.md#get_pipeline_files) | **GET** /api/pipelines/{pipelineId}/files | Retrieve files for a pipeline.
[**get_pipeline_html_documentation**](PipelineApi.md#get_pipeline_html_documentation) | **GET** /api/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_pipeline_input_parameters**](PipelineApi.md#get_pipeline_input_parameters) | **GET** /api/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a pipeline.
[**get_pipeline_reference_sets**](PipelineApi.md#get_pipeline_reference_sets) | **GET** /api/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a pipeline.
[**get_pipelines**](PipelineApi.md#get_pipelines) | **GET** /api/pipelines | Retrieve a list of pipelines.


# **archive_pipeline**
> archive_pipeline(pipeline_id)

Archive a pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.archive_pipeline import ArchivePipeline
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline
    archive_pipeline = ArchivePipeline(
        message="message_example",
    ) # ArchivePipeline |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Archive a pipeline.
        api_instance.archive_pipeline(pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->archive_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Archive a pipeline.
        api_instance.archive_pipeline(pipeline_id, archive_pipeline=archive_pipeline)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->archive_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline |
 **archive_pipeline** | [**ArchivePipeline**](ArchivePipeline.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully archived. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecate_pipeline**
> deprecate_pipeline(pipeline_id)

Deprecate a pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.deprecate_pipeline import DeprecatePipeline
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline
    deprecate_pipeline = DeprecatePipeline(
        message="message_example",
    ) # DeprecatePipeline |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deprecate a pipeline.
        api_instance.deprecate_pipeline(pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->deprecate_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deprecate a pipeline.
        api_instance.deprecate_pipeline(pipeline_id, deprecate_pipeline=deprecate_pipeline)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->deprecate_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline |
 **deprecate_pipeline** | [**DeprecatePipeline**](DeprecatePipeline.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully deprecated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_pipeline_file_content**
> file_type download_pipeline_file_content(pipeline_id, file_id)

Download the contents of a pipeline file.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve files for
    file_id = "fileId_example" # str | The ID of the pipeline file

    # example passing only required values which don't have defaults set
    try:
        # Download the contents of a pipeline file.
        api_response = api_instance.download_pipeline_file_content(pipeline_id, file_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->download_pipeline_file_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for |
 **file_id** | **str**| The ID of the pipeline file |

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.pipeline_v3 import PipelineV3
from libica.openapi.v2.model.pipeline_v4 import PipelineV4
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a pipeline.
        api_response = api_instance.get_pipeline(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve |

### Return type

[**PipelineV4**](PipelineV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve configuration parameters for a pipeline.
        api_response = api_instance.get_pipeline_configuration_parameters(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_configuration_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**|  |

### Return type

[**PipelineConfigurationParameterList**](PipelineConfigurationParameterList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.pipeline_file_list import PipelineFileList
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve files for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve files for a pipeline.
        api_response = api_instance.get_pipeline_files(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for |

### Return type

[**PipelineFileList**](PipelineFileList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve HTML documentation from

    # example passing only required values which don't have defaults set
    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_pipeline_html_documentation(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_html_documentation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve HTML documentation from |

### Return type

[**PipelineHtmlDocumentation**](PipelineHtmlDocumentation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.input_parameter_list import InputParameterList
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline to retrieve input parameters for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve input parameters for a pipeline.
        api_response = api_instance.get_pipeline_input_parameters(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_input_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve input parameters for |

### Return type

[**InputParameterList**](InputParameterList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.reference_set_list import ReferenceSetList
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
    api_instance = pipeline_api.PipelineApi(api_client)
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline to retrieve reference sets for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the reference sets of a pipeline.
        api_response = api_instance.get_pipeline_reference_sets(pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_reference_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The ID of the pipeline to retrieve reference sets for |

### Return type

[**ReferenceSetList**](ReferenceSetList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import pipeline_api
from libica.openapi.v2.model.pipeline_list import PipelineList
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of pipelines.
        api_response = api_instance.get_pipelines()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling PipelineApi->get_pipelines: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of pipelines is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

