# InputFormFieldValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**values** | **List[Optional[str]]** | Use &#39;values&#39; for all fields except data fields. Use string values to avoid rounding of numbers with a high precision. Values of length 0 for textbox type fields will be treated as null. | [optional] 
**data_values** | [**List[InputFormData]**](InputFormData.md) | Use &#39;dataValues&#39; for data fields. | [optional] 
**external_data_values** | [**List[AnalysisInputExternalData]**](AnalysisInputExternalData.md) | Use &#39;externalDataValues&#39; for external data | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_field_values import InputFormFieldValues

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormFieldValues from a JSON string
input_form_field_values_instance = InputFormFieldValues.from_json(json)
# print the JSON string representation of the object
print(InputFormFieldValues.to_json())

# convert the object into a dict
input_form_field_values_dict = input_form_field_values_instance.to_dict()
# create an instance of InputFormFieldValues from a dict
input_form_field_values_from_dict = InputFormFieldValues.from_dict(input_form_field_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


