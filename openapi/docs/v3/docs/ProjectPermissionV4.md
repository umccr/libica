# ProjectPermissionV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**role_project** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR, ADMINISTRATOR, DATA_PROVIDER. More types could be added in a future release. | 
**role_flow** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release. | 
**role_base** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release. | 
**role_bench** | **str** | Possible values are: NONE, CONTRIBUTOR, ADMINISTRATOR. More types could be added in a future release. | 
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
from libica.openapi.v3.models.project_permission_v4 import ProjectPermissionV4

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPermissionV4 from a JSON string
project_permission_v4_instance = ProjectPermissionV4.from_json(json)
# print the JSON string representation of the object
print(ProjectPermissionV4.to_json())

# convert the object into a dict
project_permission_v4_dict = project_permission_v4_instance.to_dict()
# create an instance of ProjectPermissionV4 from a dict
project_permission_v4_from_dict = ProjectPermissionV4.from_dict(project_permission_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


