# AnalysisReferenceDataParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_code** | **str** |  | [optional] 
**reference_data_id** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_reference_data_parameter import AnalysisReferenceDataParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReferenceDataParameter from a JSON string
analysis_reference_data_parameter_instance = AnalysisReferenceDataParameter.from_json(json)
# print the JSON string representation of the object
print(AnalysisReferenceDataParameter.to_json())

# convert the object into a dict
analysis_reference_data_parameter_dict = analysis_reference_data_parameter_instance.to_dict()
# create an instance of AnalysisReferenceDataParameter from a dict
analysis_reference_data_parameter_from_dict = AnalysisReferenceDataParameter.from_dict(analysis_reference_data_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


