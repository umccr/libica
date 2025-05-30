# EventLogV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** | The code of the event | 
**description** | **str** | The details of the event | 
**event_type_category** | **str** | The type of the event | 
**user_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.event_log_v3 import EventLogV3

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogV3 from a JSON string
event_log_v3_instance = EventLogV3.from_json(json)
# print the JSON string representation of the object
print(EventLogV3.to_json())

# convert the object into a dict
event_log_v3_dict = event_log_v3_instance.to_dict()
# create an instance of EventLogV3 from a dict
event_log_v3_from_dict = EventLogV3.from_dict(event_log_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


