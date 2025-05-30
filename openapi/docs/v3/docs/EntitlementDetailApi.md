# libica.openapi.v3.EntitlementDetailApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_matching_activation_codes_for_cwl**](EntitlementDetailApi.md#find_all_matching_activation_codes_for_cwl) | **POST** /api/activationCodes:findAllMatchingForCwl | Search all matching activation code details for a Cwl pipeline.
[**find_all_matching_activation_codes_for_nextflow**](EntitlementDetailApi.md#find_all_matching_activation_codes_for_nextflow) | **POST** /api/activationCodes:findAllMatchingForNextflow | Search all matching activation code details for a Nextflow pipeline.
[**find_best_matching_activation_code_for_cwl**](EntitlementDetailApi.md#find_best_matching_activation_code_for_cwl) | **POST** /api/activationCodes:findBestMatchingForCwl | Search the best matching activation code detail for Cwl pipeline.
[**find_best_matching_activation_codes_for_nextflow**](EntitlementDetailApi.md#find_best_matching_activation_codes_for_nextflow) | **POST** /api/activationCodes:findBestMatchingForNextflow | Search the best matching activation code details for Nextflow pipeline.


# **find_all_matching_activation_codes_for_cwl**
> ActivationCodeDetailList find_all_matching_activation_codes_for_cwl(search_matching_activation_codes_for_cwl_analysis)

Search all matching activation code details for a Cwl pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v3.models.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
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
    api_instance = libica.openapi.v3.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_cwl_analysis = libica.openapi.v3.SearchMatchingActivationCodesForCwlAnalysis() # SearchMatchingActivationCodesForCwlAnalysis | 

    try:
        # Search all matching activation code details for a Cwl pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_cwl(search_matching_activation_codes_for_cwl_analysis)
        print("The response of EntitlementDetailApi->find_all_matching_activation_codes_for_cwl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_cwl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_cwl_analysis** | [**SearchMatchingActivationCodesForCwlAnalysis**](SearchMatchingActivationCodesForCwlAnalysis.md)|  | 

### Return type

[**ActivationCodeDetailList**](ActivationCodeDetailList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching activation code details are successfully searched. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_matching_activation_codes_for_nextflow**
> ActivationCodeDetailList find_all_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)

Search all matching activation code details for a Nextflow pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v3.models.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = libica.openapi.v3.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_nextflow_analysis = libica.openapi.v3.SearchMatchingActivationCodesForNextflowAnalysis() # SearchMatchingActivationCodesForNextflowAnalysis | 

    try:
        # Search all matching activation code details for a Nextflow pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)
        print("The response of EntitlementDetailApi->find_all_matching_activation_codes_for_nextflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_nextflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_nextflow_analysis** | [**SearchMatchingActivationCodesForNextflowAnalysis**](SearchMatchingActivationCodesForNextflowAnalysis.md)|  | 

### Return type

[**ActivationCodeDetailList**](ActivationCodeDetailList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching activation code details are successfully searched. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_best_matching_activation_code_for_cwl**
> ActivationCodeDetail find_best_matching_activation_code_for_cwl(search_matching_activation_codes_for_cwl_analysis)

Search the best matching activation code detail for Cwl pipeline.

Endpoint for searching the best activation code detail for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.activation_code_detail import ActivationCodeDetail
from libica.openapi.v3.models.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
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
    api_instance = libica.openapi.v3.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_cwl_analysis = libica.openapi.v3.SearchMatchingActivationCodesForCwlAnalysis() # SearchMatchingActivationCodesForCwlAnalysis | 

    try:
        # Search the best matching activation code detail for Cwl pipeline.
        api_response = api_instance.find_best_matching_activation_code_for_cwl(search_matching_activation_codes_for_cwl_analysis)
        print("The response of EntitlementDetailApi->find_best_matching_activation_code_for_cwl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_code_for_cwl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_cwl_analysis** | [**SearchMatchingActivationCodesForCwlAnalysis**](SearchMatchingActivationCodesForCwlAnalysis.md)|  | 

### Return type

[**ActivationCodeDetail**](ActivationCodeDetail.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The best matching activation code details are successfully searched. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_best_matching_activation_codes_for_nextflow**
> ActivationCodeDetail find_best_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)

Search the best matching activation code details for Nextflow pipeline.

Endpoint for searching the best activation code details for a project and an analysis for a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.activation_code_detail import ActivationCodeDetail
from libica.openapi.v3.models.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = libica.openapi.v3.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_nextflow_analysis = libica.openapi.v3.SearchMatchingActivationCodesForNextflowAnalysis() # SearchMatchingActivationCodesForNextflowAnalysis | 

    try:
        # Search the best matching activation code details for Nextflow pipeline.
        api_response = api_instance.find_best_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)
        print("The response of EntitlementDetailApi->find_best_matching_activation_codes_for_nextflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_codes_for_nextflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_nextflow_analysis** | [**SearchMatchingActivationCodesForNextflowAnalysis**](SearchMatchingActivationCodesForNextflowAnalysis.md)|  | 

### Return type

[**ActivationCodeDetail**](ActivationCodeDetail.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The best matching activation code details are successfully searched. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

