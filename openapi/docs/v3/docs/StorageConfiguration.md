# StorageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the storage configuration | 
**description** | **str** | An optional description | [optional] 
**type** | **str** |  | 
**status** | **str** |  | 
**error_message** | **str** | An optional error message when something went wrong with the configuration | [optional] 
**region** | [**Region**](Region.md) |  | 
**is_default** | **bool** | An indication if this is the default in region for new projects | 

## Example

```python
from libica.openapi.v3.models.storage_configuration import StorageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfiguration from a JSON string
storage_configuration_instance = StorageConfiguration.from_json(json)
# print the JSON string representation of the object
print(StorageConfiguration.to_json())

# convert the object into a dict
storage_configuration_dict = storage_configuration_instance.to_dict()
# create an instance of StorageConfiguration from a dict
storage_configuration_from_dict = StorageConfiguration.from_dict(storage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


