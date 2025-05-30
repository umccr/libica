# StorageCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageCredential]**](StorageCredential.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_credential_list import StorageCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageCredentialList from a JSON string
storage_credential_list_instance = StorageCredentialList.from_json(json)
# print the JSON string representation of the object
print(StorageCredentialList.to_json())

# convert the object into a dict
storage_credential_list_dict = storage_credential_list_instance.to_dict()
# create an instance of StorageCredentialList from a dict
storage_credential_list_from_dict = StorageCredentialList.from_dict(storage_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


