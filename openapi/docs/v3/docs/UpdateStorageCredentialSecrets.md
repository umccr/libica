# UpdateStorageCredentialSecrets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_credentials** | [**AwsCredentials**](AwsCredentials.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.update_storage_credential_secrets import UpdateStorageCredentialSecrets

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStorageCredentialSecrets from a JSON string
update_storage_credential_secrets_instance = UpdateStorageCredentialSecrets.from_json(json)
# print the JSON string representation of the object
print(UpdateStorageCredentialSecrets.to_json())

# convert the object into a dict
update_storage_credential_secrets_dict = update_storage_credential_secrets_instance.to_dict()
# create an instance of UpdateStorageCredentialSecrets from a dict
update_storage_credential_secrets_from_dict = UpdateStorageCredentialSecrets.from_dict(update_storage_credential_secrets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


