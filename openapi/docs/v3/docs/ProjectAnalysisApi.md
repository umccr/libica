# libica.openapi.v3.ProjectAnalysisApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_analysis**](ProjectAnalysisApi.md#abort_analysis) | **POST** /api/projects/{projectId}/analyses/{analysisId}:abort | Abort an analysis.
[**create_cwl_analysis**](ProjectAnalysisApi.md#create_cwl_analysis) | **POST** /api/projects/{projectId}/analysis:cwl | Create and start an analysis for a CWL pipeline.
[**create_cwl_analysis_with_json_input**](ProjectAnalysisApi.md#create_cwl_analysis_with_json_input) | **POST** /api/projects/{projectId}/analysis:cwlWithJsonInput | Create and start an analysis for a CWL pipeline with an input.json.
[**create_cwl_analysis_with_structured_input**](ProjectAnalysisApi.md#create_cwl_analysis_with_structured_input) | **POST** /api/projects/{projectId}/analysis:cwlWithStructuredInput | Create and start an analysis for a CWL pipeline with a structured input.
[**create_cwl_json_analysis**](ProjectAnalysisApi.md#create_cwl_json_analysis) | **POST** /api/projects/{projectId}/analysis:cwlJson | Create and start an analysis for a JSON based CWL pipeline.
[**create_nextflow_analysis**](ProjectAnalysisApi.md#create_nextflow_analysis) | **POST** /api/projects/{projectId}/analysis:nextflow | Create and start an analysis for a Nextflow pipeline.
[**create_nextflow_analysis_with_custom_input**](ProjectAnalysisApi.md#create_nextflow_analysis_with_custom_input) | **POST** /api/projects/{projectId}/analysis:nextflowWithCustomInput | Create and initiate an analysis for a Nextflow pipeline using a custom input, provided in either YAML format or an escaped JSON string.
[**create_nextflow_json_analysis**](ProjectAnalysisApi.md#create_nextflow_json_analysis) | **POST** /api/projects/{projectId}/analysis:nextflowJson | Create and start an analysis for a JSON based Nextflow pipeline.
[**get_analyses**](ProjectAnalysisApi.md#get_analyses) | **GET** /api/projects/{projectId}/analyses | Retrieve the list of analyses.
[**get_analysis**](ProjectAnalysisApi.md#get_analysis) | **GET** /api/projects/{projectId}/analyses/{analysisId} | Retrieve an analysis.
[**get_analysis_configurations**](ProjectAnalysisApi.md#get_analysis_configurations) | **GET** /api/projects/{projectId}/analyses/{analysisId}/configurations | Retrieve the configurations of an analysis.
[**get_analysis_inputs**](ProjectAnalysisApi.md#get_analysis_inputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/inputs | Retrieve the inputs of an analysis.
[**get_analysis_logs**](ProjectAnalysisApi.md#get_analysis_logs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/logs | Retrieve the analysis logs.
[**get_analysis_outputs**](ProjectAnalysisApi.md#get_analysis_outputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/outputs | Retrieve the outputs of an analysis (limited to the first 200.000 files per output folder). When trying to retrieve the listed data with an endpoint such as GET /api/data/{dataUrn}, data which has already been deleted will be skipped.
[**get_analysis_reports**](ProjectAnalysisApi.md#get_analysis_reports) | **GET** /api/projects/{projectId}/analyses/{analysisId}/reports | Retrieve the report configs and associated reports.
[**get_analysis_steps**](ProjectAnalysisApi.md#get_analysis_steps) | **GET** /api/projects/{projectId}/analyses/{analysisId}/steps | Retrieve the individual steps of an analysis.
[**get_analysis_usage_details**](ProjectAnalysisApi.md#get_analysis_usage_details) | **GET** /api/projects/{projectId}/analyses/{analysisId}/usage | Retrieve the analysis usage details.
[**get_cwl_input_json**](ProjectAnalysisApi.md#get_cwl_input_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/inputJson | Retrieve the input json of a CWL analysis.
[**get_cwl_output_json**](ProjectAnalysisApi.md#get_cwl_output_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/outputJson | Retrieve the output json of a CWL analysis.
[**get_project_analysis_input_form_values**](ProjectAnalysisApi.md#get_project_analysis_input_form_values) | **GET** /api/projects/{projectId}/analyses/{analysisId}/inputFormValues | Retrieve the values from an input form.
[**get_raw_analysis_output**](ProjectAnalysisApi.md#get_raw_analysis_output) | **GET** /api/projects/{projectId}/analyses/{analysisId}/rawOutput | Retrieve the raw output of an analysis.
[**search_analyses**](ProjectAnalysisApi.md#search_analyses) | **POST** /api/projects/{projectId}/analysis:search | Search analyses.
[**update_analysis**](ProjectAnalysisApi.md#update_analysis) | **PUT** /api/projects/{projectId}/analyses/{analysisId} | Update an analysis.


# **abort_analysis**
> abort_analysis(project_id, analysis_id)

Abort an analysis.

Endpoint for aborting an analysis. The status of the analysis is not updated immediately, only when the abortion of the analysis has actually started.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to abort

    try:
        # Abort an analysis.
        api_instance.abort_analysis(project_id, analysis_id)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->abort_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to abort | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The analysis is successfully aborted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_analysis**
> AnalysisV4 create_cwl_analysis(project_id, create_cwl_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a CWL pipeline.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
 * Initial version
## [V4]
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_cwl_analysis import CreateCwlAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_cwl_analysis = libica.openapi.v3.CreateCwlAnalysis() # CreateCwlAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id, create_cwl_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_cwl_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_cwl_analysis** | [**CreateCwlAnalysis**](CreateCwlAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_analysis_with_json_input**
> AnalysisV4 create_cwl_analysis_with_json_input(project_id, create_cwl_with_json_input_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a CWL pipeline with an input.json.

This endpoint is intended to be used with an input.json and will bypass the input form. The combination of using this endpoint with an input.json for a json-form based pipeline with sensitive fields defined is not possible.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_cwl_with_json_input_analysis import CreateCwlWithJsonInputAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_cwl_with_json_input_analysis = libica.openapi.v3.CreateCwlWithJsonInputAnalysis() # CreateCwlWithJsonInputAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a CWL pipeline with an input.json.
        api_response = api_instance.create_cwl_analysis_with_json_input(project_id, create_cwl_with_json_input_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_cwl_analysis_with_json_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis_with_json_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_cwl_with_json_input_analysis** | [**CreateCwlWithJsonInputAnalysis**](CreateCwlWithJsonInputAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_analysis_with_structured_input**
> AnalysisV4 create_cwl_analysis_with_structured_input(project_id, create_cwl_with_structured_input_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a CWL pipeline with a structured input.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_cwl_with_structured_input_analysis import CreateCwlWithStructuredInputAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_cwl_with_structured_input_analysis = libica.openapi.v3.CreateCwlWithStructuredInputAnalysis() # CreateCwlWithStructuredInputAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a CWL pipeline with a structured input.
        api_response = api_instance.create_cwl_analysis_with_structured_input(project_id, create_cwl_with_structured_input_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_cwl_analysis_with_structured_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis_with_structured_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_cwl_with_structured_input_analysis** | [**CreateCwlWithStructuredInputAnalysis**](CreateCwlWithStructuredInputAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_json_analysis**
> AnalysisV4 create_cwl_json_analysis(project_id, create_cwl_json_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a JSON based CWL pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_cwl_json_analysis import CreateCwlJsonAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_cwl_json_analysis = libica.openapi.v3.CreateCwlJsonAnalysis() # CreateCwlJsonAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a JSON based CWL pipeline.
        api_response = api_instance.create_cwl_json_analysis(project_id, create_cwl_json_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_cwl_json_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_json_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_cwl_json_analysis** | [**CreateCwlJsonAnalysis**](CreateCwlJsonAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_analysis**
> AnalysisV4 create_nextflow_analysis(project_id, create_nextflow_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a Nextflow pipeline.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
 * Initial version
## [V4]
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_nextflow_analysis import CreateNextflowAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_nextflow_analysis = libica.openapi.v3.CreateNextflowAnalysis() # CreateNextflowAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id, create_nextflow_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_nextflow_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_nextflow_analysis** | [**CreateNextflowAnalysis**](CreateNextflowAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_analysis_with_custom_input**
> AnalysisV4 create_nextflow_analysis_with_custom_input(project_id, create_nextflow_with_custom_input_analysis, idempotency_key=idempotency_key)

Create and initiate an analysis for a Nextflow pipeline using a custom input, provided in either YAML format or an escaped JSON string.

This endpoint is intended to be used with a custom input and will bypass the input form. The combination of using this endpoint with a custom input for a json-form based pipeline with sensitive fields defined is not possible.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_nextflow_with_custom_input_analysis import CreateNextflowWithCustomInputAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_nextflow_with_custom_input_analysis = libica.openapi.v3.CreateNextflowWithCustomInputAnalysis() # CreateNextflowWithCustomInputAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and initiate an analysis for a Nextflow pipeline using a custom input, provided in either YAML format or an escaped JSON string.
        api_response = api_instance.create_nextflow_analysis_with_custom_input(project_id, create_nextflow_with_custom_input_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_nextflow_analysis_with_custom_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis_with_custom_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_nextflow_with_custom_input_analysis** | [**CreateNextflowWithCustomInputAnalysis**](CreateNextflowWithCustomInputAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_json_analysis**
> AnalysisV4 create_nextflow_json_analysis(project_id, create_nextflow_json_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a JSON based Nextflow pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
from libica.openapi.v3.models.create_nextflow_json_analysis import CreateNextflowJsonAnalysis
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_nextflow_json_analysis = libica.openapi.v3.CreateNextflowJsonAnalysis() # CreateNextflowJsonAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start an analysis for a JSON based Nextflow pipeline.
        api_response = api_instance.create_nextflow_json_analysis(project_id, create_nextflow_json_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_nextflow_json_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_json_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_nextflow_json_analysis** | [**CreateNextflowJsonAnalysis**](CreateNextflowJsonAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyses**
> AnalysisPagedListV3 get_analyses(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of analyses.

This endpoint only returns V3 items. Use the search endpoint to get V4 items.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_paged_list_v3 import AnalysisPagedListV3
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    reference = 'reference_example' # str | The reference to filter on. (optional)
    userreference = 'userreference_example' # str | The user-reference to filter on. (optional)
    status = 'status_example' # str | The status to filter on. (optional)
    usertag = 'usertag_example' # str | The user-tags to filter on. (optional)
    technicaltag = 'technicaltag_example' # str | The technical-tags to filter on. (optional)
    referencetag = 'referencetag_example' # str | The reference-data-tags to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)

    try:
        # Retrieve the list of analyses.
        api_response = api_instance.get_analyses(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectAnalysisApi->get_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **reference** | **str**| The reference to filter on. | [optional] 
 **userreference** | **str**| The user-reference to filter on. | [optional] 
 **status** | **str**| The status to filter on. | [optional] 
 **usertag** | **str**| The user-tags to filter on. | [optional] 
 **technicaltag** | **str**| The technical-tags to filter on. | [optional] 
 **referencetag** | **str**| The reference-data-tags to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional] 

### Return type

[**AnalysisPagedListV3**](AnalysisPagedListV3.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis**
> AnalysisV4 get_analysis(project_id, analysis_id)

Retrieve an analysis.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
 * Initial version
## [V4]
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve

    try:
        # Retrieve an analysis.
        api_response = api_instance.get_analysis(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve | 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_configurations**
> ExecutionConfigurationList get_analysis_configurations(project_id, analysis_id)

Retrieve the configurations of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.execution_configuration_list import ExecutionConfigurationList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the configuration for

    try:
        # Retrieve the configurations of an analysis.
        api_response = api_instance.get_analysis_configurations(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the configuration for | 

### Return type

[**ExecutionConfigurationList**](ExecutionConfigurationList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configurations of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_inputs**
> AnalysisInputList get_analysis_inputs(project_id, analysis_id)

Retrieve the inputs of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_input_list import AnalysisInputList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the inputs for

    try:
        # Retrieve the inputs of an analysis.
        api_response = api_instance.get_analysis_inputs(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the inputs for | 

### Return type

[**AnalysisInputList**](AnalysisInputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_logs**
> AnalysisLogs get_analysis_logs(project_id, analysis_id)

Retrieve the analysis logs.

Retrieves the logs of the analysis. This endpoint only supports analyses started after ICA CP v2.23 has been released.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_logs import AnalysisLogs
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the logs for

    try:
        # Retrieve the analysis logs.
        api_response = api_instance.get_analysis_logs(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the logs for | 

### Return type

[**AnalysisLogs**](AnalysisLogs.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The logs are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_outputs**
> AnalysisOutputList get_analysis_outputs(project_id, analysis_id)

Retrieve the outputs of an analysis (limited to the first 200.000 files per output folder). When trying to retrieve the listed data with an endpoint such as GET /api/data/{dataUrn}, data which has already been deleted will be skipped.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_output_list import AnalysisOutputList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the outputs for

    try:
        # Retrieve the outputs of an analysis (limited to the first 200.000 files per output folder). When trying to retrieve the listed data with an endpoint such as GET /api/data/{dataUrn}, data which has already been deleted will be skipped.
        api_response = api_instance.get_analysis_outputs(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the outputs for | 

### Return type

[**AnalysisOutputList**](AnalysisOutputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The outputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_reports**
> AnalysisReportEntryList get_analysis_reports(project_id, analysis_id)

Retrieve the report configs and associated reports.

Retrieves the reports which match the report config defined in a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_report_entry_list import AnalysisReportEntryList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the reports for

    try:
        # Retrieve the report configs and associated reports.
        api_response = api_instance.get_analysis_reports(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the reports for | 

### Return type

[**AnalysisReportEntryList**](AnalysisReportEntryList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reports are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_steps**
> AnalysisStepList get_analysis_steps(project_id, analysis_id)

Retrieve the individual steps of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_step_list import AnalysisStepList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the individual steps for

    try:
        # Retrieve the individual steps of an analysis.
        api_response = api_instance.get_analysis_steps(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the individual steps for | 

### Return type

[**AnalysisStepList**](AnalysisStepList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The individual steps of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_usage_details**
> AnalysisUsageDetails get_analysis_usage_details(project_id, analysis_id)

Retrieve the analysis usage details.

The usage details can be retrieved once the analysis has completed with status SUCCEEDED or FAILED. It may take several minutes for the information to become available. A 404 status indicates that the system is busy processing the information.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_usage_details import AnalysisUsageDetails
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the usage details for

    try:
        # Retrieve the analysis usage details.
        api_response = api_instance.get_analysis_usage_details(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_usage_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_usage_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the usage details for | 

### Return type

[**AnalysisUsageDetails**](AnalysisUsageDetails.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis usage details are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwl_input_json**
> CwlAnalysisInputJson get_cwl_input_json(project_id, analysis_id)

Retrieve the input json of a CWL analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.cwl_analysis_input_json import CwlAnalysisInputJson
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the CWL analysis for which to retrieve the input json

    try:
        # Retrieve the input json of a CWL analysis.
        api_response = api_instance.get_cwl_input_json(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_cwl_input_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_input_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the input json | 

### Return type

[**CwlAnalysisInputJson**](CwlAnalysisInputJson.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input json of the CWL analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwl_output_json**
> CwlAnalysisOutputJson get_cwl_output_json(project_id, analysis_id)

Retrieve the output json of a CWL analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.cwl_analysis_output_json import CwlAnalysisOutputJson
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the CWL analysis for which to retrieve the output json

    try:
        # Retrieve the output json of a CWL analysis.
        api_response = api_instance.get_cwl_output_json(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_cwl_output_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_output_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the output json | 

### Return type

[**CwlAnalysisOutputJson**](CwlAnalysisOutputJson.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output json of the CWL analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_analysis_input_form_values**
> InputFormFieldList get_project_analysis_input_form_values(project_id, analysis_id)

Retrieve the values from an input form.

Retrieve the values from an input form of a JSON based pipeline used to start an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.input_form_field_list import InputFormFieldList
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the input form values from

    try:
        # Retrieve the values from an input form.
        api_response = api_instance.get_project_analysis_input_form_values(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_project_analysis_input_form_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_project_analysis_input_form_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the input form values from | 

### Return type

[**InputFormFieldList**](InputFormFieldList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input form values are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_analysis_output**
> AnalysisRawOutput get_raw_analysis_output(project_id, analysis_id)

Retrieve the raw output of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_raw_output import AnalysisRawOutput
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis for which to retrieve the raw output

    try:
        # Retrieve the raw output of an analysis.
        api_response = api_instance.get_raw_analysis_output(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_raw_analysis_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_raw_analysis_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis for which to retrieve the raw output | 

### Return type

[**AnalysisRawOutput**](AnalysisRawOutput.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw output of the analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_analyses**
> AnalysisPagedListV4 search_analyses(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)

Search analyses.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_paged_list_v4 import AnalysisPagedListV4
from libica.openapi.v3.models.analysis_query_parameters import AnalysisQueryParameters
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)
    analysis_query_parameters = libica.openapi.v3.AnalysisQueryParameters() # AnalysisQueryParameters |  (optional)

    try:
        # Search analyses.
        api_response = api_instance.search_analyses(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)
        print("The response of ProjectAnalysisApi->search_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->search_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional] 
 **analysis_query_parameters** | [**AnalysisQueryParameters**](AnalysisQueryParameters.md)|  | [optional] 

### Return type

[**AnalysisPagedListV4**](AnalysisPagedListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> AnalysisV4 update_analysis(project_id, analysis_id, analysis_v4, if_match=if_match)

Update an analysis.

# Attributes which can be updated: 
  - tags
# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
 * Initial version
## [V4]
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_v4 import AnalysisV4
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
    api_instance = libica.openapi.v3.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | 
    analysis_v4 = libica.openapi.v3.AnalysisV4() # AnalysisV4 | 
    if_match = 'if_match_example' # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id, analysis_v4, if_match=if_match)
        print("The response of ProjectAnalysisApi->update_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **analysis_v4** | [**AnalysisV4**](AnalysisV4.md)|  | 
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional] 

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

