# CreateStorageCredentialV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the credentials | 
**aws_credentials** | [**AwsCredentials**](AwsCredentials.md) |  | [optional] 
**type** | **str** | The type of the credentials | 

## Example

```python
from libica.openapi.v3.models.create_storage_credential_v3 import CreateStorageCredentialV3

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageCredentialV3 from a JSON string
create_storage_credential_v3_instance = CreateStorageCredentialV3.from_json(json)
# print the JSON string representation of the object
print(CreateStorageCredentialV3.to_json())

# convert the object into a dict
create_storage_credential_v3_dict = create_storage_credential_v3_instance.to_dict()
# create an instance of CreateStorageCredentialV3 from a dict
create_storage_credential_v3_from_dict = CreateStorageCredentialV3.from_dict(create_storage_credential_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


