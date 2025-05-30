# InputFormFieldDataFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_filter** | **str** |  | [optional] 
**data_format** | **List[str]** |  | [optional] 
**data_type** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_field_data_filter import InputFormFieldDataFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormFieldDataFilter from a JSON string
input_form_field_data_filter_instance = InputFormFieldDataFilter.from_json(json)
# print the JSON string representation of the object
print(InputFormFieldDataFilter.to_json())

# convert the object into a dict
input_form_field_data_filter_dict = input_form_field_data_filter_instance.to_dict()
# create an instance of InputFormFieldDataFilter from a dict
input_form_field_data_filter_from_dict = InputFormFieldDataFilter.from_dict(input_form_field_data_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


