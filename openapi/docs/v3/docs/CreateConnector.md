# CreateConnector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**active** | **bool** |  | 
**description** | **str** | The general description of the connector instance including its purpose. | [optional] 
**mode** | **str** | The mode the connector runs in. | 
**max_bandwidth** | **float** | The maximum bandwidth defined in MB per second. | [optional] 
**max_concurrent_transfers** | **int** | The maximum amount of concurrent transfers that this connector can execute. | [optional] [default to 2]
**os** | **str** | The target OS of the original connector installer. | 

## Example

```python
from libica.openapi.v3.models.create_connector import CreateConnector

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnector from a JSON string
create_connector_instance = CreateConnector.from_json(json)
# print the JSON string representation of the object
print(CreateConnector.to_json())

# convert the object into a dict
create_connector_dict = create_connector_instance.to_dict()
# create an instance of CreateConnector from a dict
create_connector_from_dict = CreateConnector.from_dict(create_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


