# NextflowAnalysisWithCustomInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_input** | **str** | Contains the custom input, in YAML format or as an escaped JSON string. | 
**data_ids** | **List[str]** |  | [optional] 
**mounts** | [**List[AnalysisInputDataMount]**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.nextflow_analysis_with_custom_input import NextflowAnalysisWithCustomInput

# TODO update the JSON string below
json = "{}"
# create an instance of NextflowAnalysisWithCustomInput from a JSON string
nextflow_analysis_with_custom_input_instance = NextflowAnalysisWithCustomInput.from_json(json)
# print the JSON string representation of the object
print(NextflowAnalysisWithCustomInput.to_json())

# convert the object into a dict
nextflow_analysis_with_custom_input_dict = nextflow_analysis_with_custom_input_instance.to_dict()
# create an instance of NextflowAnalysisWithCustomInput from a dict
nextflow_analysis_with_custom_input_from_dict = NextflowAnalysisWithCustomInput.from_dict(nextflow_analysis_with_custom_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


