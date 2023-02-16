# FindProjectSamples


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[FindSampleCondition]**](FindSampleCondition.md) | Adds a condition on a string field. | 
**date_conditions** | [**[FindSampleDateCondition]**](FindSampleDateCondition.md) | Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field. | 
**number_conditions** | [**[FindSampleNumberCondition]**](FindSampleNumberCondition.md) | Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field. | 
**boolean_conditions** | [**[FindSampleBooleanCondition]**](FindSampleBooleanCondition.md) | Adds a condition on a boolean field. | 
**full_text_search_string** | **str, none_type** | Adds a fuzzy matching condition for the text on all string fields of the sample i.e. on both the fixed fields (name, description) as any metadata text field. | [optional] 
**include_deleted** | **bool, none_type** | Indicates whether deleted samples should be included. | [optional]  if omitted the server will use the default value of False
**user_tags** | **[str, none_type], none_type** | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional] 
**user_tag_match_mode** | **str, none_type** | How the usertags are filtered. | [optional] 
**run_input_tags** | **[str, none_type], none_type** | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional] 
**run_input_tag_match_mode** | **str, none_type** | How the runInputTags are filtered. | [optional] 
**connector_tags** | **[str, none_type], none_type** | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional] 
**connector_tag_match_mode** | **str, none_type** | How the connectorTags are filtered. | [optional] 
**tech_tags** | **[str, none_type], none_type** | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional] 
**tech_tag_match_mode** | **str, none_type** | How the technicalTags are filtered. | [optional] 
**instrument_run_ids** | **[str, none_type], none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


