# ExecutionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | 
**multi_value** | **bool** | Whether the configuration has multiple values | 
**values** | **List[str]** | The configuration values | 

## Example

```python
from libica.openapi.v3.models.execution_configuration import ExecutionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionConfiguration from a JSON string
execution_configuration_instance = ExecutionConfiguration.from_json(json)
# print the JSON string representation of the object
print(ExecutionConfiguration.to_json())

# convert the object into a dict
execution_configuration_dict = execution_configuration_instance.to_dict()
# create an instance of ExecutionConfiguration from a dict
execution_configuration_from_dict = ExecutionConfiguration.from_dict(execution_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


