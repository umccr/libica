# PipelineV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**urn** | **str** | The URN of the pipeline. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**pipeline_group** | [**PipelineGroupIdentifier**](PipelineGroupIdentifier.md) |  | [optional] 
**code** | **str** | The code of the pipeline. This is deprecated, use the name &amp; version attributes instead | 
**name** | **str** | The name of the pipeline | [optional] 
**description** | **str** | The description of the pipeline | 
**status** | **str** | The status of the pipeline | [optional] 
**status_as_string** | **str** | The status of the pipeline as string (&#39;Draft&#39;, &#39;Released&#39;, &#39;Deprecated&#39;, &#39;Archived&#39;, &#39;Importing&#39;, &#39;Import Cancelling&#39;, &#39;Import Incomplete&#39;, &#39;Import Failed&#39;) | [optional] 
**language** | **str** | The language that is used by the pipeline | 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**pipeline_tags** | [**PipelineTag**](PipelineTag.md) |  | 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | 
**proprietary** | **bool** | A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
**input_form_type** | **str** | The type of the inputform used. | [optional] 
**report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md) |  | [optional] 
**resources** | [**PipelineResources**](PipelineResources.md) |  | [optional] 
**git_pipeline_import** | [**GitPipelineImport**](GitPipelineImport.md) |  | [optional] 
**version** | **str** | The version number of the pipeline | [optional] 
**latest_version_in_group** | **bool** |  | [optional] 
**pipeline_usage** | [**PipelineUsage**](PipelineUsage.md) |  | [optional] 
**icon_name** | **str** | The icon name of the pipeline | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_v4 import PipelineV4

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineV4 from a JSON string
pipeline_v4_instance = PipelineV4.from_json(json)
# print the JSON string representation of the object
print(PipelineV4.to_json())

# convert the object into a dict
pipeline_v4_dict = pipeline_v4_instance.to_dict()
# create an instance of PipelineV4 from a dict
pipeline_v4_from_dict = PipelineV4.from_dict(pipeline_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


