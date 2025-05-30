# FindProjectSamples


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[FindSampleCondition]**](FindSampleCondition.md) | Adds a condition on a string field. | 
**date_conditions** | [**List[FindSampleDateCondition]**](FindSampleDateCondition.md) | Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field. | 
**number_conditions** | [**List[FindSampleNumberCondition]**](FindSampleNumberCondition.md) | Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field. | 
**boolean_conditions** | [**List[FindSampleBooleanCondition]**](FindSampleBooleanCondition.md) | Adds a condition on a boolean field. | 
**full_text_search_string** | **str** | Adds a fuzzy matching condition for the text on all string fields of the sample i.e. on both the fixed fields (name, description) as any metadata text field. | [optional] 
**include_deleted** | **bool** | Indicates whether deleted samples should be included. | [optional] [default to False]
**user_tags** | **List[Optional[str]]** | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional] 
**user_tag_match_mode** | **str** | How the usertags are filtered. | [optional] 
**run_input_tags** | **List[Optional[str]]** | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional] 
**run_input_tag_match_mode** | **str** | How the runInputTags are filtered. | [optional] 
**connector_tags** | **List[Optional[str]]** | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional] 
**connector_tag_match_mode** | **str** | How the connectorTags are filtered. | [optional] 
**tech_tags** | **List[Optional[str]]** | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional] 
**tech_tag_match_mode** | **str** | How the technicalTags are filtered. | [optional] 
**instrument_run_ids** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.find_project_samples import FindProjectSamples

# TODO update the JSON string below
json = "{}"
# create an instance of FindProjectSamples from a JSON string
find_project_samples_instance = FindProjectSamples.from_json(json)
# print the JSON string representation of the object
print(FindProjectSamples.to_json())

# convert the object into a dict
find_project_samples_dict = find_project_samples_instance.to_dict()
# create an instance of FindProjectSamples from a dict
find_project_samples_from_dict = FindProjectSamples.from_dict(find_project_samples_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


