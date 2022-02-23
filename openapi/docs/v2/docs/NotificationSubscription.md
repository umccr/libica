# NotificationSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**event_code** | **str** | The event code to subscribe to | 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel** | [**NotificationChannel**](NotificationChannel.md) |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**filter_expression** | **str, none_type** | To be used when a notification applies to specific conditions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


