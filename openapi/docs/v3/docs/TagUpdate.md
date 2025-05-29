# TagUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_tags** | **List[str]** |  | [optional] 
**remove_tags** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.tag_update import TagUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TagUpdate from a JSON string
tag_update_instance = TagUpdate.from_json(json)
# print the JSON string representation of the object
print(TagUpdate.to_json())

# convert the object into a dict
tag_update_dict = tag_update_instance.to_dict()
# create an instance of TagUpdate from a dict
tag_update_from_dict = TagUpdate.from_dict(tag_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


