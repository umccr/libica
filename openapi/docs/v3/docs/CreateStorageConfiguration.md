# CreateStorageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | 
**description** | **str** | An optional description | [optional] 
**storage_credential_id** | **str** | The id of the storage credential | 
**type** | **str** | The type of configuration | 
**aws_details** | [**AWSDetails**](AWSDetails.md) |  | [optional] 
**region_id** | **str** | The id of the region where the bucket will be located | 

## Example

```python
from libica.openapi.v3.models.create_storage_configuration import CreateStorageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageConfiguration from a JSON string
create_storage_configuration_instance = CreateStorageConfiguration.from_json(json)
# print the JSON string representation of the object
print(CreateStorageConfiguration.to_json())

# convert the object into a dict
create_storage_configuration_dict = create_storage_configuration_instance.to_dict()
# create an instance of CreateStorageConfiguration from a dict
create_storage_configuration_from_dict = CreateStorageConfiguration.from_dict(create_storage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


