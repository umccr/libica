# PipelineConfigurationParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the parameter | 
**required** | **bool** | Indicates whether this parameter is required | 
**multi_value** | **bool** | Indicates whether multiple values are allowed for this parameter | 
**type** | **str** | The type for each parameter | 
**settings** | [**Settings**](Settings.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_configuration_parameter import PipelineConfigurationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineConfigurationParameter from a JSON string
pipeline_configuration_parameter_instance = PipelineConfigurationParameter.from_json(json)
# print the JSON string representation of the object
print(PipelineConfigurationParameter.to_json())

# convert the object into a dict
pipeline_configuration_parameter_dict = pipeline_configuration_parameter_instance.to_dict()
# create an instance of PipelineConfigurationParameter from a dict
pipeline_configuration_parameter_from_dict = PipelineConfigurationParameter.from_dict(pipeline_configuration_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


