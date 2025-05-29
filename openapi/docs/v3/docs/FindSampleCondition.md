# FindSampleCondition

Adds a condition on a string field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**FieldId**](FieldId.md) |  | [optional] 
**var_field** | **str** |  | [optional] 
**match_mode** | **str** | Defines how the value will be matched. | [optional] 
**values** | **List[str]** |  | 

## Example

```python
from libica.openapi.v3.models.find_sample_condition import FindSampleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FindSampleCondition from a JSON string
find_sample_condition_instance = FindSampleCondition.from_json(json)
# print the JSON string representation of the object
print(FindSampleCondition.to_json())

# convert the object into a dict
find_sample_condition_dict = find_sample_condition_instance.to_dict()
# create an instance of FindSampleCondition from a dict
find_sample_condition_from_dict = FindSampleCondition.from_dict(find_sample_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


