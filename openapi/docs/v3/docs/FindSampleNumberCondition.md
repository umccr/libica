# FindSampleNumberCondition

Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**FieldId**](FieldId.md) |  | [optional] 
**var_field** | **str** |  | [optional] 
**lower_bound** | **str** |  | [optional] 
**upper_bound** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.find_sample_number_condition import FindSampleNumberCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FindSampleNumberCondition from a JSON string
find_sample_number_condition_instance = FindSampleNumberCondition.from_json(json)
# print the JSON string representation of the object
print(FindSampleNumberCondition.to_json())

# convert the object into a dict
find_sample_number_condition_dict = find_sample_number_condition_instance.to_dict()
# create an instance of FindSampleNumberCondition from a dict
find_sample_number_condition_from_dict = FindSampleNumberCondition.from_dict(find_sample_number_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


