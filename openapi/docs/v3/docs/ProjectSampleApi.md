# libica.openapi.v3.ProjectSampleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_model_to_sample**](ProjectSampleApi.md#add_metadata_model_to_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}/metadata/{metadataModelId} | Add a metadata model to a sample.
[**complete_project_sample**](ProjectSampleApi.md#complete_project_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}:complete | Completes the sample after data has been linked to it.
[**create_sample_in_project**](ProjectSampleApi.md#create_sample_in_project) | **POST** /api/projects/{projectId}/samples | Create a new sample in this project
[**deep_delete_sample**](ProjectSampleApi.md#deep_delete_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}:deleteDeep | Delete a sample together with all of its data.
[**delete_and_unlink_sample**](ProjectSampleApi.md#delete_and_unlink_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}:deleteUnlink | Delete a sample and unlink its data.
[**delete_sample_with_input**](ProjectSampleApi.md#delete_sample_with_input) | **POST** /api/projects/{projectId}/samples/{sampleId}:deleteWithInput | Delete a sample as well as its input data.
[**get_project_sample**](ProjectSampleApi.md#get_project_sample) | **GET** /api/projects/{projectId}/samples/{sampleId} | Retrieve a project sample.
[**get_project_sample_analyses**](ProjectSampleApi.md#get_project_sample_analyses) | **GET** /api/projects/{projectId}/samples/{sampleId}/analyses | Retrieve the list of analyses.
[**get_project_samples**](ProjectSampleApi.md#get_project_samples) | **POST** /api/projects/{projectId}/samples:search | Retrieve project samples.
[**get_projects_for_sample**](ProjectSampleApi.md#get_projects_for_sample) | **GET** /api/projects/{projectId}/samples/{sampleId}/projects | Retrieve a list of projects for this sample.
[**get_sample_data_list**](ProjectSampleApi.md#get_sample_data_list) | **GET** /api/projects/{projectId}/samples/{sampleId}/data | Retrieve the list of sample data.
[**get_sample_history**](ProjectSampleApi.md#get_sample_history) | **GET** /api/projects/{projectId}/samples/{sampleId}/history | Retrieve sample history.
[**get_sample_metadata_field**](ProjectSampleApi.md#get_sample_metadata_field) | **GET** /api/projects/{projectId}/samples/{sampleId}/metadata/field/{fieldId} | Retrieve a metadata field.
[**get_sample_metadata_field_count**](ProjectSampleApi.md#get_sample_metadata_field_count) | **GET** /api/projects/{projectId}/samples/{sampleId}/metadata/{fieldId}/fieldCount | Retrieves the number of occurrences of a given field.
[**link_data_to_sample**](ProjectSampleApi.md#link_data_to_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}/data/{dataId} | Link data to a sample.
[**link_sample_to_project**](ProjectSampleApi.md#link_sample_to_project) | **POST** /api/projects/{projectId}/samples/{sampleId} | Link a sample to a project.
[**mark_sample_deleted**](ProjectSampleApi.md#mark_sample_deleted) | **POST** /api/projects/{projectId}/samples/{sampleId}:deleteMark | Mark a sample deleted.
[**search_project_sample_analyses**](ProjectSampleApi.md#search_project_sample_analyses) | **POST** /api/projects/{projectId}/samples/{sampleId}/analyses:search | Search analyses for sample.
[**unlink_data_from_sample**](ProjectSampleApi.md#unlink_data_from_sample) | **POST** /api/projects/{projectId}/samples/{sampleId}/data/{dataId}:unlink | Unlink data from a sample.
[**unlink_sample_from_project**](ProjectSampleApi.md#unlink_sample_from_project) | **POST** /api/projects/{projectId}/samples/{sampleId}:unlink | Unlink a sample from a project.
[**update_project_sample**](ProjectSampleApi.md#update_project_sample) | **PUT** /api/projects/{projectId}/samples/{sampleId} | Update a project sample.
[**update_sample_metadata_fields**](ProjectSampleApi.md#update_sample_metadata_fields) | **POST** /api/projects/{projectId}/samples/{sampleId}/metadata:updateFields | Update metadata fields.


# **add_metadata_model_to_sample**
> add_metadata_model_to_sample(project_id, sample_id, metadata_model_id)

Add a metadata model to a sample.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    metadata_model_id = 'metadata_model_id_example' # str | The ID of the metadata model

    try:
        # Add a metadata model to a sample.
        api_instance.add_metadata_model_to_sample(project_id, sample_id, metadata_model_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->add_metadata_model_to_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
 **metadata_model_id** | **str**| The ID of the metadata model | 

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
**204** | The metadata model is successfully added to the sample. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_project_sample**
> complete_project_sample(project_id, sample_id)

Completes the sample after data has been linked to it.

Completes the sample after data has been linked to it. The sample status will be set to 'Available' and a sample completed event will be triggered as well.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 

    try:
        # Completes the sample after data has been linked to it.
        api_instance.complete_project_sample(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->complete_project_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 

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
**204** | The sample is successfully completed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sample_in_project**
> ProjectSample create_sample_in_project(project_id, create_sample)

Create a new sample in this project

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_sample import CreateSample
from libica.openapi.v3.models.project_sample import ProjectSample
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    create_sample = libica.openapi.v3.CreateSample() # CreateSample | 

    try:
        # Create a new sample in this project
        api_response = api_instance.create_sample_in_project(project_id, create_sample)
        print("The response of ProjectSampleApi->create_sample_in_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->create_sample_in_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_sample** | [**CreateSample**](CreateSample.md)|  | 

### Return type

[**ProjectSample**](ProjectSample.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The sample is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deep_delete_sample**
> deep_delete_sample(project_id, sample_id)

Delete a sample together with all of its data.

Endpoint deleting a sample together with all of its data.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Delete a sample together with all of its data.
        api_instance.deep_delete_sample(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->deep_delete_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

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
**204** | The sample and all of its data are successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_and_unlink_sample**
> delete_and_unlink_sample(project_id, sample_id)

Delete a sample and unlink its data.

Endpoint for deleting a sample while unlinking its data.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Delete a sample and unlink its data.
        api_instance.delete_and_unlink_sample(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->delete_and_unlink_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

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
**204** | The sample is successfully deleted and the its data is successfully unlinked. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sample_with_input**
> delete_sample_with_input(project_id, sample_id)

Delete a sample as well as its input data.

Endpoint for deleting a sample as well as its input data.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Delete a sample as well as its input data.
        api_instance.delete_sample_with_input(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->delete_sample_with_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

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
**204** | The sample and its input data are successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_sample**
> ProjectSample get_project_sample(project_id, sample_id)

Retrieve a project sample.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_sample import ProjectSample
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Retrieve a project sample.
        api_response = api_instance.get_project_sample(project_id, sample_id)
        print("The response of ProjectSampleApi->get_project_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_project_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

### Return type

[**ProjectSample**](ProjectSample.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project sample is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_sample_analyses**
> AnalysisPagedListV3 get_project_sample_analyses(project_id, sample_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
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
        api_response = api_instance.get_project_sample_analyses(project_id, sample_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectSampleApi->get_project_sample_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_project_sample_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
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

# **get_project_samples**
> ProjectSamplePagedList get_project_samples(project_id, find_project_samples, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve project samples.

Endpoint for retrieving project samples. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.find_project_samples import FindProjectSamples
from libica.openapi.v3.models.project_sample_paged_list import ProjectSamplePagedList
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    find_project_samples = libica.openapi.v3.FindProjectSamples() # FindProjectSamples | 
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\" The attributes for which sorting is supported: - timeCreated - timeModified - name - description - metadataValid - status (optional)

    try:
        # Retrieve project samples.
        api_response = api_instance.get_project_samples(project_id, find_project_samples, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectSampleApi->get_project_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_project_samples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **find_project_samples** | [**FindProjectSamples**](FindProjectSamples.md)|  | 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot; The attributes for which sorting is supported: - timeCreated - timeModified - name - description - metadataValid - status | [optional] 

### Return type

[**ProjectSamplePagedList**](ProjectSamplePagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project samples are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_for_sample**
> ProjectList get_projects_for_sample(project_id, sample_id)

Retrieve a list of projects for this sample.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_list import ProjectList
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Retrieve a list of projects for this sample.
        api_response = api_instance.get_projects_for_sample(project_id, sample_id)
        print("The response of ProjectSampleApi->get_projects_for_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_projects_for_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of projects is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_data_list**
> DataPagedList get_sample_data_list(project_id, sample_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of sample data.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.data_paged_list import DataPagedList
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample to retrieve data for
    full_text = 'full_text_example' # str | To search through multiple fields of data. (optional)
    id = ['id_example'] # List[str] | The ids to filter on. This will always match exact. (optional)
    filename = ['filename_example'] # List[str] | The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. (optional)
    filename_match_mode = 'filename_match_mode_example' # str | How the filenames are filtered.  (optional)
    file_path = ['file_path_example'] # List[str] | The paths of the files to filter on. (optional)
    file_path_match_mode = STARTS_WITH_CASE_INSENSITIVE # str | How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the 'filePath' parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it's sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the 'filePath' parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). (optional) (default to STARTS_WITH_CASE_INSENSITIVE)
    status = ['status_example'] # List[str] | The statuses to filter on. (optional)
    format_id = ['format_id_example'] # List[str] | The IDs of the formats to filter on. (optional)
    format_code = ['format_code_example'] # List[str] | The codes of the formats to filter on. (optional)
    type = 'type_example' # str | The type to filter on. (optional)
    parent_folder_id = ['parent_folder_id_example'] # List[str] | The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. (optional)
    parent_folder_path = 'parent_folder_path_example' # str | The full path of the parent folder. Should start and end with a '/'. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. This does not work for contents from a linked folder apposed to individual linked files. (optional)
    creation_date_after = '2013-10-20T19:20:30+01:00' # datetime | The date after which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    creation_date_before = '2013-10-20T19:20:30+01:00' # datetime | The date before which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_after = '2013-10-20T19:20:30+01:00' # datetime | The date after which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_before = '2013-10-20T19:20:30+01:00' # datetime | The date before which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    user_tag = ['user_tag_example'] # List[str] | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. (optional)
    user_tag_match_mode = 'user_tag_match_mode_example' # str | How the usertags are filtered.  (optional)
    run_input_tag = ['run_input_tag_example'] # List[str] | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_input_tag_match_mode = 'run_input_tag_match_mode_example' # str | How the runInputTags are filtered.  (optional)
    run_output_tag = ['run_output_tag_example'] # List[str] | The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_output_tag_match_mode = 'run_output_tag_match_mode_example' # str | How the runOutputTags are filtered.  (optional)
    connector_tag = ['connector_tag_example'] # List[str] | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. (optional)
    connector_tag_match_mode = 'connector_tag_match_mode_example' # str | How the connectorTags are filtered.  (optional)
    technical_tag = ['technical_tag_example'] # List[str] | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. (optional)
    technical_tag_match_mode = 'technical_tag_match_mode_example' # str | How the technicalTags are filtered.  (optional)
    not_in_run = True # bool | When set to true, the data will be filtered on data which is not used in a run. (optional)
    instrument_run_id = ['instrument_run_id_example'] # List[str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    try:
        # Retrieve the list of sample data.
        api_response = api_instance.get_sample_data_list(project_id, sample_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectSampleApi->get_sample_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_sample_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample to retrieve data for | 
 **full_text** | **str**| To search through multiple fields of data. | [optional] 
 **id** | [**List[str]**](str.md)| The ids to filter on. This will always match exact. | [optional] 
 **filename** | [**List[str]**](str.md)| The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. | [optional] 
 **filename_match_mode** | **str**| How the filenames are filtered.  | [optional] 
 **file_path** | [**List[str]**](str.md)| The paths of the files to filter on. | [optional] 
 **file_path_match_mode** | **str**| How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it&#39;s sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). | [optional] [default to STARTS_WITH_CASE_INSENSITIVE]
 **status** | [**List[str]**](str.md)| The statuses to filter on. | [optional] 
 **format_id** | [**List[str]**](str.md)| The IDs of the formats to filter on. | [optional] 
 **format_code** | [**List[str]**](str.md)| The codes of the formats to filter on. | [optional] 
 **type** | **str**| The type to filter on. | [optional] 
 **parent_folder_id** | [**List[str]**](str.md)| The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. | [optional] 
 **parent_folder_path** | **str**| The full path of the parent folder. Should start and end with a &#39;/&#39;. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. This does not work for contents from a linked folder apposed to individual linked files. | [optional] 
 **creation_date_after** | **datetime**| The date after which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
 **creation_date_before** | **datetime**| The date before which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
 **status_date_after** | **datetime**| The date after which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
 **status_date_before** | **datetime**| The date before which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
 **user_tag** | [**List[str]**](str.md)| The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional] 
 **user_tag_match_mode** | **str**| How the usertags are filtered.  | [optional] 
 **run_input_tag** | [**List[str]**](str.md)| The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional] 
 **run_input_tag_match_mode** | **str**| How the runInputTags are filtered.  | [optional] 
 **run_output_tag** | [**List[str]**](str.md)| The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. | [optional] 
 **run_output_tag_match_mode** | **str**| How the runOutputTags are filtered.  | [optional] 
 **connector_tag** | [**List[str]**](str.md)| The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional] 
 **connector_tag_match_mode** | **str**| How the connectorTags are filtered.  | [optional] 
 **technical_tag** | [**List[str]**](str.md)| The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional] 
 **technical_tag_match_mode** | **str**| How the technicalTags are filtered.  | [optional] 
 **not_in_run** | **bool**| When set to true, the data will be filtered on data which is not used in a run. | [optional] 
 **instrument_run_id** | [**List[str]**](str.md)| The instrument run IDs of the sequencing runs to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt | [optional] 

### Return type

[**DataPagedList**](DataPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of sample data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_history**
> SampleHistoryList get_sample_history(project_id, sample_id)

Retrieve sample history.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.sample_history_list import SampleHistoryList
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Retrieve sample history.
        api_response = api_instance.get_sample_history(project_id, sample_id)
        print("The response of ProjectSampleApi->get_sample_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_sample_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

### Return type

[**SampleHistoryList**](SampleHistoryList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample history is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_metadata_field**
> ModelField get_sample_metadata_field(project_id, sample_id, field_id)

Retrieve a metadata field.

Returns a list of values for the field with identifier fieldId belonging to the sample with identifier sampleId. If the field is a group field that can occur more than once or belongs to a group field that can occur more than once the return value will have one entry in the list for each occurrence. If not the return value will be a single value list

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.model_field import ModelField
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    field_id = 'field_id_example' # str | The ID of the field

    try:
        # Retrieve a metadata field.
        api_response = api_instance.get_sample_metadata_field(project_id, sample_id, field_id)
        print("The response of ProjectSampleApi->get_sample_metadata_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_sample_metadata_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
 **field_id** | **str**| The ID of the field | 

### Return type

[**ModelField**](ModelField.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata field is successfully retrieved.  |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_metadata_field_count**
> ModelField get_sample_metadata_field_count(project_id, sample_id, field_id)

Retrieves the number of occurrences of a given field.

Returns a list of values for the field with identifier fieldId belonging to the sample with identifier sampleId. If the field is a group field that can occur more than once or belongs to a group field that can occur more than once the return value will have one entry in the list for each occurrence. If not the return value will be a single value list

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.model_field import ModelField
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    field_id = 'field_id_example' # str | The ID of the field

    try:
        # Retrieves the number of occurrences of a given field.
        api_response = api_instance.get_sample_metadata_field_count(project_id, sample_id, field_id)
        print("The response of ProjectSampleApi->get_sample_metadata_field_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->get_sample_metadata_field_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
 **field_id** | **str**| The ID of the field | 

### Return type

[**ModelField**](ModelField.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of occurrences is successfully retrieved.  |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_data_to_sample**
> link_data_to_sample(project_id, sample_id, data_id)

Link data to a sample.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    data_id = 'data_id_example' # str | The ID of the data to link

    try:
        # Link data to a sample.
        api_instance.link_data_to_sample(project_id, sample_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->link_data_to_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
 **data_id** | **str**| The ID of the data to link | 

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
**204** | The data is successfully linked to the sample. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_sample_to_project**
> ProjectSample link_sample_to_project(project_id, sample_id)

Link a sample to a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_sample import ProjectSample
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 

    try:
        # Link a sample to a project.
        api_response = api_instance.link_sample_to_project(project_id, sample_id)
        print("The response of ProjectSampleApi->link_sample_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->link_sample_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 

### Return type

[**ProjectSample**](ProjectSample.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The sample is successfully linked to the project. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_sample_deleted**
> mark_sample_deleted(project_id, sample_id)

Mark a sample deleted.

Endpoint for marking a sample as deleted.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample

    try:
        # Mark a sample deleted.
        api_instance.mark_sample_deleted(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->mark_sample_deleted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 

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
**204** | The sample is successfully marked as deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_project_sample_analyses**
> AnalysisPagedListV4 search_project_sample_analyses(project_id, sample_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)

Search analyses for sample.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)
    analysis_query_parameters = libica.openapi.v3.AnalysisQueryParameters() # AnalysisQueryParameters |  (optional)

    try:
        # Search analyses for sample.
        api_response = api_instance.search_project_sample_analyses(project_id, sample_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)
        print("The response of ProjectSampleApi->search_project_sample_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->search_project_sample_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
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

# **unlink_data_from_sample**
> unlink_data_from_sample(project_id, sample_id, data_id)

Unlink data from a sample.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | The ID of the sample
    data_id = 'data_id_example' # str | The ID of the data to unlink

    try:
        # Unlink data from a sample.
        api_instance.unlink_data_from_sample(project_id, sample_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->unlink_data_from_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**| The ID of the sample | 
 **data_id** | **str**| The ID of the data to unlink | 

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
**204** | The data is successfully unlinked from the sample. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_sample_from_project**
> unlink_sample_from_project(project_id, sample_id)

Unlink a sample from a project.

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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 

    try:
        # Unlink a sample from a project.
        api_instance.unlink_sample_from_project(project_id, sample_id)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->unlink_sample_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 

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
**204** | The sample is successfully unlinked from the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_sample**
> ProjectSample update_project_sample(project_id, sample_id, project_sample, if_match=if_match)

Update a project sample.

Fields which can be updated:
- sample.name
- sample.description
- sample.status
- sample.tags

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_sample import ProjectSample
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 
    project_sample = libica.openapi.v3.ProjectSample() # ProjectSample | 
    if_match = 'if_match_example' # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    try:
        # Update a project sample.
        api_response = api_instance.update_project_sample(project_id, sample_id, project_sample, if_match=if_match)
        print("The response of ProjectSampleApi->update_project_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->update_project_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 
 **project_sample** | [**ProjectSample**](ProjectSample.md)|  | 
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional] 

### Return type

[**ProjectSample**](ProjectSample.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sample_metadata_fields**
> Sample update_sample_metadata_fields(project_id, sample_id, update_metadata)

Update metadata fields.

Endpoint for updating metadata fields.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.sample import Sample
from libica.openapi.v3.models.update_metadata import UpdateMetadata
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
    api_instance = libica.openapi.v3.ProjectSampleApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 
    update_metadata = libica.openapi.v3.UpdateMetadata() # UpdateMetadata | 

    try:
        # Update metadata fields.
        api_response = api_instance.update_sample_metadata_fields(project_id, sample_id, update_metadata)
        print("The response of ProjectSampleApi->update_sample_metadata_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleApi->update_sample_metadata_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 
 **update_metadata** | [**UpdateMetadata**](UpdateMetadata.md)|  | 

### Return type

[**Sample**](Sample.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The metadata is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

