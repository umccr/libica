# CwlAnalysisInput

This object contains a \"oneOf\" construct. With the \"objectType\" attribute you can specify which object type you want to provide. Use \"STRUCTURED\" for type \"CreateAnalysisStructuredInput\" or use \"JSON\" for type \"CreateAnalysisJsonInput\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** |  | 
**inputs** | [**List[AnalysisDataInput]**](AnalysisDataInput.md) |  | 
**parameters** | [**List[AnalysisParameterInput]**](AnalysisParameterInput.md) |  | [optional] 
**reference_data_parameters** | [**List[AnalysisReferenceDataParameter]**](AnalysisReferenceDataParameter.md) |  | [optional] 
**input_json** | **str** | Contains the input JSON, as an escaped JSON String. | 
**data_ids** | **List[str]** |  | [optional] 
**mounts** | [**List[AnalysisInputDataMount]**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_input import CwlAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisInput from a JSON string
cwl_analysis_input_instance = CwlAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisInput.to_json())

# convert the object into a dict
cwl_analysis_input_dict = cwl_analysis_input_instance.to_dict()
# create an instance of CwlAnalysisInput from a dict
cwl_analysis_input_from_dict = CwlAnalysisInput.from_dict(cwl_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


