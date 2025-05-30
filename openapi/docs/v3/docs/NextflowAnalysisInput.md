# NextflowAnalysisInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[AnalysisDataInput]**](AnalysisDataInput.md) |  | 
**parameters** | [**List[AnalysisParameterInput]**](AnalysisParameterInput.md) |  | [optional] 
**reference_data_parameters** | [**List[AnalysisReferenceDataParameter]**](AnalysisReferenceDataParameter.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.nextflow_analysis_input import NextflowAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of NextflowAnalysisInput from a JSON string
nextflow_analysis_input_instance = NextflowAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(NextflowAnalysisInput.to_json())

# convert the object into a dict
nextflow_analysis_input_dict = nextflow_analysis_input_instance.to_dict()
# create an instance of NextflowAnalysisInput from a dict
nextflow_analysis_input_from_dict = NextflowAnalysisInput.from_dict(nextflow_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


