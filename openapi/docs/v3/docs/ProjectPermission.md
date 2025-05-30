# ProjectPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**role_project** | **str** |  | 
**role_flow** | **str** |  | 
**role_base** | **str** |  | 
**role_bench** | **str** |  | 
**membership_type** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 
**email_address** | **str** | Only present when membershipType is EMAIL | [optional] 
**workgroup** | [**Workgroup**](Workgroup.md) |  | [optional] 
**invitation_accepted** | **bool** | Only present when membershipType is EMAIL | [optional] 
**invitation_rejected** | **bool** | Only present when user is invited by EMAIL | [optional] 
**upload_allowed** | **bool** |  | 
**download_allowed** | **bool** |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_permission import ProjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPermission from a JSON string
project_permission_instance = ProjectPermission.from_json(json)
# print the JSON string representation of the object
print(ProjectPermission.to_json())

# convert the object into a dict
project_permission_dict = project_permission_instance.to_dict()
# create an instance of ProjectPermission from a dict
project_permission_from_dict = ProjectPermission.from_dict(project_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


