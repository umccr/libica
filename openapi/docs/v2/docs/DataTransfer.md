# DataTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**reference** | **str** |  | 
**direction** | **str** |  | 
**data_transferred** | **int** | The data transferred so far in bytes. | 
**status** | **str** |  | 
**data** | [**Data**](Data.md) |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**connector** | [**Connector**](Connector.md) |  | [optional] 
**protocol** | **str, none_type** |  | [optional]  if omitted the server will use the default value of "HTTPS"
**status_message** | **str, none_type** | A message explaining the reason why the transfer is in the current status. | [optional] 
**duration** | **int, none_type** | The overall duration of of the transfer defined in seconds. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


