# SampleCreationBatchSampleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**SampleCreationBatchItemRequest**](SampleCreationBatchItemRequest.md) |  | 
**processing** | [**SampleCreationBatchItemProcessing**](SampleCreationBatchItemProcessing.md) |  | 
**created_sample** | [**Sample**](Sample.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.sample_creation_batch_sample_item import SampleCreationBatchSampleItem

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCreationBatchSampleItem from a JSON string
sample_creation_batch_sample_item_instance = SampleCreationBatchSampleItem.from_json(json)
# print the JSON string representation of the object
print(SampleCreationBatchSampleItem.to_json())

# convert the object into a dict
sample_creation_batch_sample_item_dict = sample_creation_batch_sample_item_instance.to_dict()
# create an instance of SampleCreationBatchSampleItem from a dict
sample_creation_batch_sample_item_from_dict = SampleCreationBatchSampleItem.from_dict(sample_creation_batch_sample_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


