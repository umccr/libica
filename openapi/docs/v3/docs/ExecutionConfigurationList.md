# ExecutionConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExecutionConfiguration]**](ExecutionConfiguration.md) |  | 

## Example

```python
from libica.openapi.v3.models.execution_configuration_list import ExecutionConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionConfigurationList from a JSON string
execution_configuration_list_instance = ExecutionConfigurationList.from_json(json)
# print the JSON string representation of the object
print(ExecutionConfigurationList.to_json())

# convert the object into a dict
execution_configuration_list_dict = execution_configuration_list_instance.to_dict()
# create an instance of ExecutionConfigurationList from a dict
execution_configuration_list_from_dict = ExecutionConfigurationList.from_dict(execution_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


