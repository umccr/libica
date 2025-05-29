# BundleDataLinkingBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**BundleDataLinkingBatchItemRequest**](BundleDataLinkingBatchItemRequest.md) |  | 
**processing** | [**BundleDataLinkingBatchItemProcessing**](BundleDataLinkingBatchItemProcessing.md) |  | 
**bundle_data** | [**BundleData**](BundleData.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.bundle_data_linking_batch_item import BundleDataLinkingBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDataLinkingBatchItem from a JSON string
bundle_data_linking_batch_item_instance = BundleDataLinkingBatchItem.from_json(json)
# print the JSON string representation of the object
print(BundleDataLinkingBatchItem.to_json())

# convert the object into a dict
bundle_data_linking_batch_item_dict = bundle_data_linking_batch_item_instance.to_dict()
# create an instance of BundleDataLinkingBatchItem from a dict
bundle_data_linking_batch_item_from_dict = BundleDataLinkingBatchItem.from_dict(bundle_data_linking_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


