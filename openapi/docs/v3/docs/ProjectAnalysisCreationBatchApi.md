# libica.openapi.v3.ProjectAnalysisCreationBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analysis_creation_batch**](ProjectAnalysisCreationBatchApi.md#create_analysis_creation_batch) | **POST** /api/projects/{projectId}/analysisCreationBatch | Create and start multiple analyses in batch.
[**get_analysis_creation_batch**](ProjectAnalysisCreationBatchApi.md#get_analysis_creation_batch) | **GET** /api/projects/{projectId}/analysisCreationBatch/{batchId} | Retrieve a analysis creation batch.
[**get_analysis_creation_batch_item**](ProjectAnalysisCreationBatchApi.md#get_analysis_creation_batch_item) | **GET** /api/projects/{projectId}/analysisCreationBatch/{batchId}/items/{itemId} | Retrieve a analysis creation batch item.
[**get_analysis_creation_batch_items**](ProjectAnalysisCreationBatchApi.md#get_analysis_creation_batch_items) | **GET** /api/projects/{projectId}/analysisCreationBatch/{batchId}/items | Retrieve a list of analysis creation batch items.


# **create_analysis_creation_batch**
> AnalysisCreationBatch create_analysis_creation_batch(project_id, create_analysis_creation_batch, idempotency_key=idempotency_key)

Create and start multiple analyses in batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_creation_batch import AnalysisCreationBatch
from libica.openapi.v3.models.create_analysis_creation_batch import CreateAnalysisCreationBatch
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
    api_instance = libica.openapi.v3.ProjectAnalysisCreationBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    create_analysis_creation_batch = libica.openapi.v3.CreateAnalysisCreationBatch() # CreateAnalysisCreationBatch | 
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create and start multiple analyses in batch.
        api_response = api_instance.create_analysis_creation_batch(project_id, create_analysis_creation_batch, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisCreationBatchApi->create_analysis_creation_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->create_analysis_creation_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_analysis_creation_batch** | [**CreateAnalysisCreationBatch**](CreateAnalysisCreationBatch.md)|  | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**AnalysisCreationBatch**](AnalysisCreationBatch.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analyses are scheduled for creation. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_creation_batch**
> AnalysisCreationBatch get_analysis_creation_batch(project_id, batch_id)

Retrieve a analysis creation batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_creation_batch import AnalysisCreationBatch
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
    api_instance = libica.openapi.v3.ProjectAnalysisCreationBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the analysis creation batch

    try:
        # Retrieve a analysis creation batch.
        api_response = api_instance.get_analysis_creation_batch(project_id, batch_id)
        print("The response of ProjectAnalysisCreationBatchApi->get_analysis_creation_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the analysis creation batch | 

### Return type

[**AnalysisCreationBatch**](AnalysisCreationBatch.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis creation batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_creation_batch_item**
> AnalysisCreationBatchItemV4 get_analysis_creation_batch_item(project_id, batch_id, item_id)

Retrieve a analysis creation batch item.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Field 'createdAnalysis' changes:
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_creation_batch_item_v4 import AnalysisCreationBatchItemV4
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
    api_instance = libica.openapi.v3.ProjectAnalysisCreationBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the analysis creation batch
    item_id = 'item_id_example' # str | The ID of the analysis creation batch item

    try:
        # Retrieve a analysis creation batch item.
        api_response = api_instance.get_analysis_creation_batch_item(project_id, batch_id, item_id)
        print("The response of ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the analysis creation batch | 
 **item_id** | **str**| The ID of the analysis creation batch item | 

### Return type

[**AnalysisCreationBatchItemV4**](AnalysisCreationBatchItemV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis creation batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_creation_batch_items**
> AnalysisCreationBatchItemPagedListV4 get_analysis_creation_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size)

Retrieve a list of analysis creation batch items.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
 * Initial version
## [V4]
## Item field 'createdAnalysis' changes:
 * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].
 * Field analysisPriority changed from enum to String.
 * The owner and tenant are now represented by Identifier objects.


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.analysis_creation_batch_item_paged_list_v4 import AnalysisCreationBatchItemPagedListV4
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
    api_instance = libica.openapi.v3.ProjectAnalysisCreationBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the analysis creation batch
    status = ['status_example'] # List[str] | The statuses to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    try:
        # Retrieve a list of analysis creation batch items.
        api_response = api_instance.get_analysis_creation_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size)
        print("The response of ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the analysis creation batch | 
 **status** | [**List[str]**](str.md)| The statuses to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 

### Return type

[**AnalysisCreationBatchItemPagedListV4**](AnalysisCreationBatchItemPagedListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of analysis creation batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

