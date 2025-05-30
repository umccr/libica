# WorkflowV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** | The code of the workflow | 
**urn** | **str** | The URN of the workflow. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | 
**description** | **str** | The description of the workflow | 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**workflow_tags** | [**PipelineTag**](PipelineTag.md) |  | [optional] 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | 

## Example

```python
from libica.openapi.v3.models.workflow_v4 import WorkflowV4

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowV4 from a JSON string
workflow_v4_instance = WorkflowV4.from_json(json)
# print the JSON string representation of the object
print(WorkflowV4.to_json())

# convert the object into a dict
workflow_v4_dict = workflow_v4_instance.to_dict()
# create an instance of WorkflowV4 from a dict
workflow_v4_from_dict = WorkflowV4.from_dict(workflow_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


