# StorageCredentialListV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageCredentialV4]**](StorageCredentialV4.md) |  | 

## Example

```python
from libica.openapi.v3.models.storage_credential_list_v4 import StorageCredentialListV4

# TODO update the JSON string below
json = "{}"
# create an instance of StorageCredentialListV4 from a JSON string
storage_credential_list_v4_instance = StorageCredentialListV4.from_json(json)
# print the JSON string representation of the object
print(StorageCredentialListV4.to_json())

# convert the object into a dict
storage_credential_list_v4_dict = storage_credential_list_v4_instance.to_dict()
# create an instance of StorageCredentialListV4 from a dict
storage_credential_list_v4_from_dict = StorageCredentialListV4.from_dict(storage_credential_list_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


