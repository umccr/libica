# libica.openapi.v2.ProjectPipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cwl_pipeline**](ProjectPipelineApi.md#create_cwl_pipeline) | **POST** /api/projects/{projectId}/pipelines:createCwlPipeline | Create a CWL pipeline within a project.
[**create_nextflow_pipeline**](ProjectPipelineApi.md#create_nextflow_pipeline) | **POST** /api/projects/{projectId}/pipelines:createNextflowPipeline | Create a Nextflow pipeline within a project.
[**get_project_pipeline**](ProjectPipelineApi.md#get_project_pipeline) | **GET** /api/projects/{projectId}/pipelines/{pipelineId} | Retrieve a project pipeline.
[**get_project_pipeline_html_documentation**](ProjectPipelineApi.md#get_project_pipeline_html_documentation) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_project_pipeline_input_parameters**](ProjectPipelineApi.md#get_project_pipeline_input_parameters) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a project pipeline.
[**get_project_pipeline_reference_sets**](ProjectPipelineApi.md#get_project_pipeline_reference_sets) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a project pipeline.
[**get_project_pipelines**](ProjectPipelineApi.md#get_project_pipelines) | **GET** /api/projects/{projectId}/pipelines | Retrieve a list of project pipelines.
[**link_pipeline_to_project**](ProjectPipelineApi.md#link_pipeline_to_project) | **POST** /api/projects/{projectId}/pipelines/{pipelineId} | Link a pipeline to a project.
[**release_pipeline**](ProjectPipelineApi.md#release_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}:release | Release a pipeline.
[**unlink_pipeline_from_project**](ProjectPipelineApi.md#unlink_pipeline_from_project) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId} | Unlink a pipeline from a project.


# **create_cwl_pipeline**
> ProjectPipeline create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id)

Create a CWL pipeline within a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.project_pipeline import ProjectPipeline
from libica.openapi.v2.model.links import Links
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    code = "26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW" # str | The code of the CWL pipeline
    description = "description_example" # str | The description of the CWL pipeline
    workflow_cwl_file = open('/path/to/file', 'rb') # file_type | The CWL workflow file.
    parameters_xml_file = open('/path/to/file', 'rb') # file_type | 
    analysis_storage_id = "analysis_storage_id_example" # str | The id of the storage to use for the pipeline.
    tool_cwl_files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)
    metadata_model_file = open('/path/to/file', 'rb') # file_type, none_type | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = Links(
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
    ) # Links |  (optional)
    version_comment = "version_comment_example" # str, none_type |  (optional)
    categories = [
        "categories_example",
    ] # [str, none_type], none_type |  (optional)
    html_documentation = "html_documentation_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **code** | **str**| The code of the CWL pipeline |
 **description** | **str**| The description of the CWL pipeline |
 **workflow_cwl_file** | **file_type**| The CWL workflow file. |
 **parameters_xml_file** | **file_type**|  |
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. |
 **tool_cwl_files** | **[file_type]**|  | [optional]
 **metadata_model_file** | **file_type, none_type**| The metadata model json file(contents can be retrieved from the controlplane). | [optional]
 **links** | [**Links**](Links.md)|  | [optional]
 **version_comment** | **str, none_type**|  | [optional]
 **categories** | [**[str, none_type], none_type**](str, none_type.md)|  | [optional]
 **html_documentation** | **str, none_type**|  | [optional]

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The CWL pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_pipeline**
> ProjectPipeline create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id)

Create a Nextflow pipeline within a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.project_pipeline import ProjectPipeline
from libica.openapi.v2.model.links import Links
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    code = "26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW" # str | The code of the pipeline
    description = "description_example" # str | The description of the pipeline
    main_nextflow_file = open('/path/to/file', 'rb') # file_type | The main Nextflow file.
    parameters_xml_file = open('/path/to/file', 'rb') # file_type | 
    analysis_storage_id = "analysis_storage_id_example" # str | The id of the storage to use for the pipeline.
    pipeline_language_version_id = "pipeline_language_version_id_example" # str, none_type | The id of the Nextflow version to use for the pipeline. (optional)
    nextflow_config_file = open('/path/to/file', 'rb') # file_type | The Nextflow config file. (optional)
    other_nextflow_files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)
    metadata_model_file = open('/path/to/file', 'rb') # file_type, none_type | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = Links(
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
    ) # Links |  (optional)
    version_comment = "version_comment_example" # str, none_type |  (optional)
    categories = [
        "categories_example",
    ] # [str, none_type], none_type |  (optional)
    html_documentation = "html_documentation_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **code** | **str**| The code of the pipeline |
 **description** | **str**| The description of the pipeline |
 **main_nextflow_file** | **file_type**| The main Nextflow file. |
 **parameters_xml_file** | **file_type**|  |
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. |
 **pipeline_language_version_id** | **str, none_type**| The id of the Nextflow version to use for the pipeline. | [optional]
 **nextflow_config_file** | **file_type**| The Nextflow config file. | [optional]
 **other_nextflow_files** | **[file_type]**|  | [optional]
 **metadata_model_file** | **file_type, none_type**| The metadata model json file(contents can be retrieved from the controlplane). | [optional]
 **links** | [**Links**](Links.md)|  | [optional]
 **version_comment** | **str, none_type**|  | [optional]
 **categories** | [**[str, none_type], none_type**](str, none_type.md)|  | [optional]
 **html_documentation** | **str, none_type**|  | [optional]

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Nextflow pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline**
> ProjectPipeline get_project_pipeline(project_id, pipeline_id)

Retrieve a project pipeline.

Retrieves a project pipeline. This can be a pipeline from a linked bundle or an entitled, unlinked bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.project_pipeline import ProjectPipeline
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a project pipeline.
        api_response = api_instance.get_project_pipeline(project_id, pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve |

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project pipeline is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_html_documentation**
> PipelineHtmlDocumentation get_project_pipeline_html_documentation(project_id, pipeline_id)

Retrieve HTML documentation for a project pipeline.

Retrieve HTML documentation for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve HTML documentation from

    # example passing only required values which don't have defaults set
    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_project_pipeline_html_documentation(project_id, pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_html_documentation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve HTML documentation from |

### Return type

[**PipelineHtmlDocumentation**](PipelineHtmlDocumentation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTML documentation is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_input_parameters**
> InputParameterList get_project_pipeline_input_parameters(project_id, pipeline_id)

Retrieve input parameters for a project pipeline.

Retrieve input parameters for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.input_parameter_list import InputParameterList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the project pipeline to retrieve input parameters for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve input parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_input_parameters(project_id, pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_input_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve input parameters for |

### Return type

[**InputParameterList**](InputParameterList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_reference_sets**
> ReferenceSetList get_project_pipeline_reference_sets(project_id, pipeline_id)

Retrieve the reference sets of a project pipeline.

Retrieve the reference sets of a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.reference_set_list import ReferenceSetList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline to retrieve reference sets for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the reference sets of a project pipeline.
        api_response = api_instance.get_project_pipeline_reference_sets(project_id, pipeline_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_reference_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the pipeline to retrieve reference sets for |

### Return type

[**ReferenceSetList**](ReferenceSetList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of reference sets is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipelines**
> ProjectPipelineList get_project_pipelines(project_id)

Retrieve a list of project pipelines.

Lists all pipelines that are available to the project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
from libica.openapi.v2.model.project_pipeline_list import ProjectPipelineList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | The ID of the project to retrieve pipelines for

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of project pipelines.
        api_response = api_instance.get_project_pipelines(project_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to retrieve pipelines for |

### Return type

[**ProjectPipelineList**](ProjectPipelineList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project pipelines is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_pipeline_to_project**
> link_pipeline_to_project(project_id, pipeline_id)

Link a pipeline to a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline

    # example passing only required values which don't have defaults set
    try:
        # Link a pipeline to a project.
        api_instance.link_pipeline_to_project(project_id, pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->link_pipeline_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the pipeline |

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
**204** | The pipeline is successfully linked to the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_pipeline**
> release_pipeline(project_id, pipeline_id)

Release a pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline

    # example passing only required values which don't have defaults set
    try:
        # Release a pipeline.
        api_instance.release_pipeline(project_id, pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->release_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the pipeline |

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
**204** | The pipeline is successfully released. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_pipeline_from_project**
> unlink_pipeline_from_project(project_id, pipeline_id)

Unlink a pipeline from a project.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)
    project_id = "projectId_example" # str | 
    pipeline_id = "pipelineId_example" # str | The ID of the pipeline

    # example passing only required values which don't have defaults set
    try:
        # Unlink a pipeline from a project.
        api_instance.unlink_pipeline_from_project(project_id, pipeline_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling ProjectPipelineApi->unlink_pipeline_from_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **pipeline_id** | **str**| The ID of the pipeline |

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
**204** | The pipeline is successfully unlinked from the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

