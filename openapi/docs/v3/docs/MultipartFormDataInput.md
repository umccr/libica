# MultipartFormDataInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_data** | [**Dict[str, InputPart]**](InputPart.md) |  | [optional] 
**form_data_map** | **Dict[str, List[InputPart]]** |  | [optional] 
**parts** | [**List[InputPart]**](InputPart.md) |  | [optional] 
**preamble** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.multipart_form_data_input import MultipartFormDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartFormDataInput from a JSON string
multipart_form_data_input_instance = MultipartFormDataInput.from_json(json)
# print the JSON string representation of the object
print(MultipartFormDataInput.to_json())

# convert the object into a dict
multipart_form_data_input_dict = multipart_form_data_input_instance.to_dict()
# create an instance of MultipartFormDataInput from a dict
multipart_form_data_input_from_dict = MultipartFormDataInput.from_dict(multipart_form_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


