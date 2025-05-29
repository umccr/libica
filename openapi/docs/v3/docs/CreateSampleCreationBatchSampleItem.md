# CreateSampleCreationBatchSampleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_to_create** | [**CreateSample**](CreateSample.md) |  | 
**data_to_link** | [**List[CreateSampleCreationBatchDataItem]**](CreateSampleCreationBatchDataItem.md) | The data to be linked to the new sample. | [optional] 
**complete_sample** | **bool** | Indicates whether the sample must be completed. | 

## Example

```python
from libica.openapi.v3.models.create_sample_creation_batch_sample_item import CreateSampleCreationBatchSampleItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSampleCreationBatchSampleItem from a JSON string
create_sample_creation_batch_sample_item_instance = CreateSampleCreationBatchSampleItem.from_json(json)
# print the JSON string representation of the object
print(CreateSampleCreationBatchSampleItem.to_json())

# convert the object into a dict
create_sample_creation_batch_sample_item_dict = create_sample_creation_batch_sample_item_instance.to_dict()
# create an instance of CreateSampleCreationBatchSampleItem from a dict
create_sample_creation_batch_sample_item_from_dict = CreateSampleCreationBatchSampleItem.from_dict(create_sample_creation_batch_sample_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


