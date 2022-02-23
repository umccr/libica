# CreateConnector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**active** | **bool** |  | 
**mode** | **str** | The mode the connector runs in. | 
**os** | **str** | The target OS of the original connector installer. | 
**country_id** | **str, none_type** | ID of the country. If not provided then the country of the tenant will be used. | [optional] 
**address_line1** | **str, none_type** |  | [optional] 
**address_line2** | **str, none_type** |  | [optional] 
**address_line3** | **str, none_type** |  | [optional] 
**postal_code** | **str, none_type** |  | [optional] 
**city** | **str, none_type** |  | [optional] 
**state** | **str, none_type** |  | [optional] 
**description** | **str, none_type** | The general description of the connector instance including its purpose. | [optional] 
**max_bandwidth** | **float, none_type** | The maximum bandwidth defined in MB per second. | [optional] 
**max_concurrent_transfers** | **int, none_type** | The maximum amount of concurrent transfers that this connector can execute. | [optional]  if omitted the server will use the default value of 2
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


