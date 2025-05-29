# WorkflowV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** | The code of the workflow | 
**urn** | **str** | The URN of the workflow. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | 
**description** | **str** | The description of the workflow | 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**workflow_tags** | [**PipelineTag**](PipelineTag.md) |  | [optional] 
**analysis_storage** | [**AnalysisStorageV3**](AnalysisStorageV3.md) |  | 

## Example

```python
from libica.openapi.v3.models.workflow_v3 import WorkflowV3

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowV3 from a JSON string
workflow_v3_instance = WorkflowV3.from_json(json)
# print the JSON string representation of the object
print(WorkflowV3.to_json())

# convert the object into a dict
workflow_v3_dict = workflow_v3_instance.to_dict()
# create an instance of WorkflowV3 from a dict
workflow_v3_from_dict = WorkflowV3.from_dict(workflow_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


