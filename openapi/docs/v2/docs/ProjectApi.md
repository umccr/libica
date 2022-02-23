# libica.openapi.v2.ProjectApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /api/projects | Create a new project.
[**get_project**](ProjectApi.md#get_project) | **GET** /api/projects/{projectId} | Retrieve a project.
[**get_projects**](ProjectApi.md#get_projects) | **GET** /api/projects | Retrieve a list of projects.
[**update_project**](ProjectApi.md#update_project) | **PUT** /api/projects/{projectId} | Update a project.


# **create_project**
> Project create_project()

Create a new project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_api
from libica.openapi.v2.model.project import Project
from libica.openapi.v2.model.create_project import CreateProject
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
    api_instance = project_api.ProjectApi(api_client)
    create_project = CreateProject(
        name="AH",
        short_description="short_description_example",
        information="information_example",
        project_owner_id="project_owner_id_example",
        region_id="region_id_example",
        billing_mode="PROJECT",
        data_sharing_enabled=True,
        tags=ProjectTag(
            technical_tags=[
                "technical_tags_example",
            ],
            user_tags=[
                "user_tags_example",
            ],
        ),
        storage_bundle_id="storage_bundle_id_example",
        metadata_model_id="metadata_model_id_example",
        storage_configuration_id="storage_configuration_id_example",
        storage_configuration_subfolder="storage_configuration_subfolder_example",
    ) # CreateProject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new project.
        api_response = api_instance.create_project(create_project=create_project)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project** | [**CreateProject**](CreateProject.md)|  | [optional]

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The project is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Retrieve a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_api
from libica.openapi.v2.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project.
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> ProjectPagedList get_projects()

Retrieve a list of projects.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_api
from libica.openapi.v2.model.project_paged_list import ProjectPagedList
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
    api_instance = project_api.ProjectApi(api_client)
    search = "search_example" # str | Search (optional)
    user_tags = [
        "userTags_example",
    ] # [str] | User tags to filter on (optional)
    technical_tags = [
        "technicalTags_example",
    ] # [str] | Technical tags to filter on (optional)
    include_hidden_projects = False # bool, none_type | Include hidden projects. (optional) if omitted the server will use the default value of False
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - name - shortDescription - information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of projects.
        api_response = api_instance.get_projects(search=search, user_tags=user_tags, technical_tags=technical_tags, include_hidden_projects=include_hidden_projects, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search | [optional]
 **user_tags** | **[str]**| User tags to filter on | [optional]
 **technical_tags** | **[str]**| Technical tags to filter on | [optional]
 **include_hidden_projects** | **bool, none_type**| Include hidden projects. | [optional] if omitted the server will use the default value of False
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - name - shortDescription - information | [optional]

### Return type

[**ProjectPagedList**](ProjectPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of projects is successfully retrieved |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id)

Update a project.

Fields which can be updated: - shortDescription - projectInformation - billingMode - dataSharingEnabled - tags - storageBundle - metaDataModel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_api
from libica.openapi.v2.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)
    project = Project(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        name="name_example",
        active=True,
        short_description="short_description_example",
        information="information_example",
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
        billing_mode="PROJECT",
        data_sharing_enabled=True,
        tags=ProjectTag(
            technical_tags=[
                "technical_tags_example",
            ],
            user_tags=[
                "user_tags_example",
            ],
        ),
        storage_bundle=StorageBundle(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            bundle_name="bundle_name_example",
            entitlement_name="entitlement_name_example",
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
        ),
        self_managed_storage_configuration=StorageConfiguration(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            name="name_example",
            description="description_example",
            type="AWS_S3",
            status="INITIALIZING",
            error_message="error_message_example",
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
            is_default=True,
        ),
        metadata_model=MetadataModel(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            name="name_example",
            description="description_example",
            state="DRAFT",
            parent_model_id="parent_model_id_example",
        ),
    ) # Project |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a project.
        api_response = api_instance.update_project(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a project.
        api_response = api_instance.update_project(project_id, if_match=if_match, project=project)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]
 **project** | [**Project**](Project.md)|  | [optional]

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project is successfully update. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
