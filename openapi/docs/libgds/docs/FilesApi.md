# libica.openapi.libgds.FilesApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_file**](FilesApi.md#archive_file) | **POST** /v1/files/{fileId}:archive | Archive a file
[**bulk_file_update**](FilesApi.md#bulk_file_update) | **PATCH** /v1/files | Updates list of files with metadata
[**complete_file_upload**](FilesApi.md#complete_file_upload) | **POST** /v1/files/{fileId}:completeUpload | Complete a file Upload
[**copy_files**](FilesApi.md#copy_files) | **POST** /v1/files/copy | Copy list of files
[**create_file**](FilesApi.md#create_file) | **POST** /v1/files | Create a file entry in GDS and get temporary credentials for upload
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /v1/files/{fileId} | Permanently delete a file
[**get_file**](FilesApi.md#get_file) | **GET** /v1/files/{fileId} | Get details about a file, including a pre-signed URL for download
[**list_files**](FilesApi.md#list_files) | **GET** /v1/files | Get a list of files
[**list_volume_files**](FilesApi.md#list_volume_files) | **POST** /v1/files/list | Get a list of volume files
[**move_files**](FilesApi.md#move_files) | **POST** /v1/files/move | Move list of files
[**unarchive_file**](FilesApi.md#unarchive_file) | **POST** /v1/files/{fileId}:unarchive | Unarchive a file
[**update_file**](FilesApi.md#update_file) | **PATCH** /v1/files/{fileId} | Update a file entry in GDS and get temporary credentials for upload


# **archive_file**
> FileResponse archive_file(file_id, body)

Archive a file

Archives a file to a lower storage cost tier.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be archived.
body = libica.openapi.libgds.FileArchiveRequest() # FileArchiveRequest | 

    try:
        # Archive a file
        api_response = api_instance.archive_file(file_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->archive_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be archived. | 
 **body** | [**FileArchiveRequest**](FileArchiveRequest.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_file_update**
> BulkFileUpdateResponse bulk_file_update(body=body)

Updates list of files with metadata

Updates list of files with metadata

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    body = libica.openapi.libgds.BulkFileUpdateRequest() # BulkFileUpdateRequest |  (optional)

    try:
        # Updates list of files with metadata
        api_response = api_instance.bulk_file_update(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->bulk_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkFileUpdateRequest**](BulkFileUpdateRequest.md)|  | [optional] 

### Return type

[**BulkFileUpdateResponse**](BulkFileUpdateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**202** | Accepted |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_file_upload**
> FileResponse complete_file_upload(file_id, body)

Complete a file Upload

Complete a file upload operation. If the file was uploaded using multipart uploads, combine all the multiple parts uploaded into one complete file.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file upload to be completed.
body = libica.openapi.libgds.FileUploadCompleteRequest() # FileUploadCompleteRequest | 

    try:
        # Complete a file Upload
        api_response = api_instance.complete_file_upload(file_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->complete_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file upload to be completed. | 
 **body** | [**FileUploadCompleteRequest**](FileUploadCompleteRequest.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_files**
> JobResponse copy_files(body)

Copy list of files

Copies a list of files enumerated by file Ids to a destination folder

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    body = libica.openapi.libgds.FileListCopyRequest() # FileListCopyRequest | 

    try:
        # Copy list of files
        api_response = api_instance.copy_files(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->copy_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileListCopyRequest**](FileListCopyRequest.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileWriteableResponse create_file(body, include=include, upload_part_count=upload_part_count)

Create a file entry in GDS and get temporary credentials for upload

Create a file entry in GDS. Returns temporary credentials and presigned url(s) for file upload directly to S3 when the include=objectStoreAccess parameter is used. Volume ID or volume name is required for file creation. If a folder path is provided and does not exist, GDS creates the folder path in the appropriate account automatically.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    body = libica.openapi.libgds.CreateFileRequest() # CreateFileRequest | 
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)
upload_part_count = 56 # int | Optional number of parts for the presigned url for uploads (1 - 10000) (optional)

    try:
        # Create a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.create_file(body, include=include, upload_part_count=upload_part_count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFileRequest**](CreateFileRequest.md)|  | 
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional] 
 **upload_part_count** | **int**| Optional number of parts for the presigned url for uploads (1 - 10000) | [optional] 

### Return type

[**FileWriteableResponse**](FileWriteableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new File. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new File doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_id)

Permanently delete a file

Permanently delete a file entry and its underlying content

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to delete.

    try:
        # Permanently delete a file
        api_instance.delete_file(file_id)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to delete. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> FileResponse get_file(file_id, tenant_id=tenant_id, presigned_url_mode=presigned_url_mode, include_volume_metadata=include_volume_metadata, metadata_include=metadata_include, metadata_exclude=metadata_exclude, include=include)

Get details about a file, including a pre-signed URL for download

Get information and details for the specified file ID, including metadata and a pre-signed URL for file download. The URL can be used as a curl command or directly with S3.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to retrieve.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
presigned_url_mode = 'presigned_url_mode_example' # str | Optional parameter to specify presigned url's content-disposition. If not specified, the browser will determine the default behavior.              Possible values: Attachment, Inline, Browser (optional)
include_volume_metadata = True # bool | Optional parameter to return volume's metadata (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)

    try:
        # Get details about a file, including a pre-signed URL for download
        api_response = api_instance.get_file(file_id, tenant_id=tenant_id, presigned_url_mode=presigned_url_mode, include_volume_metadata=include_volume_metadata, metadata_include=metadata_include, metadata_exclude=metadata_exclude, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to retrieve. | 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **presigned_url_mode** | **str**| Optional parameter to specify presigned url&#39;s content-disposition. If not specified, the browser will determine the default behavior.              Possible values: Attachment, Inline, Browser | [optional] 
 **include_volume_metadata** | **bool**| Optional parameter to return volume&#39;s metadata | [optional] 
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional] 
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional] 
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional] 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> FileListResponse list_files(volume_id=volume_id, volume_name=volume_name, path=path, is_uploaded=is_uploaded, archive_status=archive_status, recursive=recursive, presigned_url_mode=presigned_url_mode, include=include, page_size=page_size, page_token=page_token, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)

Get a list of files

Given a volumeId or volume name, get a list of files accessible by the JWT. The default sort returned is alphabetical, ascending. The default page size is 10 items

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    volume_id = ['volume_id_example'] # list[str] | Optional field that specifies comma-separated volume IDs to include in the list (optional)
volume_name = ['volume_name_example'] # list[str] | Optional field that specifies comma-separated volume names to include in the list (optional)
path = ['path_example'] # list[str] | Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). (optional)
is_uploaded = True # bool | Optional field to filter by Uploaded files (optional)
archive_status = 'archive_status_example' # str | Optional field that specifies comma-separated Archive Statuses to include in the list (optional)
recursive = True # bool | Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths (optional)
presigned_url_mode = 'presigned_url_mode_example' # str | Optional parameter to specify presigned url's content-disposition. If not specified, the browser will determine the default behavior.  Possible values: Attachment, Inline, Browser (optional)
include = 'include_example' # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, PresignedUrl, InheritedAcl (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    try:
        # Get a list of files
        api_response = api_instance.list_files(volume_id=volume_id, volume_name=volume_name, path=path, is_uploaded=is_uploaded, archive_status=archive_status, recursive=recursive, presigned_url_mode=presigned_url_mode, include=include, page_size=page_size, page_token=page_token, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | [**list[str]**](str.md)| Optional field that specifies comma-separated volume IDs to include in the list | [optional] 
 **volume_name** | [**list[str]**](str.md)| Optional field that specifies comma-separated volume names to include in the list | [optional] 
 **path** | [**list[str]**](str.md)| Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). | [optional] 
 **is_uploaded** | **bool**| Optional field to filter by Uploaded files | [optional] 
 **archive_status** | **str**| Optional field that specifies comma-separated Archive Statuses to include in the list | [optional] 
 **recursive** | **bool**| Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths | [optional] 
 **presigned_url_mode** | **str**| Optional parameter to specify presigned url&#39;s content-disposition. If not specified, the browser will determine the default behavior.  Possible values: Attachment, Inline, Browser | [optional] 
 **include** | **str**| Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, PresignedUrl, InheritedAcl | [optional] 
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional] 
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional] 

### Return type

[**FileListResponse**](FileListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volume_files**
> VolumeFileListResponse list_volume_files(body)

Get a list of volume files

Gets file list by volume ID and an array of file IDs. The default sort returned is alphabetical, ascending

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    body = libica.openapi.libgds.VolumeFileListRequest() # VolumeFileListRequest | 

    try:
        # Get a list of volume files
        api_response = api_instance.list_volume_files(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_volume_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeFileListRequest**](VolumeFileListRequest.md)|  | 

### Return type

[**VolumeFileListResponse**](VolumeFileListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_files**
> JobResponse move_files(body)

Move list of files

Moves a list of files enumerated by file Ids to a destination folder

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    body = libica.openapi.libgds.FileListMoveRequest() # FileListMoveRequest | 

    try:
        # Move list of files
        api_response = api_instance.move_files(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->move_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileListMoveRequest**](FileListMoveRequest.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_file**
> FileResponse unarchive_file(file_id, body)

Unarchive a file

Unarchive a file from a lower storage cost tier.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be unarchived.
body = libica.openapi.libgds.FileUnarchiveRequest() # FileUnarchiveRequest | 

    try:
        # Unarchive a file
        api_response = api_instance.unarchive_file(file_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->unarchive_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be unarchived. | 
 **body** | [**FileUnarchiveRequest**](FileUnarchiveRequest.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**409** | Conflict. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileWriteableResponse update_file(file_id, include=include, upload_part_count=upload_part_count, body=body)

Update a file entry in GDS and get temporary credentials for upload

Update a file entry in GDS. Returns temporary credentials and presigned url(s) for file upload directly to S3 when the include=objectStoreAccess parameter is used. Note that the currently supported changes to the file resource are updating the file type and the underlying content.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libica.openapi.libgds
from libica.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libica.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be updated.
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)
upload_part_count = 56 # int | Optional number of parts for the presigned url for uploads (1 - 10000) (optional)
body = libica.openapi.libgds.UpdateFileRequest() # UpdateFileRequest |  (optional)

    try:
        # Update a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.update_file(file_id, include=include, upload_part_count=upload_part_count, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be updated. | 
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional] 
 **upload_part_count** | **int**| Optional number of parts for the presigned url for uploads (1 - 10000) | [optional] 
 **body** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | [optional] 

### Return type

[**FileWriteableResponse**](FileWriteableResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | File not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

