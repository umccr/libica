# FindSampleNumberCondition

Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**FieldId**](FieldId.md) |  | [optional] 
**field** | **str, none_type** |  | [optional] 
**lower_bound** | **str, none_type** |  | [optional] 
**upper_bound** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


