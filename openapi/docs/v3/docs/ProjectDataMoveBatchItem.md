# ProjectDataMoveBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataMoveBatchItemRequest**](ProjectDataMoveBatchItemRequest.md) |  | 
**processing** | [**ProjectDataMoveBatchItemProcessing**](ProjectDataMoveBatchItemProcessing.md) |  | 
**created_project_data** | [**ProjectData**](ProjectData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_move_batch_item import ProjectDataMoveBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataMoveBatchItem from a JSON string
project_data_move_batch_item_instance = ProjectDataMoveBatchItem.from_json(json)
# print the JSON string representation of the object
print(ProjectDataMoveBatchItem.to_json())

# convert the object into a dict
project_data_move_batch_item_dict = project_data_move_batch_item_instance.to_dict()
# create an instance of ProjectDataMoveBatchItem from a dict
project_data_move_batch_item_from_dict = ProjectDataMoveBatchItem.from_dict(project_data_move_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


