# StorageConfigurationWithDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** | The name of the storage configuration | 
**status** | **str** |  | 
**region** | [**Region**](Region.md) |  | 
**is_default** | **bool** | An indication if this is the default in region for new projects | 
**storage_configuration_details** | [**StorageConfigurationDetails**](StorageConfigurationDetails.md) |  | 
**type** | **str** |  | defaults to "AWS_S3"
**tenant_name** | **str, none_type** |  | [optional] 
**description** | **str, none_type** | An optional description | [optional] 
**error_message** | **str, none_type** | An optional error message when something went wrong with the configuration | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


