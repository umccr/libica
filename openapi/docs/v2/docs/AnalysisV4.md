# AnalysisV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**reference** | **str** | The unique reference of the analysis | 
**user_reference** | **str** | The user reference of the analysis | 
**pipeline** | [**PipelineV4**](PipelineV4.md) |  | 
**status** | **str** | The status of the analysis | 
**tags** | [**AnalysisTag**](AnalysisTag.md) |  | 
**workflow_session** | [**WorkflowSessionV4**](WorkflowSessionV4.md) |  | [optional] 
**start_date** | **datetime, none_type** | When the analysis was started | [optional] 
**end_date** | **datetime, none_type** | When the analysis was finished | [optional] 
**summary** | **str, none_type** | The summary of the analysis | [optional] 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | [optional] 
**analysis_priority** | **str, none_type** | The priority of the analysis | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


