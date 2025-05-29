# WorkflowSessionInputList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkflowSessionInput]**](WorkflowSessionInput.md) |  | 

## Example

```python
from libica.openapi.v3.models.workflow_session_input_list import WorkflowSessionInputList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionInputList from a JSON string
workflow_session_input_list_instance = WorkflowSessionInputList.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionInputList.to_json())

# convert the object into a dict
workflow_session_input_list_dict = workflow_session_input_list_instance.to_dict()
# create an instance of WorkflowSessionInputList from a dict
workflow_session_input_list_from_dict = WorkflowSessionInputList.from_dict(workflow_session_input_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


