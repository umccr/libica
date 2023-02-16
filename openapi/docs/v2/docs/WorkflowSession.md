# WorkflowSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_reference** | **str** | The user reference of the workflow session | 
**workflow** | [**Workflow**](Workflow.md) |  | 
**status** | **str** | The status of the workflow session | 
**tags** | [**WorkflowSessionTag**](WorkflowSessionTag.md) |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**start_date** | **datetime, none_type** | When the workflow session was started | [optional] 
**end_date** | **datetime, none_type** | When the workflow session was finished | [optional] 
**summary** | **str, none_type** | The summary of the workflow session | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


