# libica.openapi.v2.EntitlementDetailApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_matching_activation_codes_for_cwl**](EntitlementDetailApi.md#find_all_matching_activation_codes_for_cwl) | **POST** /api/activationCodes:findAllMatchingForCwl | Search all matching activation code details for a Cwl pipeline.
[**find_all_matching_activation_codes_for_nextflow**](EntitlementDetailApi.md#find_all_matching_activation_codes_for_nextflow) | **POST** /api/activationCodes:findAllMatchingForNextflow | Search all matching activation code details for a Nextflow pipeline.
[**find_best_matching_activation_code_for_cwl**](EntitlementDetailApi.md#find_best_matching_activation_code_for_cwl) | **POST** /api/activationCodes:findBestMatchingForCwl | Search the best matching activation code detail for Cwl pipeline.
[**find_best_matching_activation_codes_for_nextflow**](EntitlementDetailApi.md#find_best_matching_activation_codes_for_nextflow) | **POST** /api/activationCodes:findBestMatchingForNextflow | Search the best matching activation code details for Nextflow pipeline.


# **find_all_matching_activation_codes_for_cwl**
> ActivationCodeDetailList find_all_matching_activation_codes_for_cwl()

Search all matching activation code details for a Cwl pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitlement_detail_api
from libica.openapi.v2.model.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v2.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_cwl_analysis = SearchMatchingActivationCodesForCwlAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=CwlAnalysisInput(),
    ) # SearchMatchingActivationCodesForCwlAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search all matching activation code details for a Cwl pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_cwl(search_matching_activation_codes_for_cwl_analysis=search_matching_activation_codes_for_cwl_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_cwl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_cwl_analysis** | [**SearchMatchingActivationCodesForCwlAnalysis**](SearchMatchingActivationCodesForCwlAnalysis.md)|  | [optional]

### Return type

[**ActivationCodeDetailList**](ActivationCodeDetailList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ActivationCodeDetailList find_all_matching_activation_codes_for_nextflow()

Search all matching activation code details for a Nextflow pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitlement_detail_api
from libica.openapi.v2.model.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v2.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_nextflow_analysis = SearchMatchingActivationCodesForNextflowAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=NextflowAnalysisInput(
            inputs=[
                AnalysisDataInput(
                    parameter_code="parameter_code_example",
                    data_ids=[
                        "data_ids_example",
                    ],
                    mounts=[
                        AnalysisInputDataMount(
                            data_id="data_id_example",
                            mount_path="mount_path_example",
                        ),
                    ],
                ),
            ],
            parameters=[
                AnalysisParameterInput(
                    code="code_example",
                    value="value_example",
                    multi_value=[
                        "multi_value_example",
                    ],
                ),
            ],
            reference_data_parameters=[
                AnalysisReferenceDataParameter(
                    parameter_code="parameter_code_example",
                    reference_data_id="reference_data_id_example",
                ),
            ],
        ),
    ) # SearchMatchingActivationCodesForNextflowAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search all matching activation code details for a Nextflow pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis=search_matching_activation_codes_for_nextflow_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_nextflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_nextflow_analysis** | [**SearchMatchingActivationCodesForNextflowAnalysis**](SearchMatchingActivationCodesForNextflowAnalysis.md)|  | [optional]

### Return type

[**ActivationCodeDetailList**](ActivationCodeDetailList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ActivationCodeDetail find_best_matching_activation_code_for_cwl()

Search the best matching activation code detail for Cwl pipeline.

Endpoint for searching the best activation code detail for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitlement_detail_api
from libica.openapi.v2.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from libica.openapi.v2.model.activation_code_detail import ActivationCodeDetail
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_cwl_analysis = SearchMatchingActivationCodesForCwlAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=CwlAnalysisInput(),
    ) # SearchMatchingActivationCodesForCwlAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search the best matching activation code detail for Cwl pipeline.
        api_response = api_instance.find_best_matching_activation_code_for_cwl(search_matching_activation_codes_for_cwl_analysis=search_matching_activation_codes_for_cwl_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_code_for_cwl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_cwl_analysis** | [**SearchMatchingActivationCodesForCwlAnalysis**](SearchMatchingActivationCodesForCwlAnalysis.md)|  | [optional]

### Return type

[**ActivationCodeDetail**](ActivationCodeDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

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
> ActivationCodeDetail find_best_matching_activation_codes_for_nextflow()

Search the best matching activation code details for Nextflow pipeline.

Endpoint for searching the best activation code details for a project and an analysis for a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitlement_detail_api
from libica.openapi.v2.model.activation_code_detail import ActivationCodeDetail
from libica.openapi.v2.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_nextflow_analysis = SearchMatchingActivationCodesForNextflowAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=NextflowAnalysisInput(
            inputs=[
                AnalysisDataInput(
                    parameter_code="parameter_code_example",
                    data_ids=[
                        "data_ids_example",
                    ],
                    mounts=[
                        AnalysisInputDataMount(
                            data_id="data_id_example",
                            mount_path="mount_path_example",
                        ),
                    ],
                ),
            ],
            parameters=[
                AnalysisParameterInput(
                    code="code_example",
                    value="value_example",
                    multi_value=[
                        "multi_value_example",
                    ],
                ),
            ],
            reference_data_parameters=[
                AnalysisReferenceDataParameter(
                    parameter_code="parameter_code_example",
                    reference_data_id="reference_data_id_example",
                ),
            ],
        ),
    ) # SearchMatchingActivationCodesForNextflowAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search the best matching activation code details for Nextflow pipeline.
        api_response = api_instance.find_best_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis=search_matching_activation_codes_for_nextflow_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_codes_for_nextflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_matching_activation_codes_for_nextflow_analysis** | [**SearchMatchingActivationCodesForNextflowAnalysis**](SearchMatchingActivationCodesForNextflowAnalysis.md)|  | [optional]

### Return type

[**ActivationCodeDetail**](ActivationCodeDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The best matching activation code details are successfully searched. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

