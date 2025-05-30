# WorkflowSessionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | 
**multi_value** | **bool** | Whether the configuration has multiple values | 
**values** | **List[str]** | The configuration values | 

## Example

```python
from libica.openapi.v3.models.workflow_session_configuration import WorkflowSessionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionConfiguration from a JSON string
workflow_session_configuration_instance = WorkflowSessionConfiguration.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionConfiguration.to_json())

# convert the object into a dict
workflow_session_configuration_dict = workflow_session_configuration_instance.to_dict()
# create an instance of WorkflowSessionConfiguration from a dict
workflow_session_configuration_from_dict = WorkflowSessionConfiguration.from_dict(workflow_session_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


