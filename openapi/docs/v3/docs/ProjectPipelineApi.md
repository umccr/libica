# libica.openapi.v3.ProjectPipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_project_pipeline**](ProjectPipelineApi.md#archive_project_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}:archive | Archive a pipeline.
[**create_additional_project_pipeline_file**](ProjectPipelineApi.md#create_additional_project_pipeline_file) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/additionalFiles | Create an additional input form file for a pipeline.
[**create_cwl_json_pipeline**](ProjectPipelineApi.md#create_cwl_json_pipeline) | **POST** /api/projects/{projectId}/pipelines:createCwlJsonPipeline | Create a JSON based CWL pipeline within a project.
[**create_cwl_json_pipeline_from_git**](ProjectPipelineApi.md#create_cwl_json_pipeline_from_git) | **POST** /api/projects/{projectId}/pipelines:createCwlJsonPipelineFromGit | Create a JSON based CWL pipeline within a project from Git.
[**create_cwl_pipeline**](ProjectPipelineApi.md#create_cwl_pipeline) | **POST** /api/projects/{projectId}/pipelines:createCwlPipeline | Create a CWL pipeline within a project.
[**create_nextflow_json_pipeline**](ProjectPipelineApi.md#create_nextflow_json_pipeline) | **POST** /api/projects/{projectId}/pipelines:createNextflowJsonPipeline | Create a JSON based Nextflow pipeline within a project.
[**create_nextflow_json_pipeline_from_git**](ProjectPipelineApi.md#create_nextflow_json_pipeline_from_git) | **POST** /api/projects/{projectId}/pipelines:createNextflowJsonPipelineFromGit | Create a JSON based Nextflow pipeline within a project from Git.
[**create_nextflow_pipeline**](ProjectPipelineApi.md#create_nextflow_pipeline) | **POST** /api/projects/{projectId}/pipelines:createNextflowPipeline | Create a Nextflow pipeline within a project.
[**create_project_pipeline_file**](ProjectPipelineApi.md#create_project_pipeline_file) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/files | Create a file for a pipeline.
[**delete_additional_project_pipeline_file**](ProjectPipelineApi.md#delete_additional_project_pipeline_file) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/additionalFiles/{fileId} | Delete an additional input form file for a pipeline.
[**delete_project_pipeline_file**](ProjectPipelineApi.md#delete_project_pipeline_file) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId} | Delete a file for a pipeline.
[**deprecate_project_pipeline**](ProjectPipelineApi.md#deprecate_project_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}:deprecate | Deprecate a pipeline.
[**download_additional_file_content**](ProjectPipelineApi.md#download_additional_file_content) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/additionalFiles/{fileId}/content | Download the contents of an additional input form file.
[**download_input_form_file_content**](ProjectPipelineApi.md#download_input_form_file_content) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/inputFormFile | Download the contents of the input form file.
[**download_on_render_file_content**](ProjectPipelineApi.md#download_on_render_file_content) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/onRenderFile | Download the contents of the onRender file.
[**download_on_submit_file_content**](ProjectPipelineApi.md#download_on_submit_file_content) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/onSubmitFile | Download the contents of the onSubmit file.
[**download_project_pipeline_file_content**](ProjectPipelineApi.md#download_project_pipeline_file_content) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId}/content | Download the contents of a pipeline file.
[**get_project_pipeline**](ProjectPipelineApi.md#get_project_pipeline) | **GET** /api/projects/{projectId}/pipelines/{pipelineId} | Retrieve a project pipeline.
[**get_project_pipeline_additional_files**](ProjectPipelineApi.md#get_project_pipeline_additional_files) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/additionalFiles | Retrieve additional input form files for a project pipeline.
[**get_project_pipeline_configuration_parameters**](ProjectPipelineApi.md#get_project_pipeline_configuration_parameters) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/configurationParameters | Retrieve configuration parameters for a project pipeline.
[**get_project_pipeline_cwl_git_config**](ProjectPipelineApi.md#get_project_pipeline_cwl_git_config) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/cwlGitConfig | Retrieve git config for a CWL project pipeline.
[**get_project_pipeline_files**](ProjectPipelineApi.md#get_project_pipeline_files) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/files | Retrieve files for a project pipeline.
[**get_project_pipeline_html_documentation**](ProjectPipelineApi.md#get_project_pipeline_html_documentation) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_project_pipeline_input_parameters**](ProjectPipelineApi.md#get_project_pipeline_input_parameters) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a project pipeline.
[**get_project_pipeline_nextflow_git_config**](ProjectPipelineApi.md#get_project_pipeline_nextflow_git_config) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/nextflowGitConfig | Retrieve git config for a Nextflow project pipeline.
[**get_project_pipeline_reference_sets**](ProjectPipelineApi.md#get_project_pipeline_reference_sets) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a project pipeline.
[**get_project_pipelines**](ProjectPipelineApi.md#get_project_pipelines) | **GET** /api/projects/{projectId}/pipelines | Retrieve a list of project pipelines.
[**link_pipeline_to_project**](ProjectPipelineApi.md#link_pipeline_to_project) | **POST** /api/projects/{projectId}/pipelines/{pipelineId} | Link a pipeline to a project.
[**release_project_pipeline**](ProjectPipelineApi.md#release_project_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}:release | Release a pipeline.
[**unlink_pipeline_from_project**](ProjectPipelineApi.md#unlink_pipeline_from_project) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId} | Unlink a pipeline from a project.
[**update_additional_file**](ProjectPipelineApi.md#update_additional_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/additionalFiles/{fileId}/content | Update the contents of an additional input form file.
[**update_cwl_git_config**](ProjectPipelineApi.md#update_cwl_git_config) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/cwlGitConfig:update | Update git config for CWL
[**update_general_attributes_project_pipeline**](ProjectPipelineApi.md#update_general_attributes_project_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/generalAttributes | Update the general attributes of a project pipeline.
[**update_input_form_file**](ProjectPipelineApi.md#update_input_form_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/inputFormFile | Update the contents of the input form file for a pipeline.
[**update_nextflow_git_config**](ProjectPipelineApi.md#update_nextflow_git_config) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/nextflowGitConfig:update | Update git config for Nextflow
[**update_on_render_file**](ProjectPipelineApi.md#update_on_render_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/onRenderFile | Update the contents of the onRender file for a pipeline.
[**update_on_submit_file**](ProjectPipelineApi.md#update_on_submit_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/inputForm/onSubmitFile | Update the contents of the onSubmit file for a pipeline.
[**update_project_pipeline_file**](ProjectPipelineApi.md#update_project_pipeline_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId}/content | Update the contents of a file for a pipeline.


# **archive_project_pipeline**
> archive_project_pipeline(project_id, pipeline_id, archive_pipeline=archive_pipeline)

Archive a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.archive_pipeline import ArchivePipeline
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    archive_pipeline = libica.openapi.v3.ArchivePipeline() # ArchivePipeline |  (optional)

    try:
        # Archive a pipeline.
        api_instance.archive_project_pipeline(project_id, pipeline_id, archive_pipeline=archive_pipeline)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->archive_project_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **archive_pipeline** | [**ArchivePipeline**](ArchivePipeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully archived. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_additional_project_pipeline_file**
> PipelineFile create_additional_project_pipeline_file(project_id, pipeline_id, content)

Create an additional input form file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_file import PipelineFile
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to create a file for
    content = None # bytearray | 

    try:
        # Create an additional input form file for a pipeline.
        api_response = api_instance.create_additional_project_pipeline_file(project_id, pipeline_id, content)
        print("The response of ProjectPipelineApi->create_additional_project_pipeline_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_additional_project_pipeline_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to create a file for | 
 **content** | **bytearray**|  | 

### Return type

[**PipelineFile**](PipelineFile.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pipeline file is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_json_pipeline**
> ProjectPipelineV4 create_cwl_json_pipeline(project_id, code, description, workflow_cwl_file, input_form_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a JSON based CWL pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.project_pipeline_v4 import ProjectPipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the CWL pipeline
    description = 'description_example' # str | The description of the CWL pipeline
    workflow_cwl_file = None # bytearray | The CWL workflow file.
    input_form_file = None # bytearray | The JSON based input form.
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    tool_cwl_files = None # List[bytearray] |  (optional)
    on_render_file = None # bytearray | A file that will render the current state of the input form. (optional)
    on_submit_file = None # bytearray | A file that will submit the current state of the input form. (optional)
    other_input_form_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a JSON based CWL pipeline within a project.
        api_response = api_instance.create_cwl_json_pipeline(project_id, code, description, workflow_cwl_file, input_form_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_cwl_json_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_json_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the CWL pipeline | 
 **description** | **str**| The description of the CWL pipeline | 
 **workflow_cwl_file** | **bytearray**| The CWL workflow file. | 
 **input_form_file** | **bytearray**| The JSON based input form. | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **tool_cwl_files** | **List[bytearray]**|  | [optional] 
 **on_render_file** | **bytearray**| A file that will render the current state of the input form. | [optional] 
 **on_submit_file** | **bytearray**| A file that will submit the current state of the input form. | [optional] 
 **other_input_form_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**ProjectPipelineV4**](ProjectPipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The CWL pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_json_pipeline_from_git**
> ProjectPipelineV4 create_cwl_json_pipeline_from_git(project_id, code, description, input_form_file, analysis_storage_id, cwl_git_config, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a JSON based CWL pipeline within a project from Git.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.cwl_git_config import CwlGitConfig
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.project_pipeline_v4 import ProjectPipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the CWL pipeline
    description = 'description_example' # str | The description of the CWL pipeline
    input_form_file = None # bytearray | The JSON based input form.
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    cwl_git_config = libica.openapi.v3.CwlGitConfig() # CwlGitConfig | 
    on_render_file = None # bytearray | A file that will render the current state of the input form. (optional)
    on_submit_file = None # bytearray | A file that will submit the current state of the input form. (optional)
    other_input_form_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a JSON based CWL pipeline within a project from Git.
        api_response = api_instance.create_cwl_json_pipeline_from_git(project_id, code, description, input_form_file, analysis_storage_id, cwl_git_config, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_cwl_json_pipeline_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_json_pipeline_from_git: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the CWL pipeline | 
 **description** | **str**| The description of the CWL pipeline | 
 **input_form_file** | **bytearray**| The JSON based input form. | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **cwl_git_config** | [**CwlGitConfig**](CwlGitConfig.md)|  | 
 **on_render_file** | **bytearray**| A file that will render the current state of the input form. | [optional] 
 **on_submit_file** | **bytearray**| A file that will submit the current state of the input form. | [optional] 
 **other_input_form_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**ProjectPipelineV4**](ProjectPipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The CWL pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_pipeline**
> ProjectPipeline create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a CWL pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.project_pipeline import ProjectPipeline
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the CWL pipeline
    description = 'description_example' # str | The description of the CWL pipeline
    workflow_cwl_file = None # bytearray | The CWL workflow file.
    parameters_xml_file = None # bytearray | 
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    tool_cwl_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_cwl_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the CWL pipeline | 
 **description** | **str**| The description of the CWL pipeline | 
 **workflow_cwl_file** | **bytearray**| The CWL workflow file. | 
 **parameters_xml_file** | **bytearray**|  | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **tool_cwl_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The CWL pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_json_pipeline**
> PipelineV4 create_nextflow_json_pipeline(project_id, code, description, main_nextflow_file, input_form_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a JSON based Nextflow pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.pipeline_v4 import PipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the pipeline
    description = 'description_example' # str | The description of the pipeline
    main_nextflow_file = None # bytearray | The main Nextflow file.
    input_form_file = None # bytearray | The JSON based input form.
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    pipeline_language_version_id = 'pipeline_language_version_id_example' # str | The id of the Nextflow version to use for the pipeline. (optional)
    nextflow_config_file = None # bytearray | The Nextflow config file. (optional)
    other_nextflow_files = None # List[bytearray] |  (optional)
    on_render_file = None # bytearray | A file that will render the current state of the input form. (optional)
    on_submit_file = None # bytearray | A file that will submit the current state of the input form. (optional)
    other_input_form_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a JSON based Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_json_pipeline(project_id, code, description, main_nextflow_file, input_form_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_nextflow_json_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_json_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the pipeline | 
 **description** | **str**| The description of the pipeline | 
 **main_nextflow_file** | **bytearray**| The main Nextflow file. | 
 **input_form_file** | **bytearray**| The JSON based input form. | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **pipeline_language_version_id** | **str**| The id of the Nextflow version to use for the pipeline. | [optional] 
 **nextflow_config_file** | **bytearray**| The Nextflow config file. | [optional] 
 **other_nextflow_files** | **List[bytearray]**|  | [optional] 
 **on_render_file** | **bytearray**| A file that will render the current state of the input form. | [optional] 
 **on_submit_file** | **bytearray**| A file that will submit the current state of the input form. | [optional] 
 **other_input_form_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**PipelineV4**](PipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Nextflow pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_json_pipeline_from_git**
> PipelineV4 create_nextflow_json_pipeline_from_git(project_id, code, description, input_form_file, analysis_storage_id, nextflow_git_config, pipeline_language_version_id=pipeline_language_version_id, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a JSON based Nextflow pipeline within a project from Git.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.nextflow_git_config import NextflowGitConfig
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.pipeline_v4 import PipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the pipeline
    description = 'description_example' # str | The description of the pipeline
    input_form_file = None # bytearray | The JSON based input form.
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    nextflow_git_config = libica.openapi.v3.NextflowGitConfig() # NextflowGitConfig | 
    pipeline_language_version_id = 'pipeline_language_version_id_example' # str | The id of the Nextflow version to use for the pipeline. (optional)
    on_render_file = None # bytearray | A file that will render the current state of the input form. (optional)
    on_submit_file = None # bytearray | A file that will submit the current state of the input form. (optional)
    other_input_form_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a JSON based Nextflow pipeline within a project from Git.
        api_response = api_instance.create_nextflow_json_pipeline_from_git(project_id, code, description, input_form_file, analysis_storage_id, nextflow_git_config, pipeline_language_version_id=pipeline_language_version_id, on_render_file=on_render_file, on_submit_file=on_submit_file, other_input_form_files=other_input_form_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_nextflow_json_pipeline_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_json_pipeline_from_git: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the pipeline | 
 **description** | **str**| The description of the pipeline | 
 **input_form_file** | **bytearray**| The JSON based input form. | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **nextflow_git_config** | [**NextflowGitConfig**](NextflowGitConfig.md)|  | 
 **pipeline_language_version_id** | **str**| The id of the Nextflow version to use for the pipeline. | [optional] 
 **on_render_file** | **bytearray**| A file that will render the current state of the input form. | [optional] 
 **on_submit_file** | **bytearray**| A file that will submit the current state of the input form. | [optional] 
 **other_input_form_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**PipelineV4**](PipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Nextflow pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_pipeline**
> ProjectPipeline create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)

Create a Nextflow pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.links import Links
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig
from libica.openapi.v3.models.pipeline_resources import PipelineResources
from libica.openapi.v3.models.project_pipeline import ProjectPipeline
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the pipeline
    description = 'description_example' # str | The description of the pipeline
    main_nextflow_file = None # bytearray | The main Nextflow file.
    parameters_xml_file = None # bytearray | 
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    pipeline_language_version_id = 'pipeline_language_version_id_example' # str | The id of the Nextflow version to use for the pipeline. (optional)
    nextflow_config_file = None # bytearray | The Nextflow config file. (optional)
    other_nextflow_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = libica.openapi.v3.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[Optional[str]] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)
    proprietary = False # bool | A boolean which indicates if the code of this pipeline is proprietary (optional) (default to False)
    report_configs = libica.openapi.v3.PipelineReportConfig() # PipelineReportConfig |  (optional)
    resources = libica.openapi.v3.PipelineResources() # PipelineResources |  (optional)

    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation, proprietary=proprietary, report_configs=report_configs, resources=resources)
        print("The response of ProjectPipelineApi->create_nextflow_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the pipeline | 
 **description** | **str**| The description of the pipeline | 
 **main_nextflow_file** | **bytearray**| The main Nextflow file. | 
 **parameters_xml_file** | **bytearray**|  | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **pipeline_language_version_id** | **str**| The id of the Nextflow version to use for the pipeline. | [optional] 
 **nextflow_config_file** | **bytearray**| The Nextflow config file. | [optional] 
 **other_nextflow_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 
 **proprietary** | **bool**| A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
 **report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md)|  | [optional] 
 **resources** | [**PipelineResources**](PipelineResources.md)|  | [optional] 

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Nextflow pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_pipeline_file**
> PipelineFile create_project_pipeline_file(project_id, pipeline_id, content)

Create a file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_file import PipelineFile
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to create a file for
    content = None # bytearray | 

    try:
        # Create a file for a pipeline.
        api_response = api_instance.create_project_pipeline_file(project_id, pipeline_id, content)
        print("The response of ProjectPipelineApi->create_project_pipeline_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_project_pipeline_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to create a file for | 
 **content** | **bytearray**|  | 

### Return type

[**PipelineFile**](PipelineFile.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pipeline file is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_additional_project_pipeline_file**
> delete_additional_project_pipeline_file(project_id, pipeline_id, file_id)

Delete an additional input form file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to delete an additional file for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Delete an additional input form file for a pipeline.
        api_instance.delete_additional_project_pipeline_file(project_id, pipeline_id, file_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->delete_additional_project_pipeline_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to delete an additional file for | 
 **file_id** | **str**| The ID of the pipeline file | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline file is successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_pipeline_file**
> delete_project_pipeline_file(project_id, pipeline_id, file_id)

Delete a file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to delete a file for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Delete a file for a pipeline.
        api_instance.delete_project_pipeline_file(project_id, pipeline_id, file_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->delete_project_pipeline_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to delete a file for | 
 **file_id** | **str**| The ID of the pipeline file | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline file is successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecate_project_pipeline**
> deprecate_project_pipeline(project_id, pipeline_id, deprecate_pipeline=deprecate_pipeline)

Deprecate a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.deprecate_pipeline import DeprecatePipeline
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    deprecate_pipeline = libica.openapi.v3.DeprecatePipeline() # DeprecatePipeline |  (optional)

    try:
        # Deprecate a pipeline.
        api_instance.deprecate_project_pipeline(project_id, pipeline_id, deprecate_pipeline=deprecate_pipeline)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->deprecate_project_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **deprecate_pipeline** | [**DeprecatePipeline**](DeprecatePipeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully deprecated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_additional_file_content**
> bytearray download_additional_file_content(project_id, pipeline_id, file_id)

Download the contents of an additional input form file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the additional file for
    file_id = 'file_id_example' # str | The ID of the additional file

    try:
        # Download the contents of an additional input form file.
        api_response = api_instance.download_additional_file_content(project_id, pipeline_id, file_id)
        print("The response of ProjectPipelineApi->download_additional_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_additional_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the additional file for | 
 **file_id** | **str**| The ID of the additional file | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_input_form_file_content**
> bytearray download_input_form_file_content(project_id, pipeline_id)

Download the contents of the input form file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the input form file for

    try:
        # Download the contents of the input form file.
        api_response = api_instance.download_input_form_file_content(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->download_input_form_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_input_form_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the input form file for | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input form file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_on_render_file_content**
> bytearray download_on_render_file_content(project_id, pipeline_id)

Download the contents of the onRender file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the onRender file for

    try:
        # Download the contents of the onRender file.
        api_response = api_instance.download_on_render_file_content(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->download_on_render_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_on_render_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the onRender file for | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The onRender file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_on_submit_file_content**
> bytearray download_on_submit_file_content(project_id, pipeline_id)

Download the contents of the onSubmit file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the onSubmit file for

    try:
        # Download the contents of the onSubmit file.
        api_response = api_instance.download_on_submit_file_content(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->download_on_submit_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_on_submit_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the onSubmit file for | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The onSubmit file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_project_pipeline_file_content**
> bytearray download_project_pipeline_file_content(project_id, pipeline_id, file_id)

Download the contents of a pipeline file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Download the contents of a pipeline file.
        api_response = api_instance.download_project_pipeline_file_content(project_id, pipeline_id, file_id)
        print("The response of ProjectPipelineApi->download_project_pipeline_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_project_pipeline_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 
 **file_id** | **str**| The ID of the pipeline file | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline file is successfully downloaded. |  * Content-Disposition - Contains name of the additional file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline**
> ProjectPipelineV4 get_project_pipeline(project_id, pipeline_id)

Retrieve a project pipeline.

Retrieves a project pipeline. This can be a pipeline from a linked bundle or an entitled, unlinked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_pipeline_v4 import ProjectPipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve

    try:
        # Retrieve a project pipeline.
        api_response = api_instance.get_project_pipeline(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve | 

### Return type

[**ProjectPipelineV4**](ProjectPipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project pipeline is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_additional_files**
> PipelineFileList get_project_pipeline_additional_files(project_id, pipeline_id)

Retrieve additional input form files for a project pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_file_list import PipelineFileList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for

    try:
        # Retrieve additional input form files for a project pipeline.
        api_response = api_instance.get_project_pipeline_additional_files(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_additional_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_additional_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 

### Return type

[**PipelineFileList**](PipelineFileList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The files are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_configuration_parameters**
> PipelineConfigurationParameterList get_project_pipeline_configuration_parameters(project_id, pipeline_id)

Retrieve configuration parameters for a project pipeline.

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve input parameters for

    try:
        # Retrieve configuration parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_configuration_parameters(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_configuration_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_configuration_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve input parameters for | 

### Return type

[**PipelineConfigurationParameterList**](PipelineConfigurationParameterList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_cwl_git_config**
> CwlGitConfig get_project_pipeline_cwl_git_config(project_id, pipeline_id)

Retrieve git config for a CWL project pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.cwl_git_config import CwlGitConfig
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the git config for

    try:
        # Retrieve git config for a CWL project pipeline.
        api_response = api_instance.get_project_pipeline_cwl_git_config(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_cwl_git_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_cwl_git_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the git config for | 

### Return type

[**CwlGitConfig**](CwlGitConfig.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The git config is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_files**
> PipelineFileList get_project_pipeline_files(project_id, pipeline_id)

Retrieve files for a project pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_file_list import PipelineFileList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for

    try:
        # Retrieve files for a project pipeline.
        api_response = api_instance.get_project_pipeline_files(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 

### Return type

[**PipelineFileList**](PipelineFileList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The files are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_html_documentation**
> PipelineHtmlDocumentation get_project_pipeline_html_documentation(project_id, pipeline_id)

Retrieve HTML documentation for a project pipeline.

Retrieve HTML documentation for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve HTML documentation from

    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_project_pipeline_html_documentation(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_html_documentation:\n")
        pprint(api_response)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.input_parameter_list import InputParameterList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve input parameters for

    try:
        # Retrieve input parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_input_parameters(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_input_parameters:\n")
        pprint(api_response)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_nextflow_git_config**
> NextflowGitConfig get_project_pipeline_nextflow_git_config(project_id, pipeline_id)

Retrieve git config for a Nextflow project pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.nextflow_git_config import NextflowGitConfig
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve the git config for

    try:
        # Retrieve git config for a Nextflow project pipeline.
        api_response = api_instance.get_project_pipeline_nextflow_git_config(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_nextflow_git_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_nextflow_git_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve the git config for | 

### Return type

[**NextflowGitConfig**](NextflowGitConfig.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The git config is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_reference_sets**
> ReferenceSetList get_project_pipeline_reference_sets(project_id, pipeline_id)

Retrieve the reference sets of a project pipeline.

Retrieve the reference sets of a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.reference_set_list import ReferenceSetList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline to retrieve reference sets for

    try:
        # Retrieve the reference sets of a project pipeline.
        api_response = api_instance.get_project_pipeline_reference_sets(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_reference_sets:\n")
        pprint(api_response)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.project_pipeline_list import ProjectPipelineList
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project to retrieve pipelines for

    try:
        # Retrieve a list of project pipelines.
        api_response = api_instance.get_project_pipelines(project_id)
        print("The response of ProjectPipelineApi->get_project_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipelines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to retrieve pipelines for | 

### Return type

[**ProjectPipelineList**](ProjectPipelineList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Link a pipeline to a project.
        api_instance.link_pipeline_to_project(project_id, pipeline_id)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully linked to the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_project_pipeline**
> release_project_pipeline(project_id, pipeline_id)

Release a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Release a pipeline.
        api_instance.release_project_pipeline(project_id, pipeline_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->release_project_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Unlink a pipeline from a project.
        api_instance.unlink_pipeline_from_project(project_id, pipeline_id)
    except Exception as e:
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

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline is successfully unlinked from the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_additional_file**
> update_additional_file(project_id, pipeline_id, file_id, content)

Update the contents of an additional input form file.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update the additional file for
    file_id = 'file_id_example' # str | The ID of the additional file
    content = None # bytearray | 

    try:
        # Update the contents of an additional input form file.
        api_instance.update_additional_file(project_id, pipeline_id, file_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_additional_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update the additional file for | 
 **file_id** | **str**| The ID of the additional file | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cwl_git_config**
> CwlGitConfig update_cwl_git_config(project_id, pipeline_id, update_cwl_git_config)

Update git config for CWL

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.cwl_git_config import CwlGitConfig
from libica.openapi.v3.models.update_cwl_git_config import UpdateCwlGitConfig
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline for which to update the git config.
    update_cwl_git_config = libica.openapi.v3.UpdateCwlGitConfig() # UpdateCwlGitConfig | 

    try:
        # Update git config for CWL
        api_response = api_instance.update_cwl_git_config(project_id, pipeline_id, update_cwl_git_config)
        print("The response of ProjectPipelineApi->update_cwl_git_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_cwl_git_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline for which to update the git config. | 
 **update_cwl_git_config** | [**UpdateCwlGitConfig**](UpdateCwlGitConfig.md)|  | 

### Return type

[**CwlGitConfig**](CwlGitConfig.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The git config is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_general_attributes_project_pipeline**
> PipelineV4 update_general_attributes_project_pipeline(project_id, pipeline_id, pipeline_update)

Update the general attributes of a project pipeline.

Attributes which can be updated:
- code
- description
- languageVersion
- proprietary
- resources


### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.pipeline_update import PipelineUpdate
from libica.openapi.v3.models.pipeline_v4 import PipelineV4
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update
    pipeline_update = libica.openapi.v3.PipelineUpdate() # PipelineUpdate | 

    try:
        # Update the general attributes of a project pipeline.
        api_response = api_instance.update_general_attributes_project_pipeline(project_id, pipeline_id, pipeline_update)
        print("The response of ProjectPipelineApi->update_general_attributes_project_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_general_attributes_project_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update | 
 **pipeline_update** | [**PipelineUpdate**](PipelineUpdate.md)|  | 

### Return type

[**PipelineV4**](PipelineV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_input_form_file**
> update_input_form_file(project_id, pipeline_id, content)

Update the contents of the input form file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update a file for
    content = None # bytearray | 

    try:
        # Update the contents of the input form file for a pipeline.
        api_instance.update_input_form_file(project_id, pipeline_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_input_form_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update a file for | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input  form file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nextflow_git_config**
> NextflowGitConfig update_nextflow_git_config(project_id, pipeline_id, update_nextflow_git_config)

Update git config for Nextflow

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.nextflow_git_config import NextflowGitConfig
from libica.openapi.v3.models.update_nextflow_git_config import UpdateNextflowGitConfig
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline for which to update the git config.
    update_nextflow_git_config = libica.openapi.v3.UpdateNextflowGitConfig() # UpdateNextflowGitConfig | 

    try:
        # Update git config for Nextflow
        api_response = api_instance.update_nextflow_git_config(project_id, pipeline_id, update_nextflow_git_config)
        print("The response of ProjectPipelineApi->update_nextflow_git_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_nextflow_git_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline for which to update the git config. | 
 **update_nextflow_git_config** | [**UpdateNextflowGitConfig**](UpdateNextflowGitConfig.md)|  | 

### Return type

[**NextflowGitConfig**](NextflowGitConfig.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The git config is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_on_render_file**
> update_on_render_file(project_id, pipeline_id, content)

Update the contents of the onRender file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update the onRender file for
    content = None # bytearray | 

    try:
        # Update the contents of the onRender file for a pipeline.
        api_instance.update_on_render_file(project_id, pipeline_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_on_render_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update the onRender file for | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The onRender file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_on_submit_file**
> update_on_submit_file(project_id, pipeline_id, content)

Update the contents of the onSubmit file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update the onSubmit file for
    content = None # bytearray | 

    try:
        # Update the contents of the onSubmit file for a pipeline.
        api_instance.update_on_submit_file(project_id, pipeline_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_on_submit_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update the onSubmit file for | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The onSubmit file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_pipeline_file**
> update_project_pipeline_file(project_id, pipeline_id, file_id, content)

Update the contents of a file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
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
    api_instance = libica.openapi.v3.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update a file for
    file_id = 'file_id_example' # str | The ID of the pipeline file
    content = None # bytearray | 

    try:
        # Update the contents of a file for a pipeline.
        api_instance.update_project_pipeline_file(project_id, pipeline_id, file_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_project_pipeline_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update a file for | 
 **file_id** | **str**| The ID of the pipeline file | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

