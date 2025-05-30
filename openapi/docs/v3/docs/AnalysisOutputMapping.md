# AnalysisOutputMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_path** | **str** |  | 
**type** | **str** |  | [optional] 
**target_project_id** | **str** |  | 
**target_path** | **str** |  | 
**action_on_exist** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_output_mapping import AnalysisOutputMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisOutputMapping from a JSON string
analysis_output_mapping_instance = AnalysisOutputMapping.from_json(json)
# print the JSON string representation of the object
print(AnalysisOutputMapping.to_json())

# convert the object into a dict
analysis_output_mapping_dict = analysis_output_mapping_instance.to_dict()
# create an instance of AnalysisOutputMapping from a dict
analysis_output_mapping_from_dict = AnalysisOutputMapping.from_dict(analysis_output_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


