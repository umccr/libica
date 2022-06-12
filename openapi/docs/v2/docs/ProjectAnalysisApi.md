# libica.openapi.v2.ProjectAnalysisApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_analysis**](ProjectAnalysisApi.md#abort_analysis) | **POST** /api/projects/{projectId}/analyses/{analysisId}:abort | Abort an analysis.
[**create_cwl_analysis**](ProjectAnalysisApi.md#create_cwl_analysis) | **POST** /api/projects/{projectId}/analysis:cwl | Create and start an analysis for a CWL pipeline.
[**create_nextflow_analysis**](ProjectAnalysisApi.md#create_nextflow_analysis) | **POST** /api/projects/{projectId}/analysis:nextflow | Create and start an analysis for a Nextflow pipeline.
[**get_analyses**](ProjectAnalysisApi.md#get_analyses) | **GET** /api/projects/{projectId}/analyses | Retrieve the list of project analyses.
[**get_analysis**](ProjectAnalysisApi.md#get_analysis) | **GET** /api/projects/{projectId}/analyses/{analysisId} | Retrieve an analysis.
[**get_analysis_configurations**](ProjectAnalysisApi.md#get_analysis_configurations) | **GET** /api/projects/{projectId}/analyses/{analysisId}/configurations | Retrieve the configurations of an analysis.
[**get_analysis_inputs**](ProjectAnalysisApi.md#get_analysis_inputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/inputs | Retrieve the inputs of an analysis.
[**get_analysis_outputs**](ProjectAnalysisApi.md#get_analysis_outputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/outputs | Retrieve the outputs of an analysis.
[**get_analysis_steps**](ProjectAnalysisApi.md#get_analysis_steps) | **GET** /api/projects/{projectId}/analyses/{analysisId}/steps | Retrieve the individual steps of an analysis.
[**get_raw_analysis_output**](ProjectAnalysisApi.md#get_raw_analysis_output) | **GET** /api/projects/{projectId}/analyses/{analysisId}/rawOutput | Retrieve the raw output of an analysis.
[**update_analysis**](ProjectAnalysisApi.md#update_analysis) | **PUT** /api/projects/{projectId}/analyses/{analysisId} | Update an analysis.


# **abort_analysis**
> abort_analysis(project_id, analysis_id)

Abort an analysis.

Endpoint for aborting an analysis. The status of the analysis is not updated immediately, only when the abortion of the analysis has actually started.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to abort

    # example passing only required values which don't have defaults set
    try:
        # Abort an analysis.
        api_instance.abort_analysis(project_id, analysis_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->abort_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to abort |

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
**204** | The analysis is successfully aborted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_analysis**
> Analysis create_cwl_analysis(project_id)

Create and start an analysis for a CWL pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.create_cwl_analysis import CreateCwlAnalysis
from libica.openapi.v2.model.analysis import Analysis
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to <a href=\"https://tools.ietf.org/id/draft-idempotency-header-01.html\">the IETF spec</a> and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)
    create_cwl_analysis = CreateCwlAnalysis(
        user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        pipeline_id="pipeline_id_example",
        tags=AnalysisTag(
            technical_tags=[
                "technical_tags_example",
            ],
            user_tags=[
                "user_tags_example",
            ],
            reference_tags=[
                "reference_tags_example",
            ],
        ),
        activation_code_detail_id="activation_code_detail_id_example",
        analysis_storage_id="analysis_storage_id_example",
        output_parent_folder_id="output_parent_folder_id_example",
        analysis_input=CwlAnalysisInput(),
    ) # CreateCwlAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id, idempotency_key=idempotency_key, create_cwl_analysis=create_cwl_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to &lt;a href&#x3D;\&quot;https://tools.ietf.org/id/draft-idempotency-header-01.html\&quot;&gt;the IETF spec&lt;/a&gt; and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional]
 **create_cwl_analysis** | [**CreateCwlAnalysis**](CreateCwlAnalysis.md)|  | [optional]

### Return type

[**Analysis**](Analysis.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_analysis**
> Analysis create_nextflow_analysis(project_id)

Create and start an analysis for a Nextflow pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis import Analysis
from libica.openapi.v2.model.create_nextflow_analysis import CreateNextflowAnalysis
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    idempotency_key = "Idempotency-Key_example" # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to <a href=\"https://tools.ietf.org/id/draft-idempotency-header-01.html\">the IETF spec</a> and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)
    create_nextflow_analysis = CreateNextflowAnalysis(
        user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        pipeline_id="pipeline_id_example",
        tags=AnalysisTag(
            technical_tags=[
                "technical_tags_example",
            ],
            user_tags=[
                "user_tags_example",
            ],
            reference_tags=[
                "reference_tags_example",
            ],
        ),
        activation_code_detail_id="activation_code_detail_id_example",
        analysis_storage_id="analysis_storage_id_example",
        output_parent_folder_id="output_parent_folder_id_example",
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
                AnalysisParameter(
                    code="code_example",
                    value="value_example",
                ),
            ],
            reference_data_parameters=[
                AnalysisReferenceDataParameter(
                    parameter_code="parameter_code_example",
                    reference_data_id="reference_data_id_example",
                ),
            ],
        ),
    ) # CreateNextflowAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id, idempotency_key=idempotency_key, create_nextflow_analysis=create_nextflow_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to &lt;a href&#x3D;\&quot;https://tools.ietf.org/id/draft-idempotency-header-01.html\&quot;&gt;the IETF spec&lt;/a&gt; and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional]
 **create_nextflow_analysis** | [**CreateNextflowAnalysis**](CreateNextflowAnalysis.md)|  | [optional]

### Return type

[**Analysis**](Analysis.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyses**
> AnalysisPagedList get_analyses(project_id)

Retrieve the list of project analyses.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_paged_list import AnalysisPagedList
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    reference = "reference_example" # str | The reference to filter on. (optional)
    userreference = "userreference_example" # str | The user-reference to filter on. (optional)
    status = "status_example" # str | The status to filter on. (optional)
    usertag = "usertag_example" # str | The user-tags to filter on. (optional)
    technicaltag = "technicaltag_example" # str | The technical-tags to filter on. (optional)
    referencetag = "referencetag_example" # str | The reference-data-tags to filter on. (optional)
    page_offset = "pageOffset_example" # str | The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. (optional)
    page_token = "pageToken_example" # str | The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. (optional)
    page_size = "pageSize_example" # str | The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. (optional)
    sort = "sort_example" # str | Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the list of project analyses.
        api_response = api_instance.get_analyses(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the list of project analyses.
        api_response = api_instance.get_analyses(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **reference** | **str**| The reference to filter on. | [optional]
 **userreference** | **str**| The user-reference to filter on. | [optional]
 **status** | **str**| The status to filter on. | [optional]
 **usertag** | **str**| The user-tags to filter on. | [optional]
 **technicaltag** | **str**| The technical-tags to filter on. | [optional]
 **referencetag** | **str**| The reference-data-tags to filter on. | [optional]
 **page_offset** | **str**| The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. | [optional]
 **page_token** | **str**| The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. | [optional]
 **page_size** | **str**| The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results. | [optional]
 **sort** | **str**| Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional]

### Return type

[**AnalysisPagedList**](AnalysisPagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis**
> Analysis get_analysis(project_id, analysis_id)

Retrieve an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis import Analysis
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an analysis.
        api_response = api_instance.get_analysis(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to retrieve |

### Return type

[**Analysis**](Analysis.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_configurations**
> ExecutionConfigurationList get_analysis_configurations(project_id, analysis_id)

Retrieve the configurations of an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.execution_configuration_list import ExecutionConfigurationList
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to retrieve the configuration for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the configurations of an analysis.
        api_response = api_instance.get_analysis_configurations(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to retrieve the configuration for |

### Return type

[**ExecutionConfigurationList**](ExecutionConfigurationList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configurations of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_inputs**
> AnalysisInputList get_analysis_inputs(project_id, analysis_id)

Retrieve the inputs of an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_input_list import AnalysisInputList
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to retrieve the inputs for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the inputs of an analysis.
        api_response = api_instance.get_analysis_inputs(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_inputs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to retrieve the inputs for |

### Return type

[**AnalysisInputList**](AnalysisInputList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_outputs**
> AnalysisOutputList get_analysis_outputs(project_id, analysis_id)

Retrieve the outputs of an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_output_list import AnalysisOutputList
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to retrieve the outputs for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the outputs of an analysis.
        api_response = api_instance.get_analysis_outputs(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_outputs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to retrieve the outputs for |

### Return type

[**AnalysisOutputList**](AnalysisOutputList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The outputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_steps**
> AnalysisStepList get_analysis_steps(project_id, analysis_id)

Retrieve the individual steps of an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_step_list import AnalysisStepList
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis to retrieve the individual steps for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the individual steps of an analysis.
        api_response = api_instance.get_analysis_steps(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis to retrieve the individual steps for |

### Return type

[**AnalysisStepList**](AnalysisStepList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The individual steps of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_analysis_output**
> AnalysisRawOutput get_raw_analysis_output(project_id, analysis_id)

Retrieve the raw output of an analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.problem import Problem
from libica.openapi.v2.model.analysis_raw_output import AnalysisRawOutput
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | The ID of the analysis for which to retrieve the raw output

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the raw output of an analysis.
        api_response = api_instance.get_raw_analysis_output(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_raw_analysis_output: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the analysis for which to retrieve the raw output |

### Return type

[**AnalysisRawOutput**](AnalysisRawOutput.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw output of the analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> Analysis update_analysis(project_id, analysis_id)

Update an analysis.

Attributes which can be updated:    - tags

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis import Analysis
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
    api_instance = project_analysis_api.ProjectAnalysisApi(api_client)
    project_id = "projectId_example" # str | 
    analysis_id = "analysisId_example" # str | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)
    analysis = Analysis(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        reference="reference_example",
        user_reference="user_reference_example",
        pipeline=Pipeline(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            code="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
            description="description_example",
            language="CWL",
            pipeline_tags=PipelineTag(
                technical_tags=[
                    "technical_tags_example",
                ],
            ),
            analysis_storage=AnalysisStorage(
                id="id_example",
                time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                name="name_example",
                description="description_example",
            ),
        ),
        status="REQUESTED",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        summary="summary_example",
        analysis_storage=AnalysisStorage(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            name="name_example",
            description="description_example",
        ),
        tags=AnalysisTag(
            technical_tags=[
                "technical_tags_example",
            ],
            user_tags=[
                "user_tags_example",
            ],
            reference_tags=[
                "reference_tags_example",
            ],
        ),
    ) # Analysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id, if_match=if_match, analysis=analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]
 **analysis** | [**Analysis**](Analysis.md)|  | [optional]

### Return type

[**Analysis**](Analysis.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

