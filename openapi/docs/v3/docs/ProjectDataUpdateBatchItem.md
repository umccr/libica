# ProjectDataUpdateBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataUpdateBatchItemRequest**](ProjectDataUpdateBatchItemRequest.md) |  | 
**processing** | [**ProjectDataUpdateBatchItemProcessing**](ProjectDataUpdateBatchItemProcessing.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_data_update_batch_item import ProjectDataUpdateBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUpdateBatchItem from a JSON string
project_data_update_batch_item_instance = ProjectDataUpdateBatchItem.from_json(json)
# print the JSON string representation of the object
print(ProjectDataUpdateBatchItem.to_json())

# convert the object into a dict
project_data_update_batch_item_dict = project_data_update_batch_item_instance.to_dict()
# create an instance of ProjectDataUpdateBatchItem from a dict
project_data_update_batch_item_from_dict = ProjectDataUpdateBatchItem.from_dict(project_data_update_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


