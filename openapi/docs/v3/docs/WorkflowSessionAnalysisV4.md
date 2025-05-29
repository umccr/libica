# WorkflowSessionAnalysisV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**AnalysisV4**](AnalysisV4.md) |  | 
**project** | [**Project**](Project.md) |  | 
**workflow_session_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.workflow_session_analysis_v4 import WorkflowSessionAnalysisV4

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionAnalysisV4 from a JSON string
workflow_session_analysis_v4_instance = WorkflowSessionAnalysisV4.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionAnalysisV4.to_json())

# convert the object into a dict
workflow_session_analysis_v4_dict = workflow_session_analysis_v4_instance.to_dict()
# create an instance of WorkflowSessionAnalysisV4 from a dict
workflow_session_analysis_v4_from_dict = WorkflowSessionAnalysisV4.from_dict(workflow_session_analysis_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


