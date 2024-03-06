# CreateNotificationSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_code** | **str** | The event code to subscribe to | 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel_id** | **str** | The ID of the notification channel used to send on | 
**payload_version** | **str, none_type** | The version of the notification event payload in case multiple versions exist. For analysis events possible values are [V3,V4] | [optional] 
**filter_expression** | **str, none_type** | To be used when a notification applies to specific conditions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


