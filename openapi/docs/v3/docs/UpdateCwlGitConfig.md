# UpdateCwlGitConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | URL to the repository | 
**git_credential_id** | **str** | Id the of the git credential | [optional] 
**main_file_path** | **str** | Path of the main file | 
**commit_id** | **str** | Id the of the git commit | 

## Example

```python
from libica.openapi.v3.models.update_cwl_git_config import UpdateCwlGitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCwlGitConfig from a JSON string
update_cwl_git_config_instance = UpdateCwlGitConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateCwlGitConfig.to_json())

# convert the object into a dict
update_cwl_git_config_dict = update_cwl_git_config_instance.to_dict()
# create an instance of UpdateCwlGitConfig from a dict
update_cwl_git_config_from_dict = UpdateCwlGitConfig.from_dict(update_cwl_git_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


