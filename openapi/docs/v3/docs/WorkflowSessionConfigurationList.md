# WorkflowSessionConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkflowSessionConfiguration]**](WorkflowSessionConfiguration.md) |  | 

## Example

```python
from libica.openapi.v3.models.workflow_session_configuration_list import WorkflowSessionConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionConfigurationList from a JSON string
workflow_session_configuration_list_instance = WorkflowSessionConfigurationList.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionConfigurationList.to_json())

# convert the object into a dict
workflow_session_configuration_list_dict = workflow_session_configuration_list_instance.to_dict()
# create an instance of WorkflowSessionConfigurationList from a dict
workflow_session_configuration_list_from_dict = WorkflowSessionConfigurationList.from_dict(workflow_session_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


