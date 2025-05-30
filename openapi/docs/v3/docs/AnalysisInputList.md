# AnalysisInputList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisInput]**](AnalysisInput.md) |  | 

## Example

```python
from libica.openapi.v3.models.analysis_input_list import AnalysisInputList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisInputList from a JSON string
analysis_input_list_instance = AnalysisInputList.from_json(json)
# print the JSON string representation of the object
print(AnalysisInputList.to_json())

# convert the object into a dict
analysis_input_list_dict = analysis_input_list_instance.to_dict()
# create an instance of AnalysisInputList from a dict
analysis_input_list_from_dict = AnalysisInputList.from_dict(analysis_input_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


