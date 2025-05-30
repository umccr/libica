# NotificationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**event_code** | **str** | The event code to subscribe to | 
**payload_version** | **str** | The version of the notification event payload in case multiple versions exist. For analysis events possible values are [V3,V4] | [optional] 
**filter_expression** | **str** | To be used when a notification applies to specific conditions. | [optional] 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel** | [**NotificationChannel**](NotificationChannel.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.notification_subscription import NotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscription from a JSON string
notification_subscription_instance = NotificationSubscription.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscription.to_json())

# convert the object into a dict
notification_subscription_dict = notification_subscription_instance.to_dict()
# create an instance of NotificationSubscription from a dict
notification_subscription_from_dict = NotificationSubscription.from_dict(notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


