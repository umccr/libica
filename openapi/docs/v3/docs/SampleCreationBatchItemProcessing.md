# SampleCreationBatchItemProcessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.sample_creation_batch_item_processing import SampleCreationBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCreationBatchItemProcessing from a JSON string
sample_creation_batch_item_processing_instance = SampleCreationBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print(SampleCreationBatchItemProcessing.to_json())

# convert the object into a dict
sample_creation_batch_item_processing_dict = sample_creation_batch_item_processing_instance.to_dict()
# create an instance of SampleCreationBatchItemProcessing from a dict
sample_creation_batch_item_processing_from_dict = SampleCreationBatchItemProcessing.from_dict(sample_creation_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


