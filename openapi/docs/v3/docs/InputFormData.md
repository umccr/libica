# InputFormData

Use 'dataValues' for data fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** |  | 
**mount_path** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_data import InputFormData

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormData from a JSON string
input_form_data_instance = InputFormData.from_json(json)
# print the JSON string representation of the object
print(InputFormData.to_json())

# convert the object into a dict
input_form_data_dict = input_form_data_instance.to_dict()
# create an instance of InputFormData from a dict
input_form_data_from_dict = InputFormData.from_dict(input_form_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


