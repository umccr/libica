# StorageBundleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageBundle]**](StorageBundle.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_bundle_list import StorageBundleList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBundleList from a JSON string
storage_bundle_list_instance = StorageBundleList.from_json(json)
# print the JSON string representation of the object
print(StorageBundleList.to_json())

# convert the object into a dict
storage_bundle_list_dict = storage_bundle_list_instance.to_dict()
# create an instance of StorageBundleList from a dict
storage_bundle_list_from_dict = StorageBundleList.from_dict(storage_bundle_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


