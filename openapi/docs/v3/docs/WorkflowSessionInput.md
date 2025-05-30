# WorkflowSessionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The name of the input-parameter. | 
**analysis_data** | [**List[WorkflowSessionData]**](WorkflowSessionData.md) | The workflow-session-data used as input by the workflow session. | [optional] 
**external_data** | [**List[WorkflowSessionExternalData]**](WorkflowSessionExternalData.md) | The external data used as input by the workflow session. | [optional] 

## Example

```python
from libica.openapi.v3.models.workflow_session_input import WorkflowSessionInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionInput from a JSON string
workflow_session_input_instance = WorkflowSessionInput.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionInput.to_json())

# convert the object into a dict
workflow_session_input_dict = workflow_session_input_instance.to_dict()
# create an instance of WorkflowSessionInput from a dict
workflow_session_input_from_dict = WorkflowSessionInput.from_dict(workflow_session_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


