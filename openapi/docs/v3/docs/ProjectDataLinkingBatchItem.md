# ProjectDataLinkingBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataLinkingBatchItemRequest**](ProjectDataLinkingBatchItemRequest.md) |  | 
**processing** | [**ProjectDataLinkingBatchItemProcessing**](ProjectDataLinkingBatchItemProcessing.md) |  | 
**created_project_data** | [**ProjectData**](ProjectData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_linking_batch_item import ProjectDataLinkingBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataLinkingBatchItem from a JSON string
project_data_linking_batch_item_instance = ProjectDataLinkingBatchItem.from_json(json)
# print the JSON string representation of the object
print(ProjectDataLinkingBatchItem.to_json())

# convert the object into a dict
project_data_linking_batch_item_dict = project_data_linking_batch_item_instance.to_dict()
# create an instance of ProjectDataLinkingBatchItem from a dict
project_data_linking_batch_item_from_dict = ProjectDataLinkingBatchItem.from_dict(project_data_linking_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


