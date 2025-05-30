# AnalysisInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The name of the input-parameter. | 
**analysis_data** | [**List[AnalysisData]**](AnalysisData.md) | The analysis-data used as input by the analysis. | [optional] 
**external_data** | [**List[AnalysisExternalData]**](AnalysisExternalData.md) | The external data used as input by the analysis. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_input import AnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisInput from a JSON string
analysis_input_instance = AnalysisInput.from_json(json)
# print the JSON string representation of the object
print(AnalysisInput.to_json())

# convert the object into a dict
analysis_input_dict = analysis_input_instance.to_dict()
# create an instance of AnalysisInput from a dict
analysis_input_from_dict = AnalysisInput.from_dict(analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


