# ProjectPermissionListV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectPermissionV4]**](ProjectPermissionV4.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_permission_list_v4 import ProjectPermissionListV4

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPermissionListV4 from a JSON string
project_permission_list_v4_instance = ProjectPermissionListV4.from_json(json)
# print the JSON string representation of the object
print(ProjectPermissionListV4.to_json())

# convert the object into a dict
project_permission_list_v4_dict = project_permission_list_v4_instance.to_dict()
# create an instance of ProjectPermissionListV4 from a dict
project_permission_list_v4_from_dict = ProjectPermissionListV4.from_dict(project_permission_list_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


