# BaseJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**type** | **str** | The type of the job | 
**status** | **str** | The status of the job | 
**tenant_name** | **str, none_type** |  | [optional] 
**description** | **str, none_type** | A short description of the base job | [optional] 
**table** | [**ProjectBaseTable**](ProjectBaseTable.md) |  | [optional] 
**overall_duration** | **int, none_type** | The duration of the job expressed in milliseconds | [optional] 
**details** | **str, none_type** | Detailed description of the job | [optional] 
**bytes_billed** | **int, none_type** | Bytes billed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


