# BundleSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | [**Sample**](Sample.md) |  | 
**bundle_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.bundle_sample import BundleSample

# TODO update the JSON string below
json = "{}"
# create an instance of BundleSample from a JSON string
bundle_sample_instance = BundleSample.from_json(json)
# print the JSON string representation of the object
print(BundleSample.to_json())

# convert the object into a dict
bundle_sample_dict = bundle_sample_instance.to_dict()
# create an instance of BundleSample from a dict
bundle_sample_from_dict = BundleSample.from_dict(bundle_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


