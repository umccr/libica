# SampleHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurred_at** | **datetime** | When the change was made | 
**user** | **str** | The user that made the change | [optional] 
**run** | **str** | In which execution context the change was made | [optional] 
**source** | **str** | In which context the change was made | 
**text** | **str** | What was changed | 
**project** | **str** | In which project context the change was made | [optional] 
**model** | **int** | In which model context the change was made | [optional] 

## Example

```python
from libica.openapi.v3.models.sample_history import SampleHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SampleHistory from a JSON string
sample_history_instance = SampleHistory.from_json(json)
# print the JSON string representation of the object
print(SampleHistory.to_json())

# convert the object into a dict
sample_history_dict = sample_history_instance.to_dict()
# create an instance of SampleHistory from a dict
sample_history_from_dict = SampleHistory.from_dict(sample_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


