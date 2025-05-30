# InputFormExternalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 
**s3_details** | [**InputFormS3DataDetails**](InputFormS3DataDetails.md) |  | [optional] 
**basespace_details** | [**InputFormBaseSpaceDataDetails**](InputFormBaseSpaceDataDetails.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_external_data import InputFormExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormExternalData from a JSON string
input_form_external_data_instance = InputFormExternalData.from_json(json)
# print the JSON string representation of the object
print(InputFormExternalData.to_json())

# convert the object into a dict
input_form_external_data_dict = input_form_external_data_instance.to_dict()
# create an instance of InputFormExternalData from a dict
input_form_external_data_from_dict = InputFormExternalData.from_dict(input_form_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


