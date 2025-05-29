# BundleDataLinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_data_linking_batch import BundleDataLinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDataLinkingBatch from a JSON string
bundle_data_linking_batch_instance = BundleDataLinkingBatch.from_json(json)
# print the JSON string representation of the object
print(BundleDataLinkingBatch.to_json())

# convert the object into a dict
bundle_data_linking_batch_dict = bundle_data_linking_batch_instance.to_dict()
# create an instance of BundleDataLinkingBatch from a dict
bundle_data_linking_batch_from_dict = BundleDataLinkingBatch.from_dict(bundle_data_linking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


