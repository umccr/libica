# MetadataField

The metadata of the sample

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 
**group_values** | [**List[MetadataField]**](MetadataField.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.metadata_field import MetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataField from a JSON string
metadata_field_instance = MetadataField.from_json(json)
# print the JSON string representation of the object
print(MetadataField.to_json())

# convert the object into a dict
metadata_field_dict = metadata_field_instance.to_dict()
# create an instance of MetadataField from a dict
metadata_field_from_dict = MetadataField.from_dict(metadata_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


