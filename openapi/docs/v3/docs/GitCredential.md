# GitCredential


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
**git_url** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.git_credential import GitCredential

# TODO update the JSON string below
json = "{}"
# create an instance of GitCredential from a JSON string
git_credential_instance = GitCredential.from_json(json)
# print the JSON string representation of the object
print(GitCredential.to_json())

# convert the object into a dict
git_credential_dict = git_credential_instance.to_dict()
# create an instance of GitCredential from a dict
git_credential_from_dict = GitCredential.from_dict(git_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


