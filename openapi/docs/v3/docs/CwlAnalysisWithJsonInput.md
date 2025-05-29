# CwlAnalysisWithJsonInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_json** | **str** | Contains the input JSON, as an escaped JSON String. | 
**data_ids** | **List[str]** |  | [optional] 
**mounts** | [**List[AnalysisInputDataMount]**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_with_json_input import CwlAnalysisWithJsonInput

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisWithJsonInput from a JSON string
cwl_analysis_with_json_input_instance = CwlAnalysisWithJsonInput.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisWithJsonInput.to_json())

# convert the object into a dict
cwl_analysis_with_json_input_dict = cwl_analysis_with_json_input_instance.to_dict()
# create an instance of CwlAnalysisWithJsonInput from a dict
cwl_analysis_with_json_input_from_dict = CwlAnalysisWithJsonInput.from_dict(cwl_analysis_with_json_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


