# CreateProjectPermissionV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_project** | **str** |  | 
**role_flow** | **str** |  | 
**role_base** | **str** |  | 
**role_bench** | **str** |  | 
**membership_type** | **str** | How users are invited to the project | 
**user_id** | **str** | the id of the user that should be given access, required when membershipType is USER | [optional] 
**email_address** | **str** | The email to invite a user on, required when membershipType is EMAIL | [optional] 
**workgroup_id** | **str** | the id of the workgroup to give access, required when membershipType is WORKGROUP | [optional] 
**upload_allowed** | **bool** | Indicates if uploading data is allowed or not. | 
**download_allowed** | **bool** | Indicates if downloading data is allowed or not. | 

## Example

```python
from libica.openapi.v3.models.create_project_permission_v4 import CreateProjectPermissionV4

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectPermissionV4 from a JSON string
create_project_permission_v4_instance = CreateProjectPermissionV4.from_json(json)
# print the JSON string representation of the object
print(CreateProjectPermissionV4.to_json())

# convert the object into a dict
create_project_permission_v4_dict = create_project_permission_v4_instance.to_dict()
# create an instance of CreateProjectPermissionV4 from a dict
create_project_permission_v4_from_dict = CreateProjectPermissionV4.from_dict(create_project_permission_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


