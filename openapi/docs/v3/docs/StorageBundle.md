# StorageBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**bundle_name** | **str** | The name of the storage bundle | 
**entitlement_name** | **str** | The name of the parent entitlement | 
**region** | [**Region**](Region.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_bundle import StorageBundle

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBundle from a JSON string
storage_bundle_instance = StorageBundle.from_json(json)
# print the JSON string representation of the object
print(StorageBundle.to_json())

# convert the object into a dict
storage_bundle_dict = storage_bundle_instance.to_dict()
# create an instance of StorageBundle from a dict
storage_bundle_from_dict = StorageBundle.from_dict(storage_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


