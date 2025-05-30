# ProjectDataLinkingBatchItemProcessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_linking_batch_item_processing import ProjectDataLinkingBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataLinkingBatchItemProcessing from a JSON string
project_data_linking_batch_item_processing_instance = ProjectDataLinkingBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print(ProjectDataLinkingBatchItemProcessing.to_json())

# convert the object into a dict
project_data_linking_batch_item_processing_dict = project_data_linking_batch_item_processing_instance.to_dict()
# create an instance of ProjectDataLinkingBatchItemProcessing from a dict
project_data_linking_batch_item_processing_from_dict = ProjectDataLinkingBatchItemProcessing.from_dict(project_data_linking_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


