# CreateUploadRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**local_folder** | **str** | The local folder to monitor. Files in this folder on your local environment will be uploaded to the specified project. Only files matching the filePattern will be uploaded. | 
**file_pattern** | **str** | The regular expression to match a file name. eg: to match all files use &#39;.*&#39; | 
**project_id** | **str** | The project to which the data will be uploaded. | 
**active** | **bool, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**data_format_id** | **str, none_type** | The format which will be assigned to the uploaded data. If not specified, an auto-detection of the format will be done. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


