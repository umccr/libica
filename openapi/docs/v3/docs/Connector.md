# Connector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** |  | 
**active** | **bool** |  | 
**connected** | **bool** | Indicates if the connector is connected or not. This is cached so even when the connector is no longer connected, for a short time this still may return true. | 
**technical_code** | **str** | Technical code to be used for processing. | 
**initialization_key** | **str** | The key provided via other channels to initialize the installation. | [optional] 
**description** | **str** | The general description of the connector instance including its purpose. | [optional] 
**mode** | **str** | The mode the connector runs in. | 
**max_bandwidth** | **float** | The maximum bandwidth defined in MB per second. | [optional] 
**max_concurrent_transfers** | **int** | The maximum amount of concurrent transfers that this connector can execute. | [optional] 
**os** | **str** | The target OS of the original connector installer. | 
**installation_status** | **str** |  | 
**new_connector_version_available** | **bool** |  | 

## Example

```python
from libica.openapi.v3.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print(Connector.to_json())

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_from_dict = Connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


