# CreateSampleCreationBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateSampleCreationBatchSampleItem]**](CreateSampleCreationBatchSampleItem.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_sample_creation_batch import CreateSampleCreationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSampleCreationBatch from a JSON string
create_sample_creation_batch_instance = CreateSampleCreationBatch.from_json(json)
# print the JSON string representation of the object
print(CreateSampleCreationBatch.to_json())

# convert the object into a dict
create_sample_creation_batch_dict = create_sample_creation_batch_instance.to_dict()
# create an instance of CreateSampleCreationBatch from a dict
create_sample_creation_batch_from_dict = CreateSampleCreationBatch.from_dict(create_sample_creation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


