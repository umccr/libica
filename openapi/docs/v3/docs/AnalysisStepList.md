# AnalysisStepList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisStep]**](AnalysisStep.md) |  | 

## Example

```python
from libica.openapi.v3.models.analysis_step_list import AnalysisStepList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStepList from a JSON string
analysis_step_list_instance = AnalysisStepList.from_json(json)
# print the JSON string representation of the object
print(AnalysisStepList.to_json())

# convert the object into a dict
analysis_step_list_dict = analysis_step_list_instance.to_dict()
# create an instance of AnalysisStepList from a dict
analysis_step_list_from_dict = AnalysisStepList.from_dict(analysis_step_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


