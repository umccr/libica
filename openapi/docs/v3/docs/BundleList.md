# BundleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Bundle]**](Bundle.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_list import BundleList

# TODO update the JSON string below
json = "{}"
# create an instance of BundleList from a JSON string
bundle_list_instance = BundleList.from_json(json)
# print the JSON string representation of the object
print(BundleList.to_json())

# convert the object into a dict
bundle_list_dict = bundle_list_instance.to_dict()
# create an instance of BundleList from a dict
bundle_list_from_dict = BundleList.from_dict(bundle_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


