# CwlGitConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | URL to the repository | 
**git_credential_id** | **str** | Id the of the git credential | [optional] 
**main_file_path** | **str** | Path of the main file | 
**commit_id** | **str** | Id the of the git commit | 

## Example

```python
from libica.openapi.v3.models.cwl_git_config import CwlGitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CwlGitConfig from a JSON string
cwl_git_config_instance = CwlGitConfig.from_json(json)
# print the JSON string representation of the object
print(CwlGitConfig.to_json())

# convert the object into a dict
cwl_git_config_dict = cwl_git_config_instance.to_dict()
# create an instance of CwlGitConfig from a dict
cwl_git_config_from_dict = CwlGitConfig.from_dict(cwl_git_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


