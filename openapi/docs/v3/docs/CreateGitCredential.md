# CreateGitCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the credentials | 
**git_user_name** | **str** | The git username | 
**personal_accesstoken** | **str** | The personal access token | 

## Example

```python
from libica.openapi.v3.models.create_git_credential import CreateGitCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGitCredential from a JSON string
create_git_credential_instance = CreateGitCredential.from_json(json)
# print the JSON string representation of the object
print(CreateGitCredential.to_json())

# convert the object into a dict
create_git_credential_dict = create_git_credential_instance.to_dict()
# create an instance of CreateGitCredential from a dict
create_git_credential_from_dict = CreateGitCredential.from_dict(create_git_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


