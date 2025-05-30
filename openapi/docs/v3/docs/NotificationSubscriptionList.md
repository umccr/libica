# NotificationSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NotificationSubscription]**](NotificationSubscription.md) |  | 

## Example

```python
from libica.openapi.v3.models.notification_subscription_list import NotificationSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscriptionList from a JSON string
notification_subscription_list_instance = NotificationSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(NotificationSubscriptionList.to_json())

# convert the object into a dict
notification_subscription_list_dict = notification_subscription_list_instance.to_dict()
# create an instance of NotificationSubscriptionList from a dict
notification_subscription_list_from_dict = NotificationSubscriptionList.from_dict(notification_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


