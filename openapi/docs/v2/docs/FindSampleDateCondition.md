# FindSampleDateCondition

Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**FieldId**](FieldId.md) |  | [optional] 
**field** | **str, none_type** |  | [optional] 
**before_date** | **str, none_type** | Before date. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
**after_date** | **str, none_type** | After date. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


