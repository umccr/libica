# InputFormGroupField


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
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**choices** | [**List[InputFormFieldChoice]**](InputFormFieldChoice.md) |  | [optional] 
**data_filter** | [**InputFormFieldDataFilter**](InputFormFieldDataFilter.md) |  | [optional] 
**regex** | **str** |  | [optional] 
**regex_error_message** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**empty_values_allowed** | **bool** |  | [optional] 
**update_render_on_change** | **bool** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_group_field import InputFormGroupField

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormGroupField from a JSON string
input_form_group_field_instance = InputFormGroupField.from_json(json)
# print the JSON string representation of the object
print(InputFormGroupField.to_json())

# convert the object into a dict
input_form_group_field_dict = input_form_group_field_instance.to_dict()
# create an instance of InputFormGroupField from a dict
input_form_group_field_from_dict = InputFormGroupField.from_dict(input_form_group_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


