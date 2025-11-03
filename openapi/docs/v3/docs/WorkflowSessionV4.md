# WorkflowSessionV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**user_reference** | **str** | The user reference of the workflow session | 
**workflow** | [**WorkflowV4**](WorkflowV4.md) |  | 
**status** | **str** | The status of the workflow session | 
**start_date** | **datetime** | When the workflow session was started | [optional] 
**end_date** | **datetime** | When the workflow session was finished | [optional] 
**summary** | **str** | The summary of the workflow session | [optional] 
**tags** | [**WorkflowSessionTag**](WorkflowSessionTag.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.workflow_session_v4 import WorkflowSessionV4

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionV4 from a JSON string
workflow_session_v4_instance = WorkflowSessionV4.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionV4.to_json())

# convert the object into a dict
workflow_session_v4_dict = workflow_session_v4_instance.to_dict()
# create an instance of WorkflowSessionV4 from a dict
workflow_session_v4_from_dict = WorkflowSessionV4.from_dict(workflow_session_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


