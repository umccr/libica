# Config


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the report | 
**regex** | **str** | regex pattern of the filename | 
**format** | **str, none_type** | Format of the file | [optional] 
**match_target** | **str, none_type** | Selects which part of the analysis output file the regex is matched against. FILE_NAME matches against the file name only (segment after the last /). FULL_PATH matches against the file&#39;s full relative path within the analysis output tree. Defaults to FILE_NAME when omitted. One of: FILE_NAME, FULL_PATH. | [optional]  if omitted the server will use the default value of "FILE_NAME"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


