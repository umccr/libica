# UploadRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**code** | **str** |  | 
**local_folder** | **str** | The local folder to monitor. Files in this folder on your local environment will be uploaded to the specified project. Only files matching the filePattern will be uploaded. | 
**file_pattern** | **str** | The regular expression to match a file name. eg: to match all files use &#39;.*&#39; | 
**project** | [**Project**](Project.md) |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**active** | **bool, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**data_format** | [**DataFormat**](DataFormat.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


