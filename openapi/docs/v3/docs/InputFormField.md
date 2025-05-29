# InputFormField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**min_max_values_message** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**place_holder_text** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 
**data_values** | [**List[InputFormWithExternalData]**](InputFormWithExternalData.md) |  | [optional] 
**group_values** | [**List[InputFormGroupFieldValues]**](InputFormGroupFieldValues.md) |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**choices** | [**List[InputFormFieldChoice]**](InputFormFieldChoice.md) |  | [optional] 
**fields** | [**List[InputFormGroupField]**](InputFormGroupField.md) |  | [optional] 
**data_filter** | [**InputFormFieldDataFilter**](InputFormFieldDataFilter.md) |  | [optional] 
**regex** | **str** |  | [optional] 
**regex_error_message** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**empty_values_allowed** | **bool** |  | [optional] 
**update_render_on_change** | **bool** |  | [optional] 
**sensitive** | **bool** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_field import InputFormField

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormField from a JSON string
input_form_field_instance = InputFormField.from_json(json)
# print the JSON string representation of the object
print(InputFormField.to_json())

# convert the object into a dict
input_form_field_dict = input_form_field_instance.to_dict()
# create an instance of InputFormField from a dict
input_form_field_from_dict = InputFormField.from_dict(input_form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


