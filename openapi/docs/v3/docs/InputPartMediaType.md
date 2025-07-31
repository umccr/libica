# InputPartMediaType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**wildcard_subtype** | **bool** |  | [optional] 
**wildcard_type** | **bool** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.input_part_media_type import InputPartMediaType

# TODO update the JSON string below
json = "{}"
# create an instance of InputPartMediaType from a JSON string
input_part_media_type_instance = InputPartMediaType.from_json(json)
# print the JSON string representation of the object
print(InputPartMediaType.to_json())

# convert the object into a dict
input_part_media_type_dict = input_part_media_type_instance.to_dict()
# create an instance of InputPartMediaType from a dict
input_part_media_type_from_dict = InputPartMediaType.from_dict(input_part_media_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


