# StorageConfigurationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_s3** | [**AWSDetails**](AWSDetails.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.storage_configuration_details import StorageConfigurationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfigurationDetails from a JSON string
storage_configuration_details_instance = StorageConfigurationDetails.from_json(json)
# print the JSON string representation of the object
print(StorageConfigurationDetails.to_json())

# convert the object into a dict
storage_configuration_details_dict = storage_configuration_details_instance.to_dict()
# create an instance of StorageConfigurationDetails from a dict
storage_configuration_details_from_dict = StorageConfigurationDetails.from_dict(storage_configuration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


