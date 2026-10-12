# CreateStorageCredentialV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the credentials | 
**aws_credentials** | [**AwsCredentials**](AwsCredentials.md) |  | [optional] 
**type** | **str** | The type of the credentials. Allowed values : AWS_USER, AWS_ROLE. | 

## Example

```python
from libica.openapi.v3.models.create_storage_credential_v4 import CreateStorageCredentialV4

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageCredentialV4 from a JSON string
create_storage_credential_v4_instance = CreateStorageCredentialV4.from_json(json)
# print the JSON string representation of the object
print(CreateStorageCredentialV4.to_json())

# convert the object into a dict
create_storage_credential_v4_dict = create_storage_credential_v4_instance.to_dict()
# create an instance of CreateStorageCredentialV4 from a dict
create_storage_credential_v4_from_dict = CreateStorageCredentialV4.from_dict(create_storage_credential_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


