# libica.openapi.v3.ProjectDataApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_secondary_data**](ProjectDataApi.md#add_secondary_data) | **POST** /api/projects/{projectId}/data/{dataId}/secondaryData/{secondaryDataId} | Add secondary data to data.
[**archive_data**](ProjectDataApi.md#archive_data) | **POST** /api/projects/{projectId}/data/{dataId}:archive | Schedule this data for archival.
[**complete_folder_upload_session**](ProjectDataApi.md#complete_folder_upload_session) | **POST** /api/projects/{projectId}/data/{dataId}/folderUploadSessions/{folderUploadSessionId}:complete | Complete a trackable folder upload session.
[**create_data_in_project**](ProjectDataApi.md#create_data_in_project) | **POST** /api/projects/{projectId}/data | Create data in this project.
[**create_download_url_for_data**](ProjectDataApi.md#create_download_url_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createDownloadUrl | Retrieve a download URL for this data.
[**create_download_urls_for_data**](ProjectDataApi.md#create_download_urls_for_data) | **POST** /api/projects/{projectId}/data:createDownloadUrls | Retrieve download URLs for the data.
[**create_file**](ProjectDataApi.md#create_file) | **POST** /api/projects/{projectId}/data:createFile | Create a file in this project.
[**create_file_with_temporary_credentials**](ProjectDataApi.md#create_file_with_temporary_credentials) | **POST** /api/projects/{projectId}/data:createFileWithTemporaryCredentials | Create a file in this project, and retrieve temporary credentials for it.
[**create_file_with_upload_url**](ProjectDataApi.md#create_file_with_upload_url) | **POST** /api/projects/{projectId}/data:createFileWithUploadUrl | Create a file in this project, and retrieve an upload url for it.
[**create_folder**](ProjectDataApi.md#create_folder) | **POST** /api/projects/{projectId}/data:createFolder | Create a folder in this project.
[**create_folder_upload_session**](ProjectDataApi.md#create_folder_upload_session) | **POST** /api/projects/{projectId}/data/{dataId}/folderUploadSessions | Create a trackable folder upload session.
[**create_folder_with_temporary_credentials**](ProjectDataApi.md#create_folder_with_temporary_credentials) | **POST** /api/projects/{projectId}/data:createFolderWithTemporaryCredentials | Create a folder in this project, and and retrieve temporary credentials for it.
[**create_folder_with_upload_session**](ProjectDataApi.md#create_folder_with_upload_session) | **POST** /api/projects/{projectId}/data:createFolderWithUploadSession | Create a folder in this project, and create a trackable folder upload session.
[**create_inline_view_url_for_data**](ProjectDataApi.md#create_inline_view_url_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createInlineViewUrl | Retrieve an URL for this data to use for inline view in a browser.
[**create_non_indexed_folder**](ProjectDataApi.md#create_non_indexed_folder) | **POST** /api/projects/{projectId}/data:createNonIndexedFolder | Create a non indexed folder in this project. The folder will be created as a top-level folder.
[**create_temporary_credentials_for_data**](ProjectDataApi.md#create_temporary_credentials_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createTemporaryCredentials | Retrieve temporary credentials for this data.
[**create_upload_url_for_data**](ProjectDataApi.md#create_upload_url_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createUploadUrl | Retrieve an upload URL for this data.
[**delete_data**](ProjectDataApi.md#delete_data) | **POST** /api/projects/{projectId}/data/{dataId}:delete | Schedule this data for deletion.
[**get_data_eligible_for_linking**](ProjectDataApi.md#get_data_eligible_for_linking) | **GET** /api/projects/{projectId}/data/eligibleForLinking | Retrieve a list of data eligible for linking to the current project.
[**get_folder_upload_session**](ProjectDataApi.md#get_folder_upload_session) | **GET** /api/projects/{projectId}/data/{dataId}/folderUploadSessions/{folderUploadSessionId} | Retrieve folder upload session details.
[**get_non_sample_project_data**](ProjectDataApi.md#get_non_sample_project_data) | **GET** /api/projects/{projectId}/data/nonSampleData | Retrieve a list of project data not linked to a sample.
[**get_project_data**](ProjectDataApi.md#get_project_data) | **GET** /api/projects/{projectId}/data/{dataId} | Retrieve a project data.
[**get_project_data_children**](ProjectDataApi.md#get_project_data_children) | **GET** /api/projects/{projectId}/data/{dataId}/children | Retrieve the children of this data.
[**get_project_data_list**](ProjectDataApi.md#get_project_data_list) | **GET** /api/projects/{projectId}/data | Retrieve the list of project data.
[**get_projects_linked_to_data**](ProjectDataApi.md#get_projects_linked_to_data) | **GET** /api/projects/{projectId}/data/{dataId}/linkedProjects | Retrieve a list of projects to which this data is linked.
[**get_secondary_data**](ProjectDataApi.md#get_secondary_data) | **GET** /api/projects/{projectId}/data/{dataId}/secondaryData | Retrieve a list of secondary data for data.
[**link_data_to_project**](ProjectDataApi.md#link_data_to_project) | **POST** /api/projects/{projectId}/data/{dataId} | Link data to this project.
[**remove_secondary_data**](ProjectDataApi.md#remove_secondary_data) | **DELETE** /api/projects/{projectId}/data/{dataId}/secondaryData/{secondaryDataId} | Remove secondary data from data.
[**schedule_download_for_data**](ProjectDataApi.md#schedule_download_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:scheduleDownload | Schedule a download.
[**unarchive_data**](ProjectDataApi.md#unarchive_data) | **POST** /api/projects/{projectId}/data/{dataId}:unarchive | Schedule this data for unarchival.
[**unlink_data_from_project**](ProjectDataApi.md#unlink_data_from_project) | **POST** /api/projects/{projectId}/data/{dataId}:unlink | Unlink data from this project.
[**update_project_data**](ProjectDataApi.md#update_project_data) | **PUT** /api/projects/{projectId}/data/{dataId} | Update this project data.


# **add_secondary_data**
> add_secondary_data(project_id, data_id, secondary_data_id)

Add secondary data to data.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    secondary_data_id = 'secondary_data_id_example' # str | 

    try:
        # Add secondary data to data.
        api_instance.add_secondary_data(project_id, data_id, secondary_data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->add_secondary_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **secondary_data_id** | **str**|  | 

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
**204** | The secondary data is successfully added. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_data**
> archive_data(project_id, data_id)

Schedule this data for archival.

Endpoint for scheduling this data for archival. This will also archive all files and directories below that data.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Schedule this data for archival.
        api_instance.archive_data(project_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->archive_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

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
**204** | The data is successfully scheduled for archival. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_folder_upload_session**
> FolderUploadSession complete_folder_upload_session(project_id, data_id, folder_upload_session_id, complete_folder_upload_session)

Complete a trackable folder upload session.

Complete a trackable folder upload session. By completing the folder upload session, and specifying how many files you have uploaded, ICA can ensure that all uploaded files are accounted for.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.complete_folder_upload_session import CompleteFolderUploadSession
from libica.openapi.v3.models.folder_upload_session import FolderUploadSession
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    folder_upload_session_id = 'folder_upload_session_id_example' # str | 
    complete_folder_upload_session = libica.openapi.v3.CompleteFolderUploadSession() # CompleteFolderUploadSession | The info required to complete the folder upload session.

    try:
        # Complete a trackable folder upload session.
        api_response = api_instance.complete_folder_upload_session(project_id, data_id, folder_upload_session_id, complete_folder_upload_session)
        print("The response of ProjectDataApi->complete_folder_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->complete_folder_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **folder_upload_session_id** | **str**|  | 
 **complete_folder_upload_session** | [**CompleteFolderUploadSession**](CompleteFolderUploadSession.md)| The info required to complete the folder upload session. | 

### Return type

[**FolderUploadSession**](FolderUploadSession.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The folder upload session is successfully completed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_in_project**
> ProjectData create_data_in_project(project_id, create_data, idempotency_key=idempotency_key)

Create data in this project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_data import CreateData
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_data = libica.openapi.v3.CreateData() # CreateData | The data to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create data in this project.
        api_response = api_instance.create_data_in_project(project_id, create_data, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_data_in_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_data_in_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_data** | [**CreateData**](CreateData.md)| The data to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully created in this project. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download_url_for_data**
> Download create_download_url_for_data(project_id, data_id)

Retrieve a download URL for this data.

Can be used to download a file directly from the region where it is located, no connector is needed. Not applicable for Folder.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.download import Download
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Retrieve a download URL for this data.
        api_response = api_instance.create_download_url_for_data(project_id, data_id)
        print("The response of ProjectDataApi->create_download_url_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_download_url_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

### Return type

[**Download**](Download.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download_urls_for_data**
> DataUrlWithPathList create_download_urls_for_data(project_id, data_id_or_path_list)

Retrieve download URLs for the data.

Can be used to download files directly from the region where it is located, no connector is needed. Not applicable for Folders.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.data_id_or_path_list import DataIdOrPathList
from libica.openapi.v3.models.data_url_with_path_list import DataUrlWithPathList
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id_or_path_list = libica.openapi.v3.DataIdOrPathList() # DataIdOrPathList | 

    try:
        # Retrieve download URLs for the data.
        api_response = api_instance.create_download_urls_for_data(project_id, data_id_or_path_list)
        print("The response of ProjectDataApi->create_download_urls_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_download_urls_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id_or_path_list** | [**DataIdOrPathList**](DataIdOrPathList.md)|  | 

### Return type

[**DataUrlWithPathList**](DataUrlWithPathList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download URLs are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> ProjectData create_file(project_id, create_file_data, idempotency_key=idempotency_key)

Create a file in this project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_file_data import CreateFileData
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_file_data = libica.openapi.v3.CreateFileData() # CreateFileData | The file to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a file in this project.
        api_response = api_instance.create_file(project_id, create_file_data, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_file_data** | [**CreateFileData**](CreateFileData.md)| The file to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The file is successfully created in this project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_with_temporary_credentials**
> ProjectDataAndTemporaryCredentials create_file_with_temporary_credentials(project_id, create_file_and_temporary_credentials, idempotency_key=idempotency_key)

Create a file in this project, and retrieve temporary credentials for it.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_file_and_temporary_credentials import CreateFileAndTemporaryCredentials
from libica.openapi.v3.models.project_data_and_temporary_credentials import ProjectDataAndTemporaryCredentials
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_file_and_temporary_credentials = libica.openapi.v3.CreateFileAndTemporaryCredentials() # CreateFileAndTemporaryCredentials | The data to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a file in this project, and retrieve temporary credentials for it.
        api_response = api_instance.create_file_with_temporary_credentials(project_id, create_file_and_temporary_credentials, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_file_with_temporary_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_file_with_temporary_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_file_and_temporary_credentials** | [**CreateFileAndTemporaryCredentials**](CreateFileAndTemporaryCredentials.md)| The data to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectDataAndTemporaryCredentials**](ProjectDataAndTemporaryCredentials.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully created in this project, and the temporary credentials are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_with_upload_url**
> ProjectFileAndUploadUrl create_file_with_upload_url(project_id, create_file_and_upload_url, idempotency_key=idempotency_key)

Create a file in this project, and retrieve an upload url for it.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_file_and_upload_url import CreateFileAndUploadUrl
from libica.openapi.v3.models.project_file_and_upload_url import ProjectFileAndUploadUrl
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_file_and_upload_url = libica.openapi.v3.CreateFileAndUploadUrl() # CreateFileAndUploadUrl | The data to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a file in this project, and retrieve an upload url for it.
        api_response = api_instance.create_file_with_upload_url(project_id, create_file_and_upload_url, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_file_with_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_file_with_upload_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_file_and_upload_url** | [**CreateFileAndUploadUrl**](CreateFileAndUploadUrl.md)| The data to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectFileAndUploadUrl**](ProjectFileAndUploadUrl.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully created in this project, and the upload URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> ProjectData create_folder(project_id, create_folder, idempotency_key=idempotency_key)

Create a folder in this project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_folder import CreateFolder
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_folder = libica.openapi.v3.CreateFolder() # CreateFolder | The folder to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a folder in this project.
        api_response = api_instance.create_folder(project_id, create_folder, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_folder** | [**CreateFolder**](CreateFolder.md)| The folder to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The folder is successfully created in this project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_upload_session**
> FolderUploadSession create_folder_upload_session(project_id, data_id, create_temporary_credentials=create_temporary_credentials)

Create a trackable folder upload session.

This endpoint can be used to ensure that all uploaded files within the requested session are accounted for. This call has to be used together with the :complete endpoint once upload is done.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_temporary_credentials import CreateTemporaryCredentials
from libica.openapi.v3.models.folder_upload_session import FolderUploadSession
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    create_temporary_credentials = libica.openapi.v3.CreateTemporaryCredentials() # CreateTemporaryCredentials | Temporary credentials request options. (optional)

    try:
        # Create a trackable folder upload session.
        api_response = api_instance.create_folder_upload_session(project_id, data_id, create_temporary_credentials=create_temporary_credentials)
        print("The response of ProjectDataApi->create_folder_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_folder_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **create_temporary_credentials** | [**CreateTemporaryCredentials**](CreateTemporaryCredentials.md)| Temporary credentials request options. | [optional] 

### Return type

[**FolderUploadSession**](FolderUploadSession.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The folder upload session is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_with_temporary_credentials**
> ProjectDataAndTemporaryCredentials create_folder_with_temporary_credentials(project_id, create_folder_and_temporary_credentials, idempotency_key=idempotency_key)

Create a folder in this project, and and retrieve temporary credentials for it.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_folder_and_temporary_credentials import CreateFolderAndTemporaryCredentials
from libica.openapi.v3.models.project_data_and_temporary_credentials import ProjectDataAndTemporaryCredentials
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_folder_and_temporary_credentials = libica.openapi.v3.CreateFolderAndTemporaryCredentials() # CreateFolderAndTemporaryCredentials | The data to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a folder in this project, and and retrieve temporary credentials for it.
        api_response = api_instance.create_folder_with_temporary_credentials(project_id, create_folder_and_temporary_credentials, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_folder_with_temporary_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_folder_with_temporary_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_folder_and_temporary_credentials** | [**CreateFolderAndTemporaryCredentials**](CreateFolderAndTemporaryCredentials.md)| The data to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectDataAndTemporaryCredentials**](ProjectDataAndTemporaryCredentials.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully created in this project, and the temporary credentials are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_with_upload_session**
> ProjectFolderAndUploadSession create_folder_with_upload_session(project_id, create_folder_and_temporary_credentials, idempotency_key=idempotency_key)

Create a folder in this project, and create a trackable folder upload session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_folder_and_temporary_credentials import CreateFolderAndTemporaryCredentials
from libica.openapi.v3.models.project_folder_and_upload_session import ProjectFolderAndUploadSession
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_folder_and_temporary_credentials = libica.openapi.v3.CreateFolderAndTemporaryCredentials() # CreateFolderAndTemporaryCredentials | The data to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a folder in this project, and create a trackable folder upload session.
        api_response = api_instance.create_folder_with_upload_session(project_id, create_folder_and_temporary_credentials, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_folder_with_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_folder_with_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_folder_and_temporary_credentials** | [**CreateFolderAndTemporaryCredentials**](CreateFolderAndTemporaryCredentials.md)| The data to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectFolderAndUploadSession**](ProjectFolderAndUploadSession.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully created in this project, and the folder upload session is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inline_view_url_for_data**
> InlineView create_inline_view_url_for_data(project_id, data_id)

Retrieve an URL for this data to use for inline view in a browser.

Can be used to view a file directly from the region where it is located, no connector is needed.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.inline_view import InlineView
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Retrieve an URL for this data to use for inline view in a browser.
        api_response = api_instance.create_inline_view_url_for_data(project_id, data_id)
        print("The response of ProjectDataApi->create_inline_view_url_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_inline_view_url_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

### Return type

[**InlineView**](InlineView.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inline view URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_indexed_folder**
> ProjectData create_non_indexed_folder(project_id, create_non_indexed_folder, idempotency_key=idempotency_key)

Create a non indexed folder in this project. The folder will be created as a top-level folder.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_non_indexed_folder import CreateNonIndexedFolder
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    create_non_indexed_folder = libica.openapi.v3.CreateNonIndexedFolder() # CreateNonIndexedFolder | The non indexed folder to create.
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    try:
        # Create a non indexed folder in this project. The folder will be created as a top-level folder.
        api_response = api_instance.create_non_indexed_folder(project_id, create_non_indexed_folder, idempotency_key=idempotency_key)
        print("The response of ProjectDataApi->create_non_indexed_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_non_indexed_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_non_indexed_folder** | [**CreateNonIndexedFolder**](CreateNonIndexedFolder.md)| The non indexed folder to create. | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional] 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The non indexed folder is successfully created in this project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_credentials_for_data**
> TempCredentials create_temporary_credentials_for_data(project_id, data_id, create_temporary_credentials=create_temporary_credentials)

Retrieve temporary credentials for this data.

Can be used to upload or download a file directly from the region where it is located, no connector is needed. The returned credentials expire after 36 hours.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_temporary_credentials import CreateTemporaryCredentials
from libica.openapi.v3.models.temp_credentials import TempCredentials
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    create_temporary_credentials = libica.openapi.v3.CreateTemporaryCredentials() # CreateTemporaryCredentials | Temporary credentials request options. (optional)

    try:
        # Retrieve temporary credentials for this data.
        api_response = api_instance.create_temporary_credentials_for_data(project_id, data_id, create_temporary_credentials=create_temporary_credentials)
        print("The response of ProjectDataApi->create_temporary_credentials_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_temporary_credentials_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **create_temporary_credentials** | [**CreateTemporaryCredentials**](CreateTemporaryCredentials.md)| Temporary credentials request options. | [optional] 

### Return type

[**TempCredentials**](TempCredentials.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The temporary credentials are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_url_for_data**
> Upload create_upload_url_for_data(project_id, data_id, file_type=file_type, hash=hash)

Retrieve an upload URL for this data.

Can be used to upload a file directly from the region where it is located, no connector is needed. The project identifier must match the project which owns the data. You can create both new files and overwrite files in status 'partial'.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.upload import Upload
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    file_type = 'file_type_example' # str |  (optional)
    hash = 'hash_example' # str |  (optional)

    try:
        # Retrieve an upload URL for this data.
        api_response = api_instance.create_upload_url_for_data(project_id, data_id, file_type=file_type, hash=hash)
        print("The response of ProjectDataApi->create_upload_url_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->create_upload_url_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **file_type** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 

### Return type

[**Upload**](Upload.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upload URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data**
> delete_data(project_id, data_id)

Schedule this data for deletion.

Endpoint for scheduling this data for deletion. This will also delete all files and directories below that data.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Schedule this data for deletion.
        api_instance.delete_data(project_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->delete_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

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
**204** | The data is successfully scheduled for deletion. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_eligible_for_linking**
> DataPagedList get_data_eligible_for_linking(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve a list of data eligible for linking to the current project.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
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
    not_linked_to_sample = True # bool | When set to true only data that is unlinked to a sample will be returned. This filter implies a filter of type File. (optional)
    instrument_run_id = ['instrument_run_id_example'] # List[str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    try:
        # Retrieve a list of data eligible for linking to the current project.
        api_response = api_instance.get_data_eligible_for_linking(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectDataApi->get_data_eligible_for_linking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_data_eligible_for_linking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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
 **not_linked_to_sample** | **bool**| When set to true only data that is unlinked to a sample will be returned. This filter implies a filter of type File. | [optional] 
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
**200** | The list of data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_upload_session**
> FolderUploadSession get_folder_upload_session(project_id, data_id, folder_upload_session_id)

Retrieve folder upload session details.

Retrieve folder upload session details, including the current status of your upload session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.folder_upload_session import FolderUploadSession
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    folder_upload_session_id = 'folder_upload_session_id_example' # str | 

    try:
        # Retrieve folder upload session details.
        api_response = api_instance.get_folder_upload_session(project_id, data_id, folder_upload_session_id)
        print("The response of ProjectDataApi->get_folder_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_folder_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **folder_upload_session_id** | **str**|  | 

### Return type

[**FolderUploadSession**](FolderUploadSession.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The folder upload session details are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_sample_project_data**
> ProjectDataPagedList get_non_sample_project_data(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size)

Retrieve a list of project data not linked to a sample.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_paged_list import ProjectDataPagedList
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    try:
        # Retrieve a list of project data not linked to a sample.
        api_response = api_instance.get_non_sample_project_data(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size)
        print("The response of ProjectDataApi->get_non_sample_project_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_non_sample_project_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data**
> ProjectData get_project_data(project_id, data_id)

Retrieve a project data.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Retrieve a project data.
        api_response = api_instance.get_project_data(project_id, data_id)
        print("The response of ProjectDataApi->get_project_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_project_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_children**
> ProjectDataPagedList get_project_data_children(project_id, data_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size)

Retrieve the children of this data.

# Changelog
For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.

## [V3]
Initial version
## [V4]
Added pagination


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_paged_list import ProjectDataPagedList
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    full_text = 'full_text_example' # str | To search through multiple fields of data. (optional)
    id = ['id_example'] # List[str] | The ids to filter on. This will always match exact. (optional)
    filename = ['filename_example'] # List[str] | The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. (optional)
    filename_match_mode = 'filename_match_mode_example' # str | How the filenames are filtered.  (optional)
    status = ['status_example'] # List[str] | The statuses to filter on. (optional)
    format_id = ['format_id_example'] # List[str] | The IDs of the formats to filter on. (optional)
    format_code = ['format_code_example'] # List[str] | The codes of the formats to filter on. (optional)
    type = 'type_example' # str | The type to filter on. (optional)
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
    not_linked_to_sample = True # bool | When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. (optional)
    instrument_run_id = ['instrument_run_id_example'] # List[str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)

    try:
        # Retrieve the children of this data.
        api_response = api_instance.get_project_data_children(project_id, data_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size)
        print("The response of ProjectDataApi->get_project_data_children:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_project_data_children: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **full_text** | **str**| To search through multiple fields of data. | [optional] 
 **id** | [**List[str]**](str.md)| The ids to filter on. This will always match exact. | [optional] 
 **filename** | [**List[str]**](str.md)| The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. | [optional] 
 **filename_match_mode** | **str**| How the filenames are filtered.  | [optional] 
 **status** | [**List[str]**](str.md)| The statuses to filter on. | [optional] 
 **format_id** | [**List[str]**](str.md)| The IDs of the formats to filter on. | [optional] 
 **format_code** | [**List[str]**](str.md)| The codes of the formats to filter on. | [optional] 
 **type** | **str**| The type to filter on. | [optional] 
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
 **not_linked_to_sample** | **bool**| When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. | [optional] 
 **instrument_run_id** | [**List[str]**](str.md)| The instrument run IDs of the sequencing runs to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of data children is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_list**
> ProjectDataPagedList get_project_data_list(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, non_indexed_folders=non_indexed_folders, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, owning_project_id=owning_project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of project data.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data_paged_list import ProjectDataPagedList
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
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
    non_indexed_folders = True # bool | To filter on non-indexed folders. (optional)
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
    not_linked_to_sample = True # bool | When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. (optional)
    instrument_run_id = ['instrument_run_id_example'] # List[str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    owning_project_id = ['owning_project_id_example'] # List[str] | The owning project ID to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, non_indexed_folders=non_indexed_folders, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, owning_project_id=owning_project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectDataApi->get_project_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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
 **non_indexed_folders** | **bool**| To filter on non-indexed folders. | [optional] 
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
 **not_linked_to_sample** | **bool**| When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. | [optional] 
 **instrument_run_id** | [**List[str]**](str.md)| The instrument run IDs of the sequencing runs to filter on. | [optional] 
 **owning_project_id** | [**List[str]**](str.md)| The owning project ID to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt | [optional] 

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_linked_to_data**
> ProjectList get_projects_linked_to_data(project_id, data_id)

Retrieve a list of projects to which this data is linked.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Retrieve a list of projects to which this data is linked.
        api_response = api_instance.get_projects_linked_to_data(project_id, data_id)
        print("The response of ProjectDataApi->get_projects_linked_to_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_projects_linked_to_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

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

# **get_secondary_data**
> DataList get_secondary_data(project_id, data_id)

Retrieve a list of secondary data for data.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.data_list import DataList
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Retrieve a list of secondary data for data.
        api_response = api_instance.get_secondary_data(project_id, data_id)
        print("The response of ProjectDataApi->get_secondary_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->get_secondary_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

### Return type

[**DataList**](DataList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of secondary data is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_data_to_project**
> ProjectData link_data_to_project(project_id, data_id)

Link data to this project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Link data to this project.
        api_response = api_instance.link_data_to_project(project_id, data_id)
        print("The response of ProjectDataApi->link_data_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->link_data_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The data is successfully linked to the project. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_secondary_data**
> remove_secondary_data(project_id, data_id, secondary_data_id)

Remove secondary data from data.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    secondary_data_id = 'secondary_data_id_example' # str | 

    try:
        # Remove secondary data from data.
        api_instance.remove_secondary_data(project_id, data_id, secondary_data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->remove_secondary_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **secondary_data_id** | **str**|  | 

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
**204** | The secondary data is successfully removed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_download_for_data**
> DataTransfer schedule_download_for_data(project_id, data_id, schedule_download)

Schedule a download.

Endpoint for scheduling a download for the data specified by the ID to a connector. This download will only start when the connector is running. Data transfers for folder contents are created asynchronously, meaning that they will not be immediately visible in the project data transfers end point. Note: The localPath field is optional. When omitted or invalid, the download rules of the connector are followed.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.data_transfer import DataTransfer
from libica.openapi.v3.models.schedule_download import ScheduleDownload
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    schedule_download = libica.openapi.v3.ScheduleDownload() # ScheduleDownload | 

    try:
        # Schedule a download.
        api_response = api_instance.schedule_download_for_data(project_id, data_id, schedule_download)
        print("The response of ProjectDataApi->schedule_download_for_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->schedule_download_for_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **schedule_download** | [**ScheduleDownload**](ScheduleDownload.md)|  | 

### Return type

[**DataTransfer**](DataTransfer.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The datatransfer which is scheduled. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_data**
> unarchive_data(project_id, data_id)

Schedule this data for unarchival.

Endpoint for scheduling this data for unarchival. This will also unarchive all files and directories below that data. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Schedule this data for unarchival.
        api_instance.unarchive_data(project_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->unarchive_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

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
**204** | The data is successfully scheduled for unarchival. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_data_from_project**
> unlink_data_from_project(project_id, data_id)

Unlink data from this project.

Note that for folders, this only unlinks the folder itself, not the folder contents!  Use 'Project Data Unlinking Batch' for recursive unlinking.

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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 

    try:
        # Unlink data from this project.
        api_instance.unlink_data_from_project(project_id, data_id)
    except Exception as e:
        print("Exception when calling ProjectDataApi->unlink_data_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 

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
**204** | The data is successfully unlinked from this project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_data**
> ProjectData update_project_data(project_id, data_id, project_data)

Update this project data.

Fields which can be updated for files:
 - data.willBeArchivedAt
 - data.willBeDeletedAt
 - data.format
 - data.tags

Fields which can be updated for folders:
 - data.tags



### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_data import ProjectData
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
    api_instance = libica.openapi.v3.ProjectDataApi(api_client)
    project_id = 'project_id_example' # str | 
    data_id = 'data_id_example' # str | 
    project_data = libica.openapi.v3.ProjectData() # ProjectData | The updated project data.

    try:
        # Update this project data.
        api_response = api_instance.update_project_data(project_id, data_id, project_data)
        print("The response of ProjectDataApi->update_project_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDataApi->update_project_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_id** | **str**|  | 
 **project_data** | [**ProjectData**](ProjectData.md)| The updated project data. | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

