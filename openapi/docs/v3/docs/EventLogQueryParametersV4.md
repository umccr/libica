# EventLogQueryParametersV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code to filter on. | [optional] 
**category** | **str** | The category to filter on | [optional] 
**date_from** | **datetime** | The date from to search in. | [optional] 
**date_until** | **datetime** | The date until to search in. | [optional] 

## Example

```python
from libica.openapi.v3.models.event_log_query_parameters_v4 import EventLogQueryParametersV4

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogQueryParametersV4 from a JSON string
event_log_query_parameters_v4_instance = EventLogQueryParametersV4.from_json(json)
# print the JSON string representation of the object
print(EventLogQueryParametersV4.to_json())

# convert the object into a dict
event_log_query_parameters_v4_dict = event_log_query_parameters_v4_instance.to_dict()
# create an instance of EventLogQueryParametersV4 from a dict
event_log_query_parameters_v4_from_dict = EventLogQueryParametersV4.from_dict(event_log_query_parameters_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


