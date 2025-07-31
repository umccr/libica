# PipelineV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** | The code of the pipeline | 
**urn** | **str** | The URN of the pipeline. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**description** | **str** | The description of the pipeline | 
**status** | **str** | The status of the pipeline | [optional] 
**language** | **str** | The language that is used by the pipeline | 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**pipeline_tags** | [**PipelineTag**](PipelineTag.md) |  | 
**analysis_storage** | [**AnalysisStorageV3**](AnalysisStorageV3.md) |  | 
**proprietary** | **bool** | A boolean which indicates if the code of this pipeline is proprietary | [optional] [default to False]
**input_form_type** | **str** | The type of the inputform used. | [optional] 
**resources** | [**PipelineResources**](PipelineResources.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_v3 import PipelineV3

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineV3 from a JSON string
pipeline_v3_instance = PipelineV3.from_json(json)
# print the JSON string representation of the object
print(PipelineV3.to_json())

# convert the object into a dict
pipeline_v3_dict = pipeline_v3_instance.to_dict()
# create an instance of PipelineV3 from a dict
pipeline_v3_from_dict = PipelineV3.from_dict(pipeline_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


