# ProjectDataUpdateBatchItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | Data to apply the update to (recursively, if it&#39;s a folder). | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**will_be_archived_at** | **datetime** | The timestamp when the data should be archived. | [optional] 
**will_be_deleted_at** | **datetime** | The timestamp when the data should be deleted. | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_update_batch_item_request import ProjectDataUpdateBatchItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUpdateBatchItemRequest from a JSON string
project_data_update_batch_item_request_instance = ProjectDataUpdateBatchItemRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectDataUpdateBatchItemRequest.to_json())

# convert the object into a dict
project_data_update_batch_item_request_dict = project_data_update_batch_item_request_instance.to_dict()
# create an instance of ProjectDataUpdateBatchItemRequest from a dict
project_data_update_batch_item_request_from_dict = ProjectDataUpdateBatchItemRequest.from_dict(project_data_update_batch_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


