# StorageCredentialV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**aws_role_session_name_prefix** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.storage_credential_v4 import StorageCredentialV4

# TODO update the JSON string below
json = "{}"
# create an instance of StorageCredentialV4 from a JSON string
storage_credential_v4_instance = StorageCredentialV4.from_json(json)
# print the JSON string representation of the object
print(StorageCredentialV4.to_json())

# convert the object into a dict
storage_credential_v4_dict = storage_credential_v4_instance.to_dict()
# create an instance of StorageCredentialV4 from a dict
storage_credential_v4_from_dict = StorageCredentialV4.from_dict(storage_credential_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


