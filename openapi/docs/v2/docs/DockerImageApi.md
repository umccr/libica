# libica.openapi.v2.DockerImageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_regions**](DockerImageApi.md#add_regions) | **POST** /api/dockerImages/{imageId}:addRegions | Add regions to an existing Docker image.
[**create_external_docker_image**](DockerImageApi.md#create_external_docker_image) | **POST** /api/dockerImages:createExternal | Create an external Docker image.
[**create_internal_docker_image**](DockerImageApi.md#create_internal_docker_image) | **POST** /api/dockerImages:createInternal | Create an internal Docker image.
[**get_docker_image**](DockerImageApi.md#get_docker_image) | **GET** /api/dockerImages/{imageId} | Retrieve a Docker image. Only the Docker image the user has access to can be retrieved.
[**get_docker_images**](DockerImageApi.md#get_docker_images) | **GET** /api/dockerImages | Retrieve a list of Docker images. Only the Docker images the user has access to are returned.
[**remove_regions**](DockerImageApi.md#remove_regions) | **POST** /api/dockerImages/{imageId}:removeRegions | Remove regions to an existing Docker image.


# **add_regions**
> add_regions(image_id, docker_image_region_list)

Add regions to an existing Docker image.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image_region_list import DockerImageRegionList
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
    api_instance = docker_image_api.DockerImageApi(api_client)
    image_id = "imageId_example" # str | 
    docker_image_region_list = DockerImageRegionList(
        region_ids=[
            "region_ids_example",
        ],
    ) # DockerImageRegionList | 

    # example passing only required values which don't have defaults set
    try:
        # Add regions to an existing Docker image.
        api_instance.add_regions(image_id, docker_image_region_list)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->add_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  |
 **docker_image_region_list** | [**DockerImageRegionList**](DockerImageRegionList.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The regions are successfully added. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_external_docker_image**
> DockerImage create_external_docker_image(create_external_docker_image)

Create an external Docker image.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image import DockerImage
from libica.openapi.v2.model.create_external_docker_image import CreateExternalDockerImage
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
    api_instance = docker_image_api.DockerImageApi(api_client)
    create_external_docker_image = CreateExternalDockerImage(
        url="url_example",
        name="name_example",
        version="version_example",
        description="description_example",
        type="TOOL",
    ) # CreateExternalDockerImage | 

    # example passing only required values which don't have defaults set
    try:
        # Create an external Docker image.
        api_response = api_instance.create_external_docker_image(create_external_docker_image)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->create_external_docker_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_docker_image** | [**CreateExternalDockerImage**](CreateExternalDockerImage.md)|  |

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Docker image is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internal_docker_image**
> DockerImage create_internal_docker_image(create_internal_docker_image)

Create an internal Docker image.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image import DockerImage
from libica.openapi.v2.model.create_internal_docker_image import CreateInternalDockerImage
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
    api_instance = docker_image_api.DockerImageApi(api_client)
    create_internal_docker_image = CreateInternalDockerImage(
        docker_data_id="docker_data_id_example",
        docker_data_project_id="docker_data_project_id_example",
        name="name_example",
        version="version_example",
        description="description_example",
        type="TOOL",
        regions=[
            "regions_example",
        ],
    ) # CreateInternalDockerImage | 

    # example passing only required values which don't have defaults set
    try:
        # Create an internal Docker image.
        api_response = api_instance.create_internal_docker_image(create_internal_docker_image)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->create_internal_docker_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_internal_docker_image** | [**CreateInternalDockerImage**](CreateInternalDockerImage.md)|  |

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Docker image is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_docker_image**
> DockerImage get_docker_image(image_id)

Retrieve a Docker image. Only the Docker image the user has access to can be retrieved.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image import DockerImage
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
    api_instance = docker_image_api.DockerImageApi(api_client)
    image_id = "imageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Docker image. Only the Docker image the user has access to can be retrieved.
        api_response = api_instance.get_docker_image(image_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->get_docker_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  |

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Docker image is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_docker_images**
> DockerImageList get_docker_images()

Retrieve a list of Docker images. Only the Docker images the user has access to are returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image_list import DockerImageList
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
    api_instance = docker_image_api.DockerImageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of Docker images. Only the Docker images the user has access to are returned.
        api_response = api_instance.get_docker_images()
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->get_docker_images: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DockerImageList**](DockerImageList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Docker images is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_regions**
> remove_regions(image_id, docker_image_region_list)

Remove regions to an existing Docker image.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import docker_image_api
from libica.openapi.v2.model.docker_image_region_list import DockerImageRegionList
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
    api_instance = docker_image_api.DockerImageApi(api_client)
    image_id = "imageId_example" # str | 
    docker_image_region_list = DockerImageRegionList(
        region_ids=[
            "region_ids_example",
        ],
    ) # DockerImageRegionList | 

    # example passing only required values which don't have defaults set
    try:
        # Remove regions to an existing Docker image.
        api_instance.remove_regions(image_id, docker_image_region_list)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling DockerImageApi->remove_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  |
 **docker_image_region_list** | [**DockerImageRegionList**](DockerImageRegionList.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The regions are successfully removed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

