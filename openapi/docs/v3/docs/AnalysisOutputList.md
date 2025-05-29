# AnalysisOutputList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisOutput]**](AnalysisOutput.md) |  | 

## Example

```python
from libica.openapi.v3.models.analysis_output_list import AnalysisOutputList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisOutputList from a JSON string
analysis_output_list_instance = AnalysisOutputList.from_json(json)
# print the JSON string representation of the object
print(AnalysisOutputList.to_json())

# convert the object into a dict
analysis_output_list_dict = analysis_output_list_instance.to_dict()
# create an instance of AnalysisOutputList from a dict
analysis_output_list_from_dict = AnalysisOutputList.from_dict(analysis_output_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


