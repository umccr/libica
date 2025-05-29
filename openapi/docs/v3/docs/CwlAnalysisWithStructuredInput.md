# CwlAnalysisWithStructuredInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[AnalysisDataInput]**](AnalysisDataInput.md) |  | 
**parameters** | [**List[AnalysisParameterInput]**](AnalysisParameterInput.md) |  | [optional] 
**reference_data_parameters** | [**List[AnalysisReferenceDataParameter]**](AnalysisReferenceDataParameter.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_with_structured_input import CwlAnalysisWithStructuredInput

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisWithStructuredInput from a JSON string
cwl_analysis_with_structured_input_instance = CwlAnalysisWithStructuredInput.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisWithStructuredInput.to_json())

# convert the object into a dict
cwl_analysis_with_structured_input_dict = cwl_analysis_with_structured_input_instance.to_dict()
# create an instance of CwlAnalysisWithStructuredInput from a dict
cwl_analysis_with_structured_input_from_dict = CwlAnalysisWithStructuredInput.from_dict(cwl_analysis_with_structured_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


