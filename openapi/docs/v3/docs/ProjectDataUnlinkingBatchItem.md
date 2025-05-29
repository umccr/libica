# ProjectDataUnlinkingBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataUnlinkingBatchItemRequest**](ProjectDataUnlinkingBatchItemRequest.md) |  | 
**processing** | [**ProjectDataUnlinkingBatchItemProcessing**](ProjectDataUnlinkingBatchItemProcessing.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_data_unlinking_batch_item import ProjectDataUnlinkingBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUnlinkingBatchItem from a JSON string
project_data_unlinking_batch_item_instance = ProjectDataUnlinkingBatchItem.from_json(json)
# print the JSON string representation of the object
print(ProjectDataUnlinkingBatchItem.to_json())

# convert the object into a dict
project_data_unlinking_batch_item_dict = project_data_unlinking_batch_item_instance.to_dict()
# create an instance of ProjectDataUnlinkingBatchItem from a dict
project_data_unlinking_batch_item_from_dict = ProjectDataUnlinkingBatchItem.from_dict(project_data_unlinking_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


