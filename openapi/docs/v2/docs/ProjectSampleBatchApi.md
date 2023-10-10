# libica.openapi.v2.ProjectSampleBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sample_creation_batch**](ProjectSampleBatchApi.md#create_sample_creation_batch) | **POST** /api/projects/{projectId}/sampleCreationBatch | Create a sample creation batch.
[**get_sample_creation_batch**](ProjectSampleBatchApi.md#get_sample_creation_batch) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId} | Retrieve a sample creation batch.
[**get_sample_creation_batch_item**](ProjectSampleBatchApi.md#get_sample_creation_batch_item) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId}/items/{itemId} | Retrieve a sample creation batch item.
[**get_sample_creation_batch_items**](ProjectSampleBatchApi.md#get_sample_creation_batch_items) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId}/items | Retrieve a list of sample creation batch items.


# **create_sample_creation_batch**
> SampleCreationBatch create_sample_creation_batch(project_id, create_sample_creation_batch)

Create a sample creation batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_sample_batch_api
from libica.openapi.v2.model.create_sample_creation_batch import CreateSampleCreationBatch
from libica.openapi.v2.model.sample_creation_batch import SampleCreationBatch
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
    api_instance = project_sample_batch_api.ProjectSampleBatchApi(api_client)
    project_id = "projectId_example" # str | 
    create_sample_creation_batch = CreateSampleCreationBatch(
        items=[
            CreateSampleCreationBatchSampleItem(
                sample_to_create=CreateSample(
                    name="name_example",
                    description="description_example",
                    tags=OptionalSampleTags(
                        technical_tags=[
                            "technical_tags_example",
                        ],
                        user_tags=[
                            "user_tags_example",
                        ],
                        connector_tags=[
                            "connector_tags_example",
                        ],
                        run_in_tags=[
                            "run_in_tags_example",
                        ],
                    ),
                ),
                data_to_link=[
                    CreateSampleCreationBatchDataItem(
                        data_id="data_id_example",
                    ),
                ],
                complete_sample=True,
            ),
        ],
    ) # CreateSampleCreationBatch | 
    idempotency_key = "Idempotency-Key_example" # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a sample creation batch.
        api_response = api_instance.create_sample_creation_batch(project_id, create_sample_creation_batch)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->create_sample_creation_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a sample creation batch.
        api_response = api_instance.create_sample_creation_batch(project_id, create_sample_creation_batch, idempotency_key=idempotency_key)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->create_sample_creation_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_sample_creation_batch** | [**CreateSampleCreationBatch**](CreateSampleCreationBatch.md)|  |
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional]

### Return type

[**SampleCreationBatch**](SampleCreationBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The sample creation batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch**
> SampleCreationBatch get_sample_creation_batch(project_id, batch_id)

Retrieve a sample creation batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_sample_batch_api
from libica.openapi.v2.model.sample_creation_batch import SampleCreationBatch
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
    api_instance = project_sample_batch_api.ProjectSampleBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | The ID of the sample creation batch

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a sample creation batch.
        api_response = api_instance.get_sample_creation_batch(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**| The ID of the sample creation batch |

### Return type

[**SampleCreationBatch**](SampleCreationBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample creation batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch_item**
> SampleCreationBatchSampleItem get_sample_creation_batch_item(project_id, batch_id, item_id)

Retrieve a sample creation batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_sample_batch_api
from libica.openapi.v2.model.sample_creation_batch_sample_item import SampleCreationBatchSampleItem
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
    api_instance = project_sample_batch_api.ProjectSampleBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | The ID of the sample creation batch
    item_id = "itemId_example" # str | The ID of the sample creation batch item

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a sample creation batch item.
        api_response = api_instance.get_sample_creation_batch_item(project_id, batch_id, item_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**| The ID of the sample creation batch |
 **item_id** | **str**| The ID of the sample creation batch item |

### Return type

[**SampleCreationBatchSampleItem**](SampleCreationBatchSampleItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample creation batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch_items**
> SampleCreationBatchItemPagedList get_sample_creation_batch_items(project_id, batch_id)

Retrieve a list of sample creation batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_sample_batch_api
from libica.openapi.v2.model.sample_creation_batch_item_paged_list import SampleCreationBatchItemPagedList
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
    api_instance = project_sample_batch_api.ProjectSampleBatchApi(api_client)
    project_id = "projectId_example" # str | 
    batch_id = "batchId_example" # str | The ID of the sample creation batch
    status = [
        "INITIALIZED",
    ] # [str] | The statuses to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of sample creation batch items.
        api_response = api_instance.get_sample_creation_batch_items(project_id, batch_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of sample creation batch items.
        api_response = api_instance.get_sample_creation_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch_id** | **str**| The ID of the sample creation batch |
 **status** | **[str]**| The statuses to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot; | [optional]

### Return type

[**SampleCreationBatchItemPagedList**](SampleCreationBatchItemPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of sample creation batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

