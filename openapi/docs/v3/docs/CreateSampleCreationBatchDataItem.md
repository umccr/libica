# CreateSampleCreationBatchDataItem

The data to be linked to the new sample.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.create_sample_creation_batch_data_item import CreateSampleCreationBatchDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSampleCreationBatchDataItem from a JSON string
create_sample_creation_batch_data_item_instance = CreateSampleCreationBatchDataItem.from_json(json)
# print the JSON string representation of the object
print(CreateSampleCreationBatchDataItem.to_json())

# convert the object into a dict
create_sample_creation_batch_data_item_dict = create_sample_creation_batch_data_item_instance.to_dict()
# create an instance of CreateSampleCreationBatchDataItem from a dict
create_sample_creation_batch_data_item_from_dict = CreateSampleCreationBatchDataItem.from_dict(create_sample_creation_batch_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


