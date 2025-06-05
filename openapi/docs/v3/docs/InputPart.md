# InputPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type_from_message** | **bool** |  | [optional] 
**body_as_string** | **str** |  | [optional] 
**media_type** | [**InputPartMediaType**](InputPartMediaType.md) |  | [optional] 
**headers** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_part import InputPart

# TODO update the JSON string below
json = "{}"
# create an instance of InputPart from a JSON string
input_part_instance = InputPart.from_json(json)
# print the JSON string representation of the object
print(InputPart.to_json())

# convert the object into a dict
input_part_dict = input_part_instance.to_dict()
# create an instance of InputPart from a dict
input_part_from_dict = InputPart.from_dict(input_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


