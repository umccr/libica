# ProjectDataUpdateBatchItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | Data to apply the update to (recursively, if it&#39;s a folder). | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**will_be_archived_at** | **datetime** | The timestamp when the data should be archived. | [optional] 
**will_be_deleted_at** | **datetime** | The timestamp when the data should be deleted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


