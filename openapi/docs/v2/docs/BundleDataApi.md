# libica.openapi.v2.BundleDataApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_data**](BundleDataApi.md#get_bundle_data) | **GET** /api/bundles/{bundleId}/data | Retrieve the list of bundle data.
[**link_data_to_bundle**](BundleDataApi.md#link_data_to_bundle) | **POST** /api/bundles/{bundleId}/data/{dataId} | Link data to this bundle.
[**unlink_data_from_bundle**](BundleDataApi.md#unlink_data_from_bundle) | **DELETE** /api/bundles/{bundleId}/data/{dataId} | Unlink data from this bundle.


# **get_bundle_data**
> BundleDataPagedList get_bundle_data(bundle_id)

Retrieve the list of bundle data.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_api
from libica.openapi.v2.model.bundle_data_paged_list import BundleDataPagedList
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
    api_instance = bundle_data_api.BundleDataApi(api_client)
    bundle_id = "bundleId_example" # str | 
    full_text = "fullText_example" # str | To search through multiple fields of data. (optional)
    id = "id_example" # str | The ids to filter on. This will always match exact. (optional)
    filename = "filename_example" # str | The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. (optional)
    filename_match_mode = "EXACT" # str | How the filenames are filtered. (optional)
    file_path = "filePath_example" # str | The paths of the files to filter on. (optional)
    file_path_match_mode = "STARTS_WITH_CASE_INSENSITIVE" # str | How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the 'filePath' parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it's sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the 'filePath' parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). (optional) if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
    status = "PARTIAL" # str | The statuses to filter on. (optional)
    format_id = "formatId_example" # str | The IDs of the formats to filter on. (optional)
    format_code = "formatCode_example" # str | The codes of the formats to filter on. (optional)
    type = "FILE" # str | The type to filter on. (optional)
    parent_folder_id = "parentFolderId_example" # str | The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. (optional)
    parent_folder_path = "parentFolderPath_example" # str | The full path of the parent folder. Should start and end with a '/'. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. (optional)
    creation_date_after = "creationDateAfter_example" # str | The date after which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    creation_date_before = "creationDateBefore_example" # str | The date before which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_after = "statusDateAfter_example" # str | The date after which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_before = "statusDateBefore_example" # str | The date before which the status has been updated Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    user_tag = "userTag_example" # str | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. (optional)
    user_tag_match_mode = "EXACT" # str | How the usertags are filtered. (optional)
    run_input_tag = "runInputTag_example" # str | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_input_tag_match_mode = "EXACT" # str | How the runInputTags are filtered. (optional)
    run_output_tag = "runOutputTag_example" # str | The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_output_tag_match_mode = "EXACT" # str | How the runOutputTags are filtered. (optional)
    connector_tag = "connectorTag_example" # str | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. (optional)
    connector_tag_match_mode = "EXACT" # str | How the connectorTags are filtered. (optional)
    technical_tag = "technicalTag_example" # str | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. (optional)
    technical_tag_match_mode = "EXACT" # str | How the technicalTags are filtered. (optional)
    not_in_run = "notInRun_example" # str | When set to true, the data will be filtered on data which is not used in a run. (optional)
    not_linked_to_sample = "notLinkedToSample_example" # str | When set to true only date that is unlinked to a sample will be returned.  This filter implies a filter of type File. (optional)
    instrument_run_id = [
        "instrumentRunId_example",
    ] # [str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the list of bundle data.
        api_response = api_instance.get_bundle_data(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataApi->get_bundle_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the list of bundle data.
        api_response = api_instance.get_bundle_data(bundle_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataApi->get_bundle_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **full_text** | **str**| To search through multiple fields of data. | [optional]
 **id** | **str**| The ids to filter on. This will always match exact. | [optional]
 **filename** | **str**| The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. | [optional]
 **filename_match_mode** | **str**| How the filenames are filtered. | [optional]
 **file_path** | **str**| The paths of the files to filter on. | [optional]
 **file_path_match_mode** | **str**| How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it&#39;s sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). | [optional] if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
 **status** | **str**| The statuses to filter on. | [optional]
 **format_id** | **str**| The IDs of the formats to filter on. | [optional]
 **format_code** | **str**| The codes of the formats to filter on. | [optional]
 **type** | **str**| The type to filter on. | [optional]
 **parent_folder_id** | **str**| The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. | [optional]
 **parent_folder_path** | **str**| The full path of the parent folder. Should start and end with a &#39;/&#39;. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. | [optional]
 **creation_date_after** | **str**| The date after which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **creation_date_before** | **str**| The date before which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_after** | **str**| The date after which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_before** | **str**| The date before which the status has been updated Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **user_tag** | **str**| The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional]
 **user_tag_match_mode** | **str**| How the usertags are filtered. | [optional]
 **run_input_tag** | **str**| The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_input_tag_match_mode** | **str**| How the runInputTags are filtered. | [optional]
 **run_output_tag** | **str**| The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_output_tag_match_mode** | **str**| How the runOutputTags are filtered. | [optional]
 **connector_tag** | **str**| The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional]
 **connector_tag_match_mode** | **str**| How the connectorTags are filtered. | [optional]
 **technical_tag** | **str**| The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional]
 **technical_tag_match_mode** | **str**| How the technicalTags are filtered. | [optional]
 **not_in_run** | **str**| When set to true, the data will be filtered on data which is not used in a run. | [optional]
 **not_linked_to_sample** | **str**| When set to true only date that is unlinked to a sample will be returned.  This filter implies a filter of type File. | [optional]
 **instrument_run_id** | **[str]**| The instrument run IDs of the sequencing runs to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt | [optional]

### Return type

[**BundleDataPagedList**](BundleDataPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundle data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_data_to_bundle**
> link_data_to_bundle(bundle_id, data_id)

Link data to this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_api
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
    api_instance = bundle_data_api.BundleDataApi(api_client)
    bundle_id = "bundleId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Link data to this bundle.
        api_instance.link_data_to_bundle(bundle_id, data_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataApi->link_data_to_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **data_id** | **str**|  |

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
**204** | The data is successfully linked to this bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_data_from_bundle**
> unlink_data_from_bundle(bundle_id, data_id)

Unlink data from this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_data_api
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
    api_instance = bundle_data_api.BundleDataApi(api_client)
    bundle_id = "bundleId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink data from this bundle.
        api_instance.unlink_data_from_bundle(bundle_id, data_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleDataApi->unlink_data_from_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  |
 **data_id** | **str**|  |

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
**204** | The data is successfully unlinked from this bundle. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

