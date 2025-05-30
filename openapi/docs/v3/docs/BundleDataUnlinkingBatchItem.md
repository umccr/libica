# BundleDataUnlinkingBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**BundleDataUnlinkingBatchItemRequest**](BundleDataUnlinkingBatchItemRequest.md) |  | 
**processing** | [**BundleDataUnlinkingBatchItemProcessing**](BundleDataUnlinkingBatchItemProcessing.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_data_unlinking_batch_item import BundleDataUnlinkingBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDataUnlinkingBatchItem from a JSON string
bundle_data_unlinking_batch_item_instance = BundleDataUnlinkingBatchItem.from_json(json)
# print the JSON string representation of the object
print(BundleDataUnlinkingBatchItem.to_json())

# convert the object into a dict
bundle_data_unlinking_batch_item_dict = bundle_data_unlinking_batch_item_instance.to_dict()
# create an instance of BundleDataUnlinkingBatchItem from a dict
bundle_data_unlinking_batch_item_from_dict = BundleDataUnlinkingBatchItem.from_dict(bundle_data_unlinking_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


