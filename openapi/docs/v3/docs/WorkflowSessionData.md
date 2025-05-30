# WorkflowSessionData

The workflow-session-data used as input by the workflow session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | The id of the file/folder. | 
**format** | [**DataFormat**](DataFormat.md) |  | 
**name** | **str** | The name of the file/folder as it was processed by the workflow session. | 
**data_type** | **str** |  | 
**mount_path** | **str** | The requested location where the input file was located on the machine that was running the workflow. | [optional] 

## Example

```python
from libica.openapi.v3.models.workflow_session_data import WorkflowSessionData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionData from a JSON string
workflow_session_data_instance = WorkflowSessionData.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionData.to_json())

# convert the object into a dict
workflow_session_data_dict = workflow_session_data_instance.to_dict()
# create an instance of WorkflowSessionData from a dict
workflow_session_data_from_dict = WorkflowSessionData.from_dict(workflow_session_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


