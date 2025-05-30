# ProjectDataMoveBatchItemProcessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the batch item. Possible values are: QUEUED, MOVING, MOVED, PARTIALLY_MOVED, FAILED. More statuses could be added in a future release. | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_move_batch_item_processing import ProjectDataMoveBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataMoveBatchItemProcessing from a JSON string
project_data_move_batch_item_processing_instance = ProjectDataMoveBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print(ProjectDataMoveBatchItemProcessing.to_json())

# convert the object into a dict
project_data_move_batch_item_processing_dict = project_data_move_batch_item_processing_instance.to_dict()
# create an instance of ProjectDataMoveBatchItemProcessing from a dict
project_data_move_batch_item_processing_from_dict = ProjectDataMoveBatchItemProcessing.from_dict(project_data_move_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


