# CustomNotificationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**custom_event_code** | **str** | The custom event code to subscribe to | 
**filter_expression** | **str** | To be used when a notification applies to specific conditions. | [optional] 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel** | [**NotificationChannel**](NotificationChannel.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.custom_notification_subscription import CustomNotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotificationSubscription from a JSON string
custom_notification_subscription_instance = CustomNotificationSubscription.from_json(json)
# print the JSON string representation of the object
print(CustomNotificationSubscription.to_json())

# convert the object into a dict
custom_notification_subscription_dict = custom_notification_subscription_instance.to_dict()
# create an instance of CustomNotificationSubscription from a dict
custom_notification_subscription_from_dict = CustomNotificationSubscription.from_dict(custom_notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


