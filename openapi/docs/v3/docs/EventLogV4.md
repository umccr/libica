# EventLogV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**code** | **str** | The code of the event | 
**description** | **str** | The details of the event | 
**event_type_category** | **str** | The type of the event | 

## Example

```python
from libica.openapi.v3.models.event_log_v4 import EventLogV4

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogV4 from a JSON string
event_log_v4_instance = EventLogV4.from_json(json)
# print the JSON string representation of the object
print(EventLogV4.to_json())

# convert the object into a dict
event_log_v4_dict = event_log_v4_instance.to_dict()
# create an instance of EventLogV4 from a dict
event_log_v4_from_dict = EventLogV4.from_dict(event_log_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


