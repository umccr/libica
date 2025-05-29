# libica.openapi.v3.DockerImageApi

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.docker_image_region_list import DockerImageRegionList
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)
    image_id = 'image_id_example' # str | 
    docker_image_region_list = libica.openapi.v3.DockerImageRegionList() # DockerImageRegionList | 

    try:
        # Add regions to an existing Docker image.
        api_instance.add_regions(image_id, docker_image_region_list)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_external_docker_image import CreateExternalDockerImage
from libica.openapi.v3.models.docker_image import DockerImage
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)
    create_external_docker_image = libica.openapi.v3.CreateExternalDockerImage() # CreateExternalDockerImage | 

    try:
        # Create an external Docker image.
        api_response = api_instance.create_external_docker_image(create_external_docker_image)
        print("The response of DockerImageApi->create_external_docker_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerImageApi->create_external_docker_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_docker_image** | [**CreateExternalDockerImage**](CreateExternalDockerImage.md)|  | 

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.create_internal_docker_image import CreateInternalDockerImage
from libica.openapi.v3.models.docker_image import DockerImage
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)
    create_internal_docker_image = libica.openapi.v3.CreateInternalDockerImage() # CreateInternalDockerImage | 

    try:
        # Create an internal Docker image.
        api_response = api_instance.create_internal_docker_image(create_internal_docker_image)
        print("The response of DockerImageApi->create_internal_docker_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerImageApi->create_internal_docker_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_internal_docker_image** | [**CreateInternalDockerImage**](CreateInternalDockerImage.md)|  | 

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.docker_image import DockerImage
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)
    image_id = 'image_id_example' # str | 

    try:
        # Retrieve a Docker image. Only the Docker image the user has access to can be retrieved.
        api_response = api_instance.get_docker_image(image_id)
        print("The response of DockerImageApi->get_docker_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerImageApi->get_docker_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 

### Return type

[**DockerImage**](DockerImage.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.docker_image_list import DockerImageList
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)

    try:
        # Retrieve a list of Docker images. Only the Docker images the user has access to are returned.
        api_response = api_instance.get_docker_images()
        print("The response of DockerImageApi->get_docker_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerImageApi->get_docker_images: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DockerImageList**](DockerImageList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.docker_image_region_list import DockerImageRegionList
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
    api_instance = libica.openapi.v3.DockerImageApi(api_client)
    image_id = 'image_id_example' # str | 
    docker_image_region_list = libica.openapi.v3.DockerImageRegionList() # DockerImageRegionList | 

    try:
        # Remove regions to an existing Docker image.
        api_instance.remove_regions(image_id, docker_image_region_list)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The regions are successfully removed. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

