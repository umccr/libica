# libiap.openapi.libgds.FilesApi

All URIs are relative to *https://aps2.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_file**](FilesApi.md#archive_file) | **POST** /v1/files/{fileId}:archive | Archive a file
[**create_file**](FilesApi.md#create_file) | **POST** /v1/files | Create a file entry in GDS and get temporary credentials for upload
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /v1/files/{fileId} | Permanently delete a file
[**destroy_file_deprecated**](FilesApi.md#destroy_file_deprecated) | **DELETE** /v1/files/{fileId}:destroy | Permanently delete a file
[**get_file**](FilesApi.md#get_file) | **GET** /v1/files/{fileId} | Get details about a file, including a pre-signed URL for download
[**list_files**](FilesApi.md#list_files) | **GET** /v1/files | Get a list of files
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
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be archived.
body = libiap.openapi.libgds.FileArchiveRequest() # FileArchiveRequest | 

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

# **create_file**
> FileWriteableResponse create_file(body, include=include)

Create a file entry in GDS and get temporary credentials for upload

Create a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Volume ID or volume name is required for file creation. If a folder path is provided and does not exist, GDS creates the folder path in the appropriate account automatically.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    body = libiap.openapi.libgds.CreateFileRequest() # CreateFileRequest | 
include = 'include_example' # str | Comma-separated list of properties to include in the response ([include=[totalItemCount]).Example: include=totalItemCount (optional)

    try:
        # Create a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.create_file(body, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFileRequest**](CreateFileRequest.md)|  | 
 **include** | **str**| Comma-separated list of properties to include in the response ([include&#x3D;[totalItemCount]).Example: include&#x3D;totalItemCount | [optional] 

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
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
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

# **destroy_file_deprecated**
> destroy_file_deprecated(file_id)

Permanently delete a file

This endpoint will be deprecated with the EarlyAccess launch. Utilize DELETE: v1/files/{fileId} instead.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to delete.

    try:
        # Permanently delete a file
        api_instance.destroy_file_deprecated(file_id)
    except ApiException as e:
        print("Exception when calling FilesApi->destroy_file_deprecated: %s\n" % e)
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
> FileResponse get_file(file_id, tenant_id=tenant_id)

Get details about a file, including a pre-signed URL for download

Get information and details for the specified file ID, including metadata and a pre-signed URL for file download. The URL can be used as a curl command or directly with S3.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to retrieve.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)

    try:
        # Get details about a file, including a pre-signed URL for download
        api_response = api_instance.get_file(file_id, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to retrieve. | 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 

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
> FileListResponse list_files(volume_id=volume_id, volume_name=volume_name, path=path, is_uploaded=is_uploaded, archive_status=archive_status, recursive=recursive, page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id)

Get a list of files

Given a volumeId or volume name, get a list of files accessible by the JWT. The default sort returned is alphabetical, ascending. The default page size is 10 items

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    volume_id = ['volume_id_example'] # list[str] | Optional field that specifies comma-separated volume IDs to include in the list (optional)
volume_name = ['volume_name_example'] # list[str] | Optional field that specifies comma-separated volume names to include in the list (optional)
path = ['path_example'] # list[str] | Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). (optional)
is_uploaded = True # bool | Optional field to filter by Uploaded files (optional)
archive_status = 'archive_status_example' # str | Optional field that specifies comma-separated Archive Statuses to include in the list (optional)
recursive = True # bool | Optional field to specify if files should be returned recursively in and under the specified paths, or only directly in the specified paths (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | START_DESC END_DESC (optional)
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)

    try:
        # Get a list of files
        api_response = api_instance.list_files(volume_id=volume_id, volume_name=volume_name, path=path, is_uploaded=is_uploaded, archive_status=archive_status, recursive=recursive, page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id)
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
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **include** | **str**| START_DESC END_DESC | [optional] 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 

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

# **unarchive_file**
> FileResponse unarchive_file(file_id, body)

Unarchive a file

Unarchive a file from a lower storage cost tier.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be unarchived.
body = libiap.openapi.libgds.FileUnarchiveRequest() # FileUnarchiveRequest | 

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
> FileWriteableResponse update_file(file_id, include=include, body=body)

Update a file entry in GDS and get temporary credentials for upload

Update a file entry in GDS. Returns temporary credentials for file upload directly to S3 when the include=objectStoreAccess parameter is used. Note that the currently supported changes to the file resource are updating the file type and the underlying content.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import libiap.openapi.libgds
from libiap.openapi.libgds.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://aps2.platform.illumina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = libiap.openapi.libgds.Configuration(
    host = "https://aps2.platform.illumina.com",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with libiap.openapi.libgds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libiap.openapi.libgds.FilesApi(api_client)
    file_id = 'file_id_example' # str | Unique identifier for the file to be updated.
include = 'include_example' # str | Comma-separated list of properties to include in the response ([include=[totalItemCount]).Example: include=totalItemCount (optional)
body = libiap.openapi.libgds.UpdateFileRequest() # UpdateFileRequest |  (optional)

    try:
        # Update a file entry in GDS and get temporary credentials for upload
        api_response = api_instance.update_file(file_id, include=include, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Unique identifier for the file to be updated. | 
 **include** | **str**| Comma-separated list of properties to include in the response ([include&#x3D;[totalItemCount]).Example: include&#x3D;totalItemCount | [optional] 
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

