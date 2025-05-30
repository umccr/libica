# StorageConfigurationWithDetailsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageConfigurationWithDetails]**](StorageConfigurationWithDetails.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_configuration_with_details_list import StorageConfigurationWithDetailsList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfigurationWithDetailsList from a JSON string
storage_configuration_with_details_list_instance = StorageConfigurationWithDetailsList.from_json(json)
# print the JSON string representation of the object
print(StorageConfigurationWithDetailsList.to_json())

# convert the object into a dict
storage_configuration_with_details_list_dict = storage_configuration_with_details_list_instance.to_dict()
# create an instance of StorageConfigurationWithDetailsList from a dict
storage_configuration_with_details_list_from_dict = StorageConfigurationWithDetailsList.from_dict(storage_configuration_with_details_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


