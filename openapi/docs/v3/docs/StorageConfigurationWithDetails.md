# StorageConfigurationWithDetails


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
**storage_configuration_details** | [**StorageConfigurationDetails**](StorageConfigurationDetails.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_configuration_with_details import StorageConfigurationWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfigurationWithDetails from a JSON string
storage_configuration_with_details_instance = StorageConfigurationWithDetails.from_json(json)
# print the JSON string representation of the object
print(StorageConfigurationWithDetails.to_json())

# convert the object into a dict
storage_configuration_with_details_dict = storage_configuration_with_details_instance.to_dict()
# create an instance of StorageConfigurationWithDetails from a dict
storage_configuration_with_details_from_dict = StorageConfigurationWithDetails.from_dict(storage_configuration_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


