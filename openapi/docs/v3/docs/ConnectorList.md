# ConnectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Connector]**](Connector.md) |  | 

## Example

```python
from libica.openapi.v3.models.connector_list import ConnectorList

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorList from a JSON string
connector_list_instance = ConnectorList.from_json(json)
# print the JSON string representation of the object
print(ConnectorList.to_json())

# convert the object into a dict
connector_list_dict = connector_list_instance.to_dict()
# create an instance of ConnectorList from a dict
connector_list_from_dict = ConnectorList.from_dict(connector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


