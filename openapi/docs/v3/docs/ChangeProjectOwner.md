# ChangeProjectOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner_id** | **str** | The id of the new project owner. | 

## Example

```python
from libica.openapi.v3.models.change_project_owner import ChangeProjectOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeProjectOwner from a JSON string
change_project_owner_instance = ChangeProjectOwner.from_json(json)
# print the JSON string representation of the object
print(ChangeProjectOwner.to_json())

# convert the object into a dict
change_project_owner_dict = change_project_owner_instance.to_dict()
# create an instance of ChangeProjectOwner from a dict
change_project_owner_from_dict = ChangeProjectOwner.from_dict(change_project_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


