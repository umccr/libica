# BundleDataUnlinkingBatchItemProcessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Possible values are: INITIALISED, WAITING_RESOURCES, RUNNING, UNLINKED, ALREADY_UNLINKED, FAILED, PARTIALLY_UNLINKED. More types could be added in a future release. | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.bundle_data_unlinking_batch_item_processing import BundleDataUnlinkingBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDataUnlinkingBatchItemProcessing from a JSON string
bundle_data_unlinking_batch_item_processing_instance = BundleDataUnlinkingBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print(BundleDataUnlinkingBatchItemProcessing.to_json())

# convert the object into a dict
bundle_data_unlinking_batch_item_processing_dict = bundle_data_unlinking_batch_item_processing_instance.to_dict()
# create an instance of BundleDataUnlinkingBatchItemProcessing from a dict
bundle_data_unlinking_batch_item_processing_from_dict = BundleDataUnlinkingBatchItemProcessing.from_dict(bundle_data_unlinking_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


