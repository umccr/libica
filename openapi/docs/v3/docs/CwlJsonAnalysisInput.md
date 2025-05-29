# CwlJsonAnalysisInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[InputFormFieldValues]**](InputFormFieldValues.md) |  | [optional] 
**groups** | [**List[InputFormGroup]**](InputFormGroup.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_json_analysis_input import CwlJsonAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of CwlJsonAnalysisInput from a JSON string
cwl_json_analysis_input_instance = CwlJsonAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(CwlJsonAnalysisInput.to_json())

# convert the object into a dict
cwl_json_analysis_input_dict = cwl_json_analysis_input_instance.to_dict()
# create an instance of CwlJsonAnalysisInput from a dict
cwl_json_analysis_input_from_dict = CwlJsonAnalysisInput.from_dict(cwl_json_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


