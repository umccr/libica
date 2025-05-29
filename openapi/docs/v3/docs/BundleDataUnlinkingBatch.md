# BundleDataUnlinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_data_unlinking_batch import BundleDataUnlinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDataUnlinkingBatch from a JSON string
bundle_data_unlinking_batch_instance = BundleDataUnlinkingBatch.from_json(json)
# print the JSON string representation of the object
print(BundleDataUnlinkingBatch.to_json())

# convert the object into a dict
bundle_data_unlinking_batch_dict = bundle_data_unlinking_batch_instance.to_dict()
# create an instance of BundleDataUnlinkingBatch from a dict
bundle_data_unlinking_batch_from_dict = BundleDataUnlinkingBatch.from_dict(bundle_data_unlinking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


