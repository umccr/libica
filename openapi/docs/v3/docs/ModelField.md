# ModelField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**multivalued** | **bool** |  | [optional] 
**filled_by_pipeline** | **bool** |  | [optional] 
**fields** | [**List[ModelField]**](ModelField.md) |  | [optional] 
**enumeration_values** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


