# libica.openapi.v2.ProjectDataApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_secondary_data**](ProjectDataApi.md#add_secondary_data) | **POST** /api/projects/{projectId}/data/{dataId}/secondaryData/{secondaryDataId} | Add secondary data to data.
[**archive_data**](ProjectDataApi.md#archive_data) | **POST** /api/projects/{projectId}/data/{dataId}:archive | Schedule this data for archival.
[**complete_folder_upload_session**](ProjectDataApi.md#complete_folder_upload_session) | **POST** /api/projects/{projectId}/data/{dataId}/folderUploadSessions/{folderUploadSessionId}:complete | Complete a trackable folder upload session.
[**create_data_in_project**](ProjectDataApi.md#create_data_in_project) | **POST** /api/projects/{projectId}/data | Create data in this project.
[**create_download_url_for_data**](ProjectDataApi.md#create_download_url_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createDownloadUrl | Retrieve a download URL for this data.
[**create_download_urls_for_data**](ProjectDataApi.md#create_download_urls_for_data) | **POST** /api/projects/{projectId}/data:createDownloadUrls | Retrieve download URLs for the data.
[**create_folder_upload_session**](ProjectDataApi.md#create_folder_upload_session) | **POST** /api/projects/{projectId}/data/{dataId}/folderUploadSessions | Create a trackable folder upload session.
[**create_inline_view_url_for_data**](ProjectDataApi.md#create_inline_view_url_for_data) | **POST** /api/projects/{projectId}/data/{dataId}:createInlineViewUrl | Retrieve an URL for this data to use for inline view in a browser.
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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    secondary_data_id = "secondaryDataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add secondary data to data.
        api_instance.add_secondary_data(project_id, data_id, secondary_data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule this data for archival.
        api_instance.archive_data(project_id, data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> FolderUploadSession complete_folder_upload_session(project_id, data_id, folder_upload_session_id)

Complete a trackable folder upload session.

Complete a trackable folder upload session. By completing the folder upload session, and specifying how many files you have uploaded, ICA can ensure that all uploaded files are accounted for.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.complete_folder_upload_session import CompleteFolderUploadSession
from libica.openapi.v2.model.folder_upload_session import FolderUploadSession
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    folder_upload_session_id = "folderUploadSessionId_example" # str | 
    complete_folder_upload_session = CompleteFolderUploadSession(
        number_of_expected_uploaded_files=1,
    ) # CompleteFolderUploadSession | The info required to complete the folder upload session. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Complete a trackable folder upload session.
        api_response = api_instance.complete_folder_upload_session(project_id, data_id, folder_upload_session_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->complete_folder_upload_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete a trackable folder upload session.
        api_response = api_instance.complete_folder_upload_session(project_id, data_id, folder_upload_session_id, complete_folder_upload_session=complete_folder_upload_session)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->complete_folder_upload_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_id** | **str**|  |
 **folder_upload_session_id** | **str**|  |
 **complete_folder_upload_session** | [**CompleteFolderUploadSession**](CompleteFolderUploadSession.md)| The info required to complete the folder upload session. | [optional]

### Return type

[**FolderUploadSession**](FolderUploadSession.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ProjectData create_data_in_project(project_id)

Create data in this project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.create_data import CreateData
from libica.openapi.v2.model.project_data import ProjectData
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    create_data = CreateData(
        name="name_example",
        folder_id="folder_id_example",
        folder_path="jUR,rZ#UM/?R,Fp^l6$ARj",
        format_code="format_code_example",
        data_type="FILE",
    ) # CreateData | The data to create. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create data in this project.
        api_response = api_instance.create_data_in_project(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_data_in_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create data in this project.
        api_response = api_instance.create_data_in_project(project_id, create_data=create_data)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_data_in_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_data** | [**CreateData**](CreateData.md)| The data to create. | [optional]

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.download import Download
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a download URL for this data.
        api_response = api_instance.create_download_url_for_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> DataUrlWithPathList create_download_urls_for_data(project_id)

Retrieve download URLs for the data.

Can be used to download files directly from the region where it is located, no connector is needed. Not applicable for Folders.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.data_id_or_path_list import DataIdOrPathList
from libica.openapi.v2.model.data_url_with_path_list import DataUrlWithPathList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id_or_path_list = DataIdOrPathList(
        data_ids=[
            "data_ids_example",
        ],
        data_paths=[
            "data_paths_example",
        ],
    ) # DataIdOrPathList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve download URLs for the data.
        api_response = api_instance.create_download_urls_for_data(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_download_urls_for_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve download URLs for the data.
        api_response = api_instance.create_download_urls_for_data(project_id, data_id_or_path_list=data_id_or_path_list)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_download_urls_for_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_id_or_path_list** | [**DataIdOrPathList**](DataIdOrPathList.md)|  | [optional]

### Return type

[**DataUrlWithPathList**](DataUrlWithPathList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The download URLs are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_upload_session**
> FolderUploadSession create_folder_upload_session(project_id, data_id)

Create a trackable folder upload session.

This endpoint can be used to ensure that all uploaded files within the requested session are accounted for. This call has to be used together with the :complete endpoint once upload is done.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.create_temporary_credentials import CreateTemporaryCredentials
from libica.openapi.v2.model.folder_upload_session import FolderUploadSession
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    create_temporary_credentials = CreateTemporaryCredentials(
        credentials_format="RCLONE",
    ) # CreateTemporaryCredentials | Temporary credentials request options. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a trackable folder upload session.
        api_response = api_instance.create_folder_upload_session(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_folder_upload_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a trackable folder upload session.
        api_response = api_instance.create_folder_upload_session(project_id, data_id, create_temporary_credentials=create_temporary_credentials)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The folder upload session is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inline_view_url_for_data**
> InlineView create_inline_view_url_for_data(project_id, data_id)

Retrieve an URL for this data to use for inline view in a browser.

Can be used to view a file directly from the region where it is located, no connector is needed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.inline_view import InlineView
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an URL for this data to use for inline view in a browser.
        api_response = api_instance.create_inline_view_url_for_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inline view URL is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_credentials_for_data**
> TempCredentials create_temporary_credentials_for_data(project_id, data_id)

Retrieve temporary credentials for this data.

Can be used to upload or download a file directly from the region where it is located, no connector is needed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.create_temporary_credentials import CreateTemporaryCredentials
from libica.openapi.v2.model.temp_credentials import TempCredentials
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    create_temporary_credentials = CreateTemporaryCredentials(
        credentials_format="RCLONE",
    ) # CreateTemporaryCredentials | Temporary credentials request options. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve temporary credentials for this data.
        api_response = api_instance.create_temporary_credentials_for_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_temporary_credentials_for_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve temporary credentials for this data.
        api_response = api_instance.create_temporary_credentials_for_data(project_id, data_id, create_temporary_credentials=create_temporary_credentials)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> Upload create_upload_url_for_data(project_id, data_id)

Retrieve an upload URL for this data.

Can be used to upload a file directly from the region where it is located, no connector is needed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.upload import Upload
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    file_type = "fileType_example" # str |  (optional)
    hash = "hash_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an upload URL for this data.
        api_response = api_instance.create_upload_url_for_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->create_upload_url_for_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an upload URL for this data.
        api_response = api_instance.create_upload_url_for_data(project_id, data_id, file_type=file_type, hash=hash)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule this data for deletion.
        api_instance.delete_data(project_id, data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> DataPagedList get_data_eligible_for_linking(project_id)

Retrieve a list of data eligible for linking to the current project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.data_paged_list import DataPagedList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    full_text = "fullText_example" # str | To search through multiple fields of data. (optional)
    id = [
        "id_example",
    ] # [str] | The ids to filter on. This will always match exact. (optional)
    filename = [
        "filename_example",
    ] # [str] | The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. (optional)
    filename_match_mode = "EXACT" # str | How the filenames are filtered.  (optional)
    file_path = [
        "filePath_example",
    ] # [str] | The paths of the files to filter on. (optional)
    file_path_match_mode = "STARTS_WITH_CASE_INSENSITIVE" # str | How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the 'filePath' parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it's sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the 'filePath' parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). (optional) if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
    status = [
        "PARTIAL",
    ] # [str] | The statuses to filter on. (optional)
    format_id = [
        "formatId_example",
    ] # [str] | The IDs of the formats to filter on. (optional)
    format_code = [
        "formatCode_example",
    ] # [str] | The codes of the formats to filter on. (optional)
    type = "FILE" # str | The type to filter on. (optional)
    parent_folder_id = [
        "parentFolderId_example",
    ] # [str] | The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. (optional)
    parent_folder_path = "parentFolderPath_example" # str | The full path of the parent folder. Should start and end with a '/'. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. (optional)
    creation_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date after which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    creation_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date before which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date after which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date before which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    user_tag = [
        "userTag_example",
    ] # [str] | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. (optional)
    user_tag_match_mode = "EXACT" # str | How the usertags are filtered.  (optional)
    run_input_tag = [
        "runInputTag_example",
    ] # [str] | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_input_tag_match_mode = "EXACT" # str | How the runInputTags are filtered.  (optional)
    run_output_tag = [
        "runOutputTag_example",
    ] # [str] | The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_output_tag_match_mode = "EXACT" # str | How the runOutputTags are filtered.  (optional)
    connector_tag = [
        "connectorTag_example",
    ] # [str] | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. (optional)
    connector_tag_match_mode = "EXACT" # str | How the connectorTags are filtered.  (optional)
    technical_tag = [
        "technicalTag_example",
    ] # [str] | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. (optional)
    technical_tag_match_mode = "EXACT" # str | How the technicalTags are filtered.  (optional)
    not_in_run = True # bool | When set to true, the data will be filtered on data which is not used in a run. (optional)
    not_linked_to_sample = True # bool | When set to true only data that is unlinked to a sample will be returned. This filter implies a filter of type File. (optional)
    instrument_run_id = [
        "instrumentRunId_example",
    ] # [str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of data eligible for linking to the current project.
        api_response = api_instance.get_data_eligible_for_linking(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_data_eligible_for_linking: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of data eligible for linking to the current project.
        api_response = api_instance.get_data_eligible_for_linking(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_data_eligible_for_linking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **full_text** | **str**| To search through multiple fields of data. | [optional]
 **id** | **[str]**| The ids to filter on. This will always match exact. | [optional]
 **filename** | **[str]**| The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. | [optional]
 **filename_match_mode** | **str**| How the filenames are filtered.  | [optional]
 **file_path** | **[str]**| The paths of the files to filter on. | [optional]
 **file_path_match_mode** | **str**| How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it&#39;s sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). | [optional] if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
 **status** | **[str]**| The statuses to filter on. | [optional]
 **format_id** | **[str]**| The IDs of the formats to filter on. | [optional]
 **format_code** | **[str]**| The codes of the formats to filter on. | [optional]
 **type** | **str**| The type to filter on. | [optional]
 **parent_folder_id** | **[str]**| The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. | [optional]
 **parent_folder_path** | **str**| The full path of the parent folder. Should start and end with a &#39;/&#39;. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. | [optional]
 **creation_date_after** | **datetime**| The date after which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **creation_date_before** | **datetime**| The date before which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_after** | **datetime**| The date after which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_before** | **datetime**| The date before which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **user_tag** | **[str]**| The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional]
 **user_tag_match_mode** | **str**| How the usertags are filtered.  | [optional]
 **run_input_tag** | **[str]**| The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_input_tag_match_mode** | **str**| How the runInputTags are filtered.  | [optional]
 **run_output_tag** | **[str]**| The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_output_tag_match_mode** | **str**| How the runOutputTags are filtered.  | [optional]
 **connector_tag** | **[str]**| The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional]
 **connector_tag_match_mode** | **str**| How the connectorTags are filtered.  | [optional]
 **technical_tag** | **[str]**| The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional]
 **technical_tag_match_mode** | **str**| How the technicalTags are filtered.  | [optional]
 **not_in_run** | **bool**| When set to true, the data will be filtered on data which is not used in a run. | [optional]
 **not_linked_to_sample** | **bool**| When set to true only data that is unlinked to a sample will be returned. This filter implies a filter of type File. | [optional]
 **instrument_run_id** | **[str]**| The instrument run IDs of the sequencing runs to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt | [optional]

### Return type

[**DataPagedList**](DataPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.folder_upload_session import FolderUploadSession
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    folder_upload_session_id = "folderUploadSessionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve folder upload session details.
        api_response = api_instance.get_folder_upload_session(project_id, data_id, folder_upload_session_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ProjectDataPagedList get_non_sample_project_data(project_id)

Retrieve a list of project data not linked to a sample.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of project data not linked to a sample.
        api_response = api_instance.get_non_sample_project_data(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_non_sample_project_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of project data not linked to a sample.
        api_response = api_instance.get_non_sample_project_data(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_non_sample_project_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_data import ProjectData
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project data.
        api_response = api_instance.get_project_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ProjectDataPagedList get_project_data_children(project_id, data_id)

Retrieve the children of this data.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3] Initial version ## [V4] Added pagination 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.data_list import DataList
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the children of this data.
        api_response = api_instance.get_project_data_children(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_children: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the children of this data.
        api_response = api_instance.get_project_data_children(project_id, data_id, page_offset=page_offset, page_token=page_token, page_size=page_size)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_children: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_id** | **str**|  |
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ProjectDataPagedList get_project_data_list(project_id)

Retrieve the list of project data.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    full_text = "fullText_example" # str | To search through multiple fields of data. (optional)
    id = [
        "id_example",
    ] # [str] | The ids to filter on. This will always match exact. (optional)
    filename = [
        "filename_example",
    ] # [str] | The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. (optional)
    filename_match_mode = "EXACT" # str | How the filenames are filtered.  (optional)
    file_path = [
        "filePath_example",
    ] # [str] | The paths of the files to filter on. (optional)
    file_path_match_mode = "STARTS_WITH_CASE_INSENSITIVE" # str | How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the 'filePath' parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it's sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the 'filePath' parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). (optional) if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
    status = [
        "PARTIAL",
    ] # [str] | The statuses to filter on. (optional)
    format_id = [
        "formatId_example",
    ] # [str] | The IDs of the formats to filter on. (optional)
    format_code = [
        "formatCode_example",
    ] # [str] | The codes of the formats to filter on. (optional)
    type = "FILE" # str | The type to filter on. (optional)
    parent_folder_id = [
        "parentFolderId_example",
    ] # [str] | The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. (optional)
    parent_folder_path = "parentFolderPath_example" # str | The full path of the parent folder. Should start and end with a '/'. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. (optional)
    creation_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date after which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    creation_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date before which the data is created. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date after which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    status_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date before which the status has been updated. Format: yyyy-MM-dd'T'HH:mm:ss'Z' eg: 2021-01-30T08:30:00Z (optional)
    user_tag = [
        "userTag_example",
    ] # [str] | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. (optional)
    user_tag_match_mode = "EXACT" # str | How the usertags are filtered.  (optional)
    run_input_tag = [
        "runInputTag_example",
    ] # [str] | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_input_tag_match_mode = "EXACT" # str | How the runInputTags are filtered.  (optional)
    run_output_tag = [
        "runOutputTag_example",
    ] # [str] | The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. (optional)
    run_output_tag_match_mode = "EXACT" # str | How the runOutputTags are filtered.  (optional)
    connector_tag = [
        "connectorTag_example",
    ] # [str] | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. (optional)
    connector_tag_match_mode = "EXACT" # str | How the connectorTags are filtered.  (optional)
    technical_tag = [
        "technicalTag_example",
    ] # [str] | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. (optional)
    technical_tag_match_mode = "EXACT" # str | How the technicalTags are filtered.  (optional)
    not_in_run = True # bool | When set to true, the data will be filtered on data which is not used in a run. (optional)
    not_linked_to_sample = True # bool | When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. (optional)
    instrument_run_id = [
        "instrumentRunId_example",
    ] # [str] | The instrument run IDs of the sequencing runs to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the list of project data.
        api_response = api_instance.get_project_data_list(project_id, full_text=full_text, id=id, filename=filename, filename_match_mode=filename_match_mode, file_path=file_path, file_path_match_mode=file_path_match_mode, status=status, format_id=format_id, format_code=format_code, type=type, parent_folder_id=parent_folder_id, parent_folder_path=parent_folder_path, creation_date_after=creation_date_after, creation_date_before=creation_date_before, status_date_after=status_date_after, status_date_before=status_date_before, user_tag=user_tag, user_tag_match_mode=user_tag_match_mode, run_input_tag=run_input_tag, run_input_tag_match_mode=run_input_tag_match_mode, run_output_tag=run_output_tag, run_output_tag_match_mode=run_output_tag_match_mode, connector_tag=connector_tag, connector_tag_match_mode=connector_tag_match_mode, technical_tag=technical_tag, technical_tag_match_mode=technical_tag_match_mode, not_in_run=not_in_run, not_linked_to_sample=not_linked_to_sample, instrument_run_id=instrument_run_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->get_project_data_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **full_text** | **str**| To search through multiple fields of data. | [optional]
 **id** | **[str]**| The ids to filter on. This will always match exact. | [optional]
 **filename** | **[str]**| The filenames to filter on. The filenameMatchMode-parameter determines how the filtering is done. | [optional]
 **filename_match_mode** | **str**| How the filenames are filtered.  | [optional]
 **file_path** | **[str]**| The paths of the files to filter on. | [optional]
 **file_path_match_mode** | **str**| How the file paths are filtered:   - STARTS_WITH_CASE_INSENSITIVE: Filters the file path to start with the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. This allows e.g. listing all data in a folder and all it&#39;s sub-folders (recursively).  - FULL_CASE_INSENSITIVE: Filters the file path to fully match the value of the &#39;filePath&#39; parameter, regardless of upper/lower casing. Note that this can result in multiple results if e.g. two files exist with the same filename but different casing (abc.txt and ABC.txt). | [optional] if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"
 **status** | **[str]**| The statuses to filter on. | [optional]
 **format_id** | **[str]**| The IDs of the formats to filter on. | [optional]
 **format_code** | **[str]**| The codes of the formats to filter on. | [optional]
 **type** | **str**| The type to filter on. | [optional]
 **parent_folder_id** | **[str]**| The IDs of parents folders to filter on. Lists all files and folders within the folder for the given ID, non-recursively. | [optional]
 **parent_folder_path** | **str**| The full path of the parent folder. Should start and end with a &#39;/&#39;. Lists all files and folders within the folder for the given path, non-recursively. This can be used to browse through the hierarchical tree of folders, e.g. traversing one level up can be done by removing the last part of the path. | [optional]
 **creation_date_after** | **datetime**| The date after which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **creation_date_before** | **datetime**| The date before which the data is created. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_after** | **datetime**| The date after which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **status_date_before** | **datetime**| The date before which the status has been updated. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional]
 **user_tag** | **[str]**| The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional]
 **user_tag_match_mode** | **str**| How the usertags are filtered.  | [optional]
 **run_input_tag** | **[str]**| The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_input_tag_match_mode** | **str**| How the runInputTags are filtered.  | [optional]
 **run_output_tag** | **[str]**| The runOutputTags to filter on. The runOutputTagMatchMode-parameter determines how the filtering is done. | [optional]
 **run_output_tag_match_mode** | **str**| How the runOutputTags are filtered.  | [optional]
 **connector_tag** | **[str]**| The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional]
 **connector_tag_match_mode** | **str**| How the connectorTags are filtered.  | [optional]
 **technical_tag** | **[str]**| The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional]
 **technical_tag_match_mode** | **str**| How the technicalTags are filtered.  | [optional]
 **not_in_run** | **bool**| When set to true, the data will be filtered on data which is not used in a run. | [optional]
 **not_linked_to_sample** | **bool**| When set to true only data that is unlinked to a sample will be returned.  This filter implies a filter of type File. | [optional]
 **instrument_run_id** | **[str]**| The instrument run IDs of the sequencing runs to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - timeCreated - timeModified - name - path - fileSizeInBytes - status - format - dataType - willBeArchivedAt - willBeDeletedAt | [optional]

### Return type

[**ProjectDataPagedList**](ProjectDataPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_list import ProjectList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of projects to which this data is linked.
        api_response = api_instance.get_projects_linked_to_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.data_list import DataList
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of secondary data for data.
        api_response = api_instance.get_secondary_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_data import ProjectData
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Link data to this project.
        api_response = api_instance.link_data_to_project(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    secondary_data_id = "secondaryDataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove secondary data from data.
        api_instance.remove_secondary_data(project_id, data_id, secondary_data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

Endpoint for scheduling a download for the data specified by the ID to a connector. This download will only start when the connector is running. This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.data_transfer import DataTransfer
from libica.openapi.v2.model.schedule_download import ScheduleDownload
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    schedule_download = ScheduleDownload(
        connector_id="connector_id_example",
        protocol="HTTPS",
        local_path="local_path_example",
        disable_hashing=True,
    ) # ScheduleDownload | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule a download.
        api_response = api_instance.schedule_download_for_data(project_id, data_id, schedule_download)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule this data for unarchival.
        api_instance.unarchive_data(project_id, data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink data from this project.
        api_instance.unlink_data_from_project(project_id, data_id)
    except libica.openapi.v2.ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ProjectData update_project_data(project_id, data_id)

Update this project data.

Fields which can be updated for files:  - data.willBeArchivedAt  - data.willBeDeletedAt  - data.format  - data.tags  Fields which can be updated for folders:  - data.tags  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_data_api
from libica.openapi.v2.model.project_data import ProjectData
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
    api_instance = project_data_api.ProjectDataApi(api_client)
    project_id = "projectId_example" # str | 
    data_id = "dataId_example" # str | 
    project_data = ProjectData(
        data=Data(
            id="id_example",
            urn="urn_example",
            details=DataDetails(
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                creator_id="creator_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                owning_project_id="owning_project_id_example",
                owning_project_name="owning_project_name_example",
                name="name_example",
                path="path_example",
                file_size_in_bytes=1,
                status="PARTIAL",
                tags=DataTag(
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
                    run_out_tags=[
                        "run_out_tags_example",
                    ],
                    reference_tags=[
                        "reference_tags_example",
                    ],
                ),
                format=DataFormat(
                    id="id_example",
                    time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    owner_id="owner_id_example",
                    tenant_id="tenant_id_example",
                    tenant_name="tenant_name_example",
                    code="code_example",
                    description="description_example",
                    mime_type="mime_type_example",
                ),
                data_type="FILE",
                object_e_tag="object_e_tag_example",
                stored_for_the_first_time_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                region=Region(
                    id="id_example",
                    time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    owner_id="owner_id_example",
                    tenant_id="tenant_id_example",
                    tenant_name="tenant_name_example",
                    code="code_example",
                    country=Country(
                        id="id_example",
                        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        owner_id="owner_id_example",
                        tenant_id="tenant_id_example",
                        tenant_name="tenant_name_example",
                        code="code_example",
                        name="name_example",
                        region="region_example",
                    ),
                    city_name="city_name_example",
                ),
                will_be_archived_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                will_be_deleted_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                sequencing_run=SequencingRun(
                    id="id_example",
                    instrument_run_id="instrument_run_id_example",
                    name="name_example",
                ),
            ),
        ),
        project_id="project_id_example",
    ) # ProjectData | The updated project data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update this project data.
        api_response = api_instance.update_project_data(project_id, data_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->update_project_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update this project data.
        api_response = api_instance.update_project_data(project_id, data_id, project_data=project_data)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectDataApi->update_project_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data_id** | **str**|  |
 **project_data** | [**ProjectData**](ProjectData.md)| The updated project data. | [optional]

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project data is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

