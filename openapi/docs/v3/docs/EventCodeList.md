# EventCodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventCode]**](EventCode.md) |  | 

## Example

```python
from libica.openapi.v3.models.event_code_list import EventCodeList

# TODO update the JSON string below
json = "{}"
# create an instance of EventCodeList from a JSON string
event_code_list_instance = EventCodeList.from_json(json)
# print the JSON string representation of the object
print(EventCodeList.to_json())

# convert the object into a dict
event_code_list_dict = event_code_list_instance.to_dict()
# create an instance of EventCodeList from a dict
event_code_list_from_dict = EventCodeList.from_dict(event_code_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


