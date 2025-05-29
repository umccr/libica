# ProjectDataLinkingBatchItemProcessingV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Possible values are: INITIALISED, WAITING_RESOURCES, RUNNING, LINKED, ALREADY_LINKED, FAILED, PARTIALLY_LINKED. More types could be added in a future release. | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_linking_batch_item_processing_v4 import ProjectDataLinkingBatchItemProcessingV4

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataLinkingBatchItemProcessingV4 from a JSON string
project_data_linking_batch_item_processing_v4_instance = ProjectDataLinkingBatchItemProcessingV4.from_json(json)
# print the JSON string representation of the object
print(ProjectDataLinkingBatchItemProcessingV4.to_json())

# convert the object into a dict
project_data_linking_batch_item_processing_v4_dict = project_data_linking_batch_item_processing_v4_instance.to_dict()
# create an instance of ProjectDataLinkingBatchItemProcessingV4 from a dict
project_data_linking_batch_item_processing_v4_from_dict = ProjectDataLinkingBatchItemProcessingV4.from_dict(project_data_linking_batch_item_processing_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


