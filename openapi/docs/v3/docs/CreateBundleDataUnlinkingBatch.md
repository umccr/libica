# CreateBundleDataUnlinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateBundleDataUnlinkingBatchItem]**](CreateBundleDataUnlinkingBatchItem.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_bundle_data_unlinking_batch import CreateBundleDataUnlinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBundleDataUnlinkingBatch from a JSON string
create_bundle_data_unlinking_batch_instance = CreateBundleDataUnlinkingBatch.from_json(json)
# print the JSON string representation of the object
print(CreateBundleDataUnlinkingBatch.to_json())

# convert the object into a dict
create_bundle_data_unlinking_batch_dict = create_bundle_data_unlinking_batch_instance.to_dict()
# create an instance of CreateBundleDataUnlinkingBatch from a dict
create_bundle_data_unlinking_batch_from_dict = CreateBundleDataUnlinkingBatch.from_dict(create_bundle_data_unlinking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


