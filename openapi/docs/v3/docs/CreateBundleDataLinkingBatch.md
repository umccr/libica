# CreateBundleDataLinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateBundleDataLinkingBatchItem]**](CreateBundleDataLinkingBatchItem.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_bundle_data_linking_batch import CreateBundleDataLinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBundleDataLinkingBatch from a JSON string
create_bundle_data_linking_batch_instance = CreateBundleDataLinkingBatch.from_json(json)
# print the JSON string representation of the object
print(CreateBundleDataLinkingBatch.to_json())

# convert the object into a dict
create_bundle_data_linking_batch_dict = create_bundle_data_linking_batch_instance.to_dict()
# create an instance of CreateBundleDataLinkingBatch from a dict
create_bundle_data_linking_batch_from_dict = CreateBundleDataLinkingBatch.from_dict(create_bundle_data_linking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


