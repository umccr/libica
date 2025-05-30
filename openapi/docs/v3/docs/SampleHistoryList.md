# SampleHistoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SampleHistory]**](SampleHistory.md) |  | 

## Example

```python
from libica.openapi.v3.models.sample_history_list import SampleHistoryList

# TODO update the JSON string below
json = "{}"
# create an instance of SampleHistoryList from a JSON string
sample_history_list_instance = SampleHistoryList.from_json(json)
# print the JSON string representation of the object
print(SampleHistoryList.to_json())

# convert the object into a dict
sample_history_list_dict = sample_history_list_instance.to_dict()
# create an instance of SampleHistoryList from a dict
sample_history_list_from_dict = SampleHistoryList.from_dict(sample_history_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


