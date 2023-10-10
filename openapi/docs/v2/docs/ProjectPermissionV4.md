# ProjectPermissionV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**role_project** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR, ADMINISTRATOR, DATA_PROVIDER. More types could be added in a future release. | 
**role_flow** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release. | 
**role_base** | **str** | Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release. | 
**role_bench** | **str** | Possible values are: NONE, CONTRIBUTOR, ADMINISTRATOR. More types could be added in a future release. | 
**membership_type** | **str** |  | 
**upload_allowed** | **bool** |  | 
**download_allowed** | **bool** |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**email_address** | **str, none_type** | Only present when membershipType is EMAIL | [optional] 
**workgroup** | [**Workgroup**](Workgroup.md) |  | [optional] 
**invitation_accepted** | **bool, none_type** | Only present when membershipType is EMAIL | [optional] 
**invitation_rejected** | **bool, none_type** | Only present when user is invited by EMAIL | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


