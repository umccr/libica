# InputFormFieldList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InputFormField]**](InputFormField.md) |  | 

## Example

```python
from libica.openapi.v3.models.input_form_field_list import InputFormFieldList

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormFieldList from a JSON string
input_form_field_list_instance = InputFormFieldList.from_json(json)
# print the JSON string representation of the object
print(InputFormFieldList.to_json())

# convert the object into a dict
input_form_field_list_dict = input_form_field_list_instance.to_dict()
# create an instance of InputFormFieldList from a dict
input_form_field_list_from_dict = InputFormFieldList.from_dict(input_form_field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


