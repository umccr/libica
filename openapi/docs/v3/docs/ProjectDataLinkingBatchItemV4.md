# ProjectDataLinkingBatchItemV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataLinkingBatchItemRequest**](ProjectDataLinkingBatchItemRequest.md) |  | 
**processing** | [**ProjectDataLinkingBatchItemProcessingV4**](ProjectDataLinkingBatchItemProcessingV4.md) |  | 
**created_project_data** | [**ProjectData**](ProjectData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_linking_batch_item_v4 import ProjectDataLinkingBatchItemV4

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataLinkingBatchItemV4 from a JSON string
project_data_linking_batch_item_v4_instance = ProjectDataLinkingBatchItemV4.from_json(json)
# print the JSON string representation of the object
print(ProjectDataLinkingBatchItemV4.to_json())

# convert the object into a dict
project_data_linking_batch_item_v4_dict = project_data_linking_batch_item_v4_instance.to_dict()
# create an instance of ProjectDataLinkingBatchItemV4 from a dict
project_data_linking_batch_item_v4_from_dict = ProjectDataLinkingBatchItemV4.from_dict(project_data_linking_batch_item_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


