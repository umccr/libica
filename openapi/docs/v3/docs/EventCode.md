# EventCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_code** | **str** | The event code that can be used for creating event subscriptions | 
**description** | **str** | A short description about the event code | 

## Example

```python
from libica.openapi.v3.models.event_code import EventCode

# TODO update the JSON string below
json = "{}"
# create an instance of EventCode from a JSON string
event_code_instance = EventCode.from_json(json)
# print the JSON string representation of the object
print(EventCode.to_json())

# convert the object into a dict
event_code_dict = event_code_instance.to_dict()
# create an instance of EventCode from a dict
event_code_from_dict = EventCode.from_dict(event_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


