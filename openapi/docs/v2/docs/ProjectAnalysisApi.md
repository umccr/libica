# libica.openapi.v2.ProjectAnalysisApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_analysis**](ProjectAnalysisApi.md#abort_analysis) | **POST** /api/projects/{projectId}/analyses/{analysisId}:abort | Abort an analysis.
[**create_cwl_analysis**](ProjectAnalysisApi.md#create_cwl_analysis) | **POST** /api/projects/{projectId}/analysis:cwl | Create and start an analysis for a CWL pipeline.
[**create_nextflow_analysis**](ProjectAnalysisApi.md#create_nextflow_analysis) | **POST** /api/projects/{projectId}/analysis:nextflow | Create and start an analysis for a Nextflow pipeline.
[**get_analyses**](ProjectAnalysisApi.md#get_analyses) | **GET** /api/projects/{projectId}/analyses | Retrieve the list of analyses.
[**get_analysis**](ProjectAnalysisApi.md#get_analysis) | **GET** /api/projects/{projectId}/analyses/{analysisId} | Retrieve an analysis.
[**get_analysis_configurations**](ProjectAnalysisApi.md#get_analysis_configurations) | **GET** /api/projects/{projectId}/analyses/{analysisId}/configurations | Retrieve the configurations of an analysis.
[**get_analysis_inputs**](ProjectAnalysisApi.md#get_analysis_inputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/inputs | Retrieve the inputs of an analysis.
[**get_analysis_outputs**](ProjectAnalysisApi.md#get_analysis_outputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/outputs | Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.
[**get_analysis_steps**](ProjectAnalysisApi.md#get_analysis_steps) | **GET** /api/projects/{projectId}/analyses/{analysisId}/steps | Retrieve the individual steps of an analysis.
[**get_cwl_input_json**](ProjectAnalysisApi.md#get_cwl_input_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/inputJson | Retrieve the input json of a CWL analysis.
[**get_cwl_output_json**](ProjectAnalysisApi.md#get_cwl_output_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/outputJson | Retrieve the output json of a CWL analysis.
[**get_raw_analysis_output**](ProjectAnalysisApi.md#get_raw_analysis_output) | **GET** /api/projects/{projectId}/analyses/{analysisId}/rawOutput | Retrieve the raw output of an analysis.
[**search_analyses**](ProjectAnalysisApi.md#search_analyses) | **POST** /api/projects/{projectId}/analysis:search | Search analyses.
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
> AnalysisV4 create_cwl_analysis(project_id, create_cwl_analysis)

Create and start an analysis for a CWL pipeline.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3]  * Initial version ## [V4]  * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].  * Field analysisPriority changed from enum to String.  * The owner and tenant are now represented by Identifier objects. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.create_cwl_analysis import CreateCwlAnalysis
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
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
    create_cwl_analysis = CreateCwlAnalysis(
        user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        pipeline_id="pipeline_id_example",
        tags=CreateAnalysisTag(
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
        analysis_output=[
            AnalysisOutputMapping(
                source_path="source_path_example",
                type="FILE",
                target_project_id="target_project_id_example",
                target_path="target_path_example",
                action_on_exist="action_on_exist_example",
            ),
        ],
        analysis_input=CwlAnalysisInput(),
    ) # CreateCwlAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = "Idempotency-Key_example" # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id, create_cwl_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id, create_cwl_analysis, idempotency_key=idempotency_key)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_cwl_analysis** | [**CreateCwlAnalysis**](CreateCwlAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; |
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional]

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_analysis**
> AnalysisV4 create_nextflow_analysis(project_id, create_nextflow_analysis)

Create and start an analysis for a Nextflow pipeline.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3]  * Initial version ## [V4]  * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].  * Field analysisPriority changed from enum to String.  * The owner and tenant are now represented by Identifier objects. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.create_nextflow_analysis import CreateNextflowAnalysis
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
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
    create_nextflow_analysis = CreateNextflowAnalysis(
        user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        pipeline_id="pipeline_id_example",
        tags=CreateAnalysisTag(
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
        analysis_output=[
            AnalysisOutputMapping(
                source_path="source_path_example",
                type="FILE",
                target_project_id="target_project_id_example",
                target_path="target_path_example",
                action_on_exist="action_on_exist_example",
            ),
        ],
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
                    external_data=[
                        AnalysisInputExternalData(
                            url="url_example",
                            type="basespac",
                            mount_path="mount_path_example",
                            s3_details=AnalysisS3DataDetails(
                                storage_credentials_id="storage_credentials_id_example",
                            ),
                            basespace_details=AnalysisBaseSpaceDataDetails(
                                workgroup_id="workgroup_id_example",
                                extensions="extensions_example",
                                path_prefix="path_prefix_example",
                            ),
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
    ) # CreateNextflowAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = "Idempotency-Key_example" # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code < 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response, which indicates that the original call is still in progress.</li><li>the request body is not the same as the previous request => 422 error response, as this is not allowed.</li></ul>This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn't been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code >= 400) we allow clients to retry the call. This is where we don't follow the IETF specification. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id, create_nextflow_analysis)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id, create_nextflow_analysis, idempotency_key=idempotency_key)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **create_nextflow_analysis** | [**CreateNextflowAnalysis**](CreateNextflowAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; |
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec, with one exception (see below). The header value is allowed to be max 255 characters long. If the header is supplied for a successful response (HTTP status code &lt; 400) then the response  will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes  a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response, which indicates that the original call is still in progress.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response, as this is not allowed.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing a new API request using the Idempotency-Key header, the request has to contain a new header value that hasn&#39;t been used (successfully) in the past 7 days for that specific API endpoint and by the specific user. For error responses (HTTP status code &gt;&#x3D; 400) we allow clients to retry the call. This is where we don&#39;t follow the IETF specification. | [optional]

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyses**
> AnalysisPagedListV3 get_analyses(project_id)

Retrieve the list of analyses.

This endpoint only returns V3 items. Use the search endpoint to get V4 items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_paged_list_v3 import AnalysisPagedListV3
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
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = "sort_example" # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the list of analyses.
        api_response = api_instance.get_analyses(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the list of analyses.
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
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional]

### Return type

[**AnalysisPagedListV3**](AnalysisPagedListV3.md)

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
> AnalysisV4 get_analysis(project_id, analysis_id)

Retrieve an analysis.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3]  * Initial version ## [V4]  * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].  * Field analysisPriority changed from enum to String.  * The owner and tenant are now represented by Identifier objects. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
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

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json


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

Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.

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
        # Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.
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

# **get_cwl_input_json**
> CwlAnalysisInputJson get_cwl_input_json(project_id, analysis_id)

Retrieve the input json of a CWL analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.cwl_analysis_input_json import CwlAnalysisInputJson
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
    analysis_id = "analysisId_example" # str | The ID of the CWL analysis for which to retrieve the input json

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the input json of a CWL analysis.
        api_response = api_instance.get_cwl_input_json(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_input_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the input json |

### Return type

[**CwlAnalysisInputJson**](CwlAnalysisInputJson.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input json of the CWL analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwl_output_json**
> CwlAnalysisOutputJson get_cwl_output_json(project_id, analysis_id)

Retrieve the output json of a CWL analysis.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.cwl_analysis_output_json import CwlAnalysisOutputJson
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
    analysis_id = "analysisId_example" # str | The ID of the CWL analysis for which to retrieve the output json

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the output json of a CWL analysis.
        api_response = api_instance.get_cwl_output_json(project_id, analysis_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_output_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the output json |

### Return type

[**CwlAnalysisOutputJson**](CwlAnalysisOutputJson.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output json of the CWL analysis is successfully retrieved. |  -  |
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

# **search_analyses**
> AnalysisPagedListV4 search_analyses(project_id)

Search analyses.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_query_parameters import AnalysisQueryParameters
from libica.openapi.v2.model.analysis_paged_list_v4 import AnalysisPagedListV4
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
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = "sort_example" # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)
    analysis_query_parameters = AnalysisQueryParameters(
        reference="reference_example",
        user_reference="user_reference_example",
        status=[
            "SUCCEEDED",
        ],
        user_tags=[
            "user_tags_example",
        ],
        technical_tags=[
            "technical_tags_example",
        ],
        reference_tags=[
            "reference_tags_example",
        ],
    ) # AnalysisQueryParameters |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search analyses.
        api_response = api_instance.search_analyses(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->search_analyses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search analyses.
        api_response = api_instance.search_analyses(project_id, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, analysis_query_parameters=analysis_query_parameters)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->search_analyses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional]
 **analysis_query_parameters** | [**AnalysisQueryParameters**](AnalysisQueryParameters.md)|  | [optional]

### Return type

[**AnalysisPagedListV4**](AnalysisPagedListV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> AnalysisV4 update_analysis(project_id, analysis_id, analysis_v4)

Update an analysis.

# Attributes which can be updated:    - tags # Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3]  * Initial version ## [V4]  * Field type 'status' changed from enum to String. New statuses have been added: ['QUEUED', 'INITIALIZING', 'PREPARING_INPUTS', 'GENERATING_OUTPUTS', 'ABORTING'].  * Field analysisPriority changed from enum to String.  * The owner and tenant are now represented by Identifier objects. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_analysis_api
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
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
    analysis_v4 = AnalysisV4(
        id="id_example",
        time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
        owner=UserIdentifier(
            id="id_example",
        ),
        tenant=TenantIdentifier(
            id="id_example",
            name="name_example",
        ),
        reference="reference_example",
        user_reference="user_reference_example",
        pipeline=PipelineV4(
            id="id_example",
            urn="urn_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            time_modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner=UserIdentifier(
                id="id_example",
            ),
            tenant=TenantIdentifier(
                id="id_example",
                name="name_example",
            ),
            code="code_example",
            description="description_example",
            status="DRAFT",
            language="CWL",
            language_version=PipelineLanguageVersion(
                id="id_example",
                name="name_example",
                language="CWL",
            ),
            pipeline_tags=PipelineTag(
                technical_tags=[
                    "technical_tags_example",
                ],
            ),
            analysis_storage=AnalysisStorageV4(
                id="id_example",
                name="name_example",
                description="description_example",
            ),
            proprietary=False,
        ),
        workflow_session=WorkflowSessionV4(
            id="id_example",
            time_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
            owner=UserIdentifier(
                id="id_example",
            ),
            tenant=TenantIdentifier(
                id="id_example",
                name="name_example",
            ),
            user_reference="user_reference_example",
            workflow=WorkflowV4(
                id="id_example",
                code="code_example",
                urn="urn_example",
                description="description_example",
                language_version=PipelineLanguageVersion(
                    id="id_example",
                    name="name_example",
                    language="CWL",
                ),
                workflow_tags=PipelineTag(
                    technical_tags=[
                        "technical_tags_example",
                    ],
                ),
                analysis_storage=AnalysisStorageV4(
                    id="id_example",
                    name="name_example",
                    description="description_example",
                ),
            ),
            status="SUCCEEDED",
            start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            summary="summary_example",
            tags=WorkflowSessionTag(
                technical_tags=[
                    "technical_tags_example",
                ],
                user_tags=[
                    "user_tags_example",
                ],
            ),
        ),
        status="SUCCEEDED",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        summary="summary_example",
        analysis_storage=AnalysisStorageV4(
            id="id_example",
            name="name_example",
            description="description_example",
        ),
        analysis_priority="HIG",
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
    ) # AnalysisV4 | 
    if_match = "If-Match_example" # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id, analysis_v4)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id, analysis_v4, if_match=if_match)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **analysis_id** | **str**|  |
 **analysis_v4** | [**AnalysisV4**](AnalysisV4.md)|  |
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional]

### Return type

[**AnalysisV4**](AnalysisV4.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

