# UpdateGitCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_user_name** | **str** | The git username | 
**personal_accesstoken** | **str** | The personal access token | 

## Example

```python
from libica.openapi.v3.models.update_git_credential import UpdateGitCredential

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGitCredential from a JSON string
update_git_credential_instance = UpdateGitCredential.from_json(json)
# print the JSON string representation of the object
print(UpdateGitCredential.to_json())

# convert the object into a dict
update_git_credential_dict = update_git_credential_instance.to_dict()
# create an instance of UpdateGitCredential from a dict
update_git_credential_from_dict = UpdateGitCredential.from_dict(update_git_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


