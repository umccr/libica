# AnalysisOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The name of the output-parameter. | 
**project_id** | **str** | The ID of the project containing the analysis-data produced by the analysis for the output-parameter. | [optional] 
**data** | [**List[AnalysisData]**](AnalysisData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_output import AnalysisOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisOutput from a JSON string
analysis_output_instance = AnalysisOutput.from_json(json)
# print the JSON string representation of the object
print(AnalysisOutput.to_json())

# convert the object into a dict
analysis_output_dict = analysis_output_instance.to_dict()
# create an instance of AnalysisOutput from a dict
analysis_output_from_dict = AnalysisOutput.from_dict(analysis_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


