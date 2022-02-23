# DownloadRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**code** | **str** |  | 
**sequence** | **int** | Defines the order of the rule. | 
**target_local_folder** | **str** | The local folder where to write the data. | 
**tenant_name** | **str, none_type** |  | [optional] 
**active** | **bool, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**format_code** | **str, none_type** | Regular expression to select which format this rule applies to. | [optional] 
**project_name** | **str, none_type** | Regular expression to select which project this rule applies to. | [optional] 
**file_name_expression** | **str, none_type** | Will allow the filename to be modified including a set of variables | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


