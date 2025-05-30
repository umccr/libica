# InputFormGroupFieldValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[InputFormFieldValues]**](InputFormFieldValues.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_group_field_values import InputFormGroupFieldValues

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormGroupFieldValues from a JSON string
input_form_group_field_values_instance = InputFormGroupFieldValues.from_json(json)
# print the JSON string representation of the object
print(InputFormGroupFieldValues.to_json())

# convert the object into a dict
input_form_group_field_values_dict = input_form_group_field_values_instance.to_dict()
# create an instance of InputFormGroupFieldValues from a dict
input_form_group_field_values_from_dict = InputFormGroupFieldValues.from_dict(input_form_group_field_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


