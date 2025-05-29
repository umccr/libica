# ProjectPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectPermission]**](ProjectPermission.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_permission_list import ProjectPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPermissionList from a JSON string
project_permission_list_instance = ProjectPermissionList.from_json(json)
# print the JSON string representation of the object
print(ProjectPermissionList.to_json())

# convert the object into a dict
project_permission_list_dict = project_permission_list_instance.to_dict()
# create an instance of ProjectPermissionList from a dict
project_permission_list_from_dict = ProjectPermissionList.from_dict(project_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


