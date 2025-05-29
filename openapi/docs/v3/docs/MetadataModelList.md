# MetadataModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetadataModel]**](MetadataModel.md) |  | 

## Example

```python
from libica.openapi.v3.models.metadata_model_list import MetadataModelList

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataModelList from a JSON string
metadata_model_list_instance = MetadataModelList.from_json(json)
# print the JSON string representation of the object
print(MetadataModelList.to_json())

# convert the object into a dict
metadata_model_list_dict = metadata_model_list_instance.to_dict()
# create an instance of MetadataModelList from a dict
metadata_model_list_from_dict = MetadataModelList.from_dict(metadata_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


