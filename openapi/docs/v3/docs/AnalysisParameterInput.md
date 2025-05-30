# AnalysisParameterInput

Supports multi-value parameters, only one of attributes 'value' or 'multiValue' must be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**value** | **str** | The value for single-value parameters. | [optional] 
**multi_value** | **List[Optional[str]]** | The values for multi-value parameters. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_parameter_input import AnalysisParameterInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisParameterInput from a JSON string
analysis_parameter_input_instance = AnalysisParameterInput.from_json(json)
# print the JSON string representation of the object
print(AnalysisParameterInput.to_json())

# convert the object into a dict
analysis_parameter_input_dict = analysis_parameter_input_instance.to_dict()
# create an instance of AnalysisParameterInput from a dict
analysis_parameter_input_from_dict = AnalysisParameterInput.from_dict(analysis_parameter_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


