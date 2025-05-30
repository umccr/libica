# AnalysisQueryParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference to filter on. | [optional] 
**user_reference** | **str** | The user-reference to filter on. | [optional] 
**status** | **List[Optional[str]]** |  | [optional] 
**user_tags** | **List[Optional[str]]** | The user-tags to filter on. | [optional] 
**technical_tags** | **List[Optional[str]]** | The technical-tags to filter on. | [optional] 
**reference_tags** | **List[Optional[str]]** | The reference-data-tags to filter on. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_query_parameters import AnalysisQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryParameters from a JSON string
analysis_query_parameters_instance = AnalysisQueryParameters.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryParameters.to_json())

# convert the object into a dict
analysis_query_parameters_dict = analysis_query_parameters_instance.to_dict()
# create an instance of AnalysisQueryParameters from a dict
analysis_query_parameters_from_dict = AnalysisQueryParameters.from_dict(analysis_query_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


