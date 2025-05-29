# MetadataModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**state** | **str** |  | 
**parent_model_id** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.metadata_model import MetadataModel

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataModel from a JSON string
metadata_model_instance = MetadataModel.from_json(json)
# print the JSON string representation of the object
print(MetadataModel.to_json())

# convert the object into a dict
metadata_model_dict = metadata_model_instance.to_dict()
# create an instance of MetadataModel from a dict
metadata_model_from_dict = MetadataModel.from_dict(metadata_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


