# Connector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**code** | **str** |  | 
**active** | **bool** |  | 
**connected** | **bool** | Indicates if the connector is connected or not. This is cached so even when the connector is no longer connected, for a short time this still may return true. | 
**technical_code** | **str** | Technical code to be used for processing. | 
**mode** | **str** | The mode the connector runs in. | 
**os** | **str** | The target OS of the original connector installer. | 
**installation_status** | **str** |  | 
**new_connector_version_available** | **bool** |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**initialization_key** | **str, none_type** | The key provided via other channels to initialize the installation. | [optional] 
**description** | **str, none_type** | The general description of the connector instance including its purpose. | [optional] 
**max_bandwidth** | **float, none_type** | The maximum bandwidth defined in MB per second. | [optional] 
**max_concurrent_transfers** | **int, none_type** | The maximum amount of concurrent transfers that this connector can execute. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


