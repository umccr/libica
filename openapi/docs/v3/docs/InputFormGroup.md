# InputFormGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**values** | [**List[InputFormGroupFieldValues]**](InputFormGroupFieldValues.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_group import InputFormGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormGroup from a JSON string
input_form_group_instance = InputFormGroup.from_json(json)
# print the JSON string representation of the object
print(InputFormGroup.to_json())

# convert the object into a dict
input_form_group_dict = input_form_group_instance.to_dict()
# create an instance of InputFormGroup from a dict
input_form_group_from_dict = InputFormGroup.from_dict(input_form_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


