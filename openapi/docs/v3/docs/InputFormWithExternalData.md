# InputFormWithExternalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** |  | [optional] 
**external_data** | [**InputFormExternalData**](InputFormExternalData.md) |  | [optional] 
**mount_path** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_with_external_data import InputFormWithExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormWithExternalData from a JSON string
input_form_with_external_data_instance = InputFormWithExternalData.from_json(json)
# print the JSON string representation of the object
print(InputFormWithExternalData.to_json())

# convert the object into a dict
input_form_with_external_data_dict = input_form_with_external_data_instance.to_dict()
# create an instance of InputFormWithExternalData from a dict
input_form_with_external_data_from_dict = InputFormWithExternalData.from_dict(input_form_with_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


