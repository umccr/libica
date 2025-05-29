# EventLogListV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventLogV3]**](EventLogV3.md) |  | 

## Example

```python
from libica.openapi.v3.models.event_log_list_v3 import EventLogListV3

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogListV3 from a JSON string
event_log_list_v3_instance = EventLogListV3.from_json(json)
# print the JSON string representation of the object
print(EventLogListV3.to_json())

# convert the object into a dict
event_log_list_v3_dict = event_log_list_v3_instance.to_dict()
# create an instance of EventLogListV3 from a dict
event_log_list_v3_from_dict = EventLogListV3.from_dict(event_log_list_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


