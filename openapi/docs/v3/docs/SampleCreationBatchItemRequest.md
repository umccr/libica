# SampleCreationBatchItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_to_create** | [**CreateSample**](CreateSample.md) |  | 
**complete_sample** | **bool** | Indicates whether the sample must be completed. | 

## Example

```python
from libica.openapi.v3.models.sample_creation_batch_item_request import SampleCreationBatchItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCreationBatchItemRequest from a JSON string
sample_creation_batch_item_request_instance = SampleCreationBatchItemRequest.from_json(json)
# print the JSON string representation of the object
print(SampleCreationBatchItemRequest.to_json())

# convert the object into a dict
sample_creation_batch_item_request_dict = sample_creation_batch_item_request_instance.to_dict()
# create an instance of SampleCreationBatchItemRequest from a dict
sample_creation_batch_item_request_from_dict = SampleCreationBatchItemRequest.from_dict(sample_creation_batch_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


