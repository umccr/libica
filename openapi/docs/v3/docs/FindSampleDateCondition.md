# FindSampleDateCondition

Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_field** | [**FieldId**](FieldId.md) |  | [optional] 
**var_field** | **str** |  | [optional] 
**before_date** | **str** | Before date. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
**after_date** | **str** | After date. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 

## Example

```python
from libica.openapi.v3.models.find_sample_date_condition import FindSampleDateCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FindSampleDateCondition from a JSON string
find_sample_date_condition_instance = FindSampleDateCondition.from_json(json)
# print the JSON string representation of the object
print(FindSampleDateCondition.to_json())

# convert the object into a dict
find_sample_date_condition_dict = find_sample_date_condition_instance.to_dict()
# create an instance of FindSampleDateCondition from a dict
find_sample_date_condition_from_dict = FindSampleDateCondition.from_dict(find_sample_date_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


