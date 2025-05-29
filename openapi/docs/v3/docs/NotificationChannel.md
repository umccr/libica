# NotificationChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**enabled** | **bool** | Should this channel be enabled or not? | 
**type** | **str** | The type of delivery target (MAIL, SQS, SNS, HTTP, ...) | 
**address** | **str** | The address where to send a notification to (email address, url, ...) | 
**aws_region** | **str** | The AWS region of the SNS notification channel | [optional] 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.notification_channel import NotificationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannel from a JSON string
notification_channel_instance = NotificationChannel.from_json(json)
# print the JSON string representation of the object
print(NotificationChannel.to_json())

# convert the object into a dict
notification_channel_dict = notification_channel_instance.to_dict()
# create an instance of NotificationChannel from a dict
notification_channel_from_dict = NotificationChannel.from_dict(notification_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


