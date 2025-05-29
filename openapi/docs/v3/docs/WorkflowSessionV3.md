# WorkflowSessionV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**user_reference** | **str** | The user reference of the workflow session | 
**workflow** | [**WorkflowV3**](WorkflowV3.md) |  | 
**status** | **str** | The status of the workflow session | 
**start_date** | **datetime** | When the workflow session was started | [optional] 
**end_date** | **datetime** | When the workflow session was finished | [optional] 
**summary** | **str** | The summary of the workflow session | [optional] 
**tags** | [**WorkflowSessionTag**](WorkflowSessionTag.md) |  | 

## Example

```python
from libica.openapi.v3.models.workflow_session_v3 import WorkflowSessionV3

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionV3 from a JSON string
workflow_session_v3_instance = WorkflowSessionV3.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionV3.to_json())

# convert the object into a dict
workflow_session_v3_dict = workflow_session_v3_instance.to_dict()
# create an instance of WorkflowSessionV3 from a dict
workflow_session_v3_from_dict = WorkflowSessionV3.from_dict(workflow_session_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


