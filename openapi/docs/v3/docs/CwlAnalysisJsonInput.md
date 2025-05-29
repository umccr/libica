# CwlAnalysisJsonInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** |  | 
**input_json** | **str** | Contains the input JSON, as an escaped JSON String. | 
**data_ids** | **List[str]** |  | [optional] 
**mounts** | [**List[AnalysisInputDataMount]**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_json_input import CwlAnalysisJsonInput

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisJsonInput from a JSON string
cwl_analysis_json_input_instance = CwlAnalysisJsonInput.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisJsonInput.to_json())

# convert the object into a dict
cwl_analysis_json_input_dict = cwl_analysis_json_input_instance.to_dict()
# create an instance of CwlAnalysisJsonInput from a dict
cwl_analysis_json_input_from_dict = CwlAnalysisJsonInput.from_dict(cwl_analysis_json_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


