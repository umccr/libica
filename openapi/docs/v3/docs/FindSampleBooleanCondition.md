# FindSampleBooleanCondition

Adds a condition on a boolean field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**ModelField**](ModelField.md) |  | [optional] 
**var_field** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.find_sample_boolean_condition import FindSampleBooleanCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FindSampleBooleanCondition from a JSON string
find_sample_boolean_condition_instance = FindSampleBooleanCondition.from_json(json)
# print the JSON string representation of the object
print(FindSampleBooleanCondition.to_json())

# convert the object into a dict
find_sample_boolean_condition_dict = find_sample_boolean_condition_instance.to_dict()
# create an instance of FindSampleBooleanCondition from a dict
find_sample_boolean_condition_from_dict = FindSampleBooleanCondition.from_dict(find_sample_boolean_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


