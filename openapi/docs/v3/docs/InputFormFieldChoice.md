# InputFormFieldChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**selected** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_field_choice import InputFormFieldChoice

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormFieldChoice from a JSON string
input_form_field_choice_instance = InputFormFieldChoice.from_json(json)
# print the JSON string representation of the object
print(InputFormFieldChoice.to_json())

# convert the object into a dict
input_form_field_choice_dict = input_form_field_choice_instance.to_dict()
# create an instance of InputFormFieldChoice from a dict
input_form_field_choice_from_dict = InputFormFieldChoice.from_dict(input_form_field_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


