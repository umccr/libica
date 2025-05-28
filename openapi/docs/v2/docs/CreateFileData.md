# CreateFileData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file as how it will be created. | 
**folder_id** | **str, none_type** | The id of the folder you want to create this new file in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str, none_type** | The absolute path of the folder you want to create this new file in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**format_code** | **str, none_type** | The code of the format you would like to assign at creation time. If not specified, auto format assignment will be done. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


