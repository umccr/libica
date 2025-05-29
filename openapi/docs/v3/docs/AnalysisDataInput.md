# AnalysisDataInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_code** | **str** |  | 
**data_ids** | **List[str]** |  | [optional] 
**mounts** | [**List[AnalysisInputDataMount]**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_data_input import AnalysisDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisDataInput from a JSON string
analysis_data_input_instance = AnalysisDataInput.from_json(json)
# print the JSON string representation of the object
print(AnalysisDataInput.to_json())

# convert the object into a dict
analysis_data_input_dict = analysis_data_input_instance.to_dict()
# create an instance of AnalysisDataInput from a dict
analysis_data_input_from_dict = AnalysisDataInput.from_dict(analysis_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


