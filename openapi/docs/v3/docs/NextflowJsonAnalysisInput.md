# NextflowJsonAnalysisInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[InputFormFieldValues]**](InputFormFieldValues.md) |  | [optional] 
**groups** | [**List[InputFormGroup]**](InputFormGroup.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.nextflow_json_analysis_input import NextflowJsonAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of NextflowJsonAnalysisInput from a JSON string
nextflow_json_analysis_input_instance = NextflowJsonAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(NextflowJsonAnalysisInput.to_json())

# convert the object into a dict
nextflow_json_analysis_input_dict = nextflow_json_analysis_input_instance.to_dict()
# create an instance of NextflowJsonAnalysisInput from a dict
nextflow_json_analysis_input_from_dict = NextflowJsonAnalysisInput.from_dict(nextflow_json_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


