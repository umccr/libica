# DataTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**reference** | **str** |  | 
**direction** | **str** |  | 
**connector** | [**Connector**](Connector.md) |  | [optional] 
**protocol** | **str** |  | [optional] 
**data_transferred** | **int** | The data transferred so far in bytes. | 
**status** | **str** |  | 
**status_message** | **str** | A message explaining the reason why the transfer is in the current status. | [optional] 
**duration** | **int** | The overall duration of of the transfer defined in seconds. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**data** | [**Data**](Data.md) |  | 

## Example

```python
from libica.openapi.v3.models.data_transfer import DataTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of DataTransfer from a JSON string
data_transfer_instance = DataTransfer.from_json(json)
# print the JSON string representation of the object
print(DataTransfer.to_json())

# convert the object into a dict
data_transfer_dict = data_transfer_instance.to_dict()
# create an instance of DataTransfer from a dict
data_transfer_from_dict = DataTransfer.from_dict(data_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


