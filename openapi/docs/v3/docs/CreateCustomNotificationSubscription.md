# CreateCustomNotificationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_event_code** | **str** | The custom event code to subscribe to | 
**filter_expression** | **str** | To be used when a notification applies to specific conditions. | [optional] 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel_id** | **str** | The id of the notification channel used to send on | 

## Example

```python
from libica.openapi.v3.models.create_custom_notification_subscription import CreateCustomNotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomNotificationSubscription from a JSON string
create_custom_notification_subscription_instance = CreateCustomNotificationSubscription.from_json(json)
# print the JSON string representation of the object
print(CreateCustomNotificationSubscription.to_json())

# convert the object into a dict
create_custom_notification_subscription_dict = create_custom_notification_subscription_instance.to_dict()
# create an instance of CreateCustomNotificationSubscription from a dict
create_custom_notification_subscription_from_dict = CreateCustomNotificationSubscription.from_dict(create_custom_notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


