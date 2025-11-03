# DataUpdateGroup

Updates to apply.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ids** | **[str]** |  | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**will_be_archived_at** | **datetime** | The timestamp when the data should be archived. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
**will_be_deleted_at** | **datetime** | The timestamp when the data should be deleted. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
**clear_will_be_archived_at** | **bool, none_type** | Boolean to indicate that the willBeArchivedAt value should be cleared. | [optional]  if omitted the server will use the default value of False
**clear_will_be_deleted_at** | **bool, none_type** | Boolean to indicate that the willBeDeletedAt value should be cleared. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


