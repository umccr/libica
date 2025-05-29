# AnalysisUsageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**AnalysisPrice**](AnalysisPrice.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_usage_details import AnalysisUsageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisUsageDetails from a JSON string
analysis_usage_details_instance = AnalysisUsageDetails.from_json(json)
# print the JSON string representation of the object
print(AnalysisUsageDetails.to_json())

# convert the object into a dict
analysis_usage_details_dict = analysis_usage_details_instance.to_dict()
# create an instance of AnalysisUsageDetails from a dict
analysis_usage_details_from_dict = AnalysisUsageDetails.from_dict(analysis_usage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


