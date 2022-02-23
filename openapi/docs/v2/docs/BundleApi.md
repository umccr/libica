# libica.openapi.v2.BundleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle**](BundleApi.md#create_bundle) | **POST** /api/bundles | Create a new bundle
[**get_bundle**](BundleApi.md#get_bundle) | **GET** /api/bundles/{bundleId} | Retrieve a bundle.
[**get_bundles**](BundleApi.md#get_bundles) | **GET** /api/bundles | Retrieve a list of bundles.
[**release_bundle**](BundleApi.md#release_bundle) | **POST** /api/bundles/{bundleId}:release | release a bundle


# **create_bundle**
> Bundle create_bundle()

Create a new bundle

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_api
from libica.openapi.v2.model.create_bundle import CreateBundle
from libica.openapi.v2.model.bundle import Bundle
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
    api_instance = bundle_api.BundleApi(api_client)
    create_bundle = CreateBundle(
        name="name_example",
        short_description="short_description_example",
        bundle_release_version="bundle_release_version_example",
        bundle_version_comment="bundle_version_comment_example",
        region_id="region_id_example",
        metadata_model_id="metadata_model_id_example",
        bundle_status="DRAFT",
        categories=[
            "categories_example",
        ],
        links=Links(
            links=[
                Link(
                    name="name_example",
                    url="url_example",
                ),
            ],
            licenses=[
                Link(
                    name="name_example",
                    url="url_example",
                ),
            ],
            homepages=[
                Link(
                    name="name_example",
                    url="url_example",
                ),
            ],
            publications=[
                Link(
                    name="name_example",
                    url="url_example",
                ),
            ],
        ),
    ) # CreateBundle |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new bundle
        api_response = api_instance.create_bundle(create_bundle=create_bundle)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleApi->create_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bundle** | [**CreateBundle**](CreateBundle.md)|  | [optional]

### Return type

[**Bundle**](Bundle.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The bundle is successfully created. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle**
> Bundle get_bundle(bundle_id)

Retrieve a bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_api
from libica.openapi.v2.model.bundle import Bundle
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
    api_instance = bundle_api.BundleApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a bundle.
        api_response = api_instance.get_bundle(bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleApi->get_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to retrieve |

### Return type

[**Bundle**](Bundle.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bundle is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundles**
> BundlePagedList get_bundles()

Retrieve a list of bundles.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_api
from libica.openapi.v2.model.bundle_paged_list import BundlePagedList
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
    api_instance = bundle_api.BundleApi(api_client)
    search = "search_example" # str | Search (optional)
    user_tags = "userTags_example" # str | User tags to filter on (optional)
    technical_tags = "technicalTags_example" # str | Technical tags to filter on (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - name - shortDescription (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of bundles.
        api_response = api_instance.get_bundles(search=search, user_tags=user_tags, technical_tags=technical_tags, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleApi->get_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search | [optional]
 **user_tags** | **str**| User tags to filter on | [optional]
 **technical_tags** | **str**| Technical tags to filter on | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - name - shortDescription | [optional]

### Return type

[**BundlePagedList**](BundlePagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of bundles is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_bundle**
> release_bundle(bundle_id)

release a bundle

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import bundle_api
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
    api_instance = bundle_api.BundleApi(api_client)
    bundle_id = "bundleId_example" # str | The ID of the bundle to release

    # example passing only required values which don't have defaults set
    try:
        # release a bundle
        api_instance.release_bundle(bundle_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling BundleApi->release_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The ID of the bundle to release |

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
**204** | The bundle is successfully released |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

