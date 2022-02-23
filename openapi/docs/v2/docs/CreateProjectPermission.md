# CreateProjectPermission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_project** | **str** |  | 
**role_flow** | **str** |  | 
**role_base** | **str** |  | 
**role_bench** | **str** |  | 
**membership_type** | **str** | How users are invited to the project | 
**upload_allowed** | **bool** | Indicates if uploading data is allowed or not. | 
**download_allowed** | **bool** | Indicates if downloading data is allowed or not. | 
**user_id** | **str, none_type** | the id of the user that should be given access, required when membershipType is USER | [optional] 
**email_address** | **str, none_type** | The email to invite a user on, required when membershipType is EMAIL | [optional] 
**workgroup_id** | **str, none_type** | the id of the workgroup to give access, required when membershipType is WORKGROUP | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


