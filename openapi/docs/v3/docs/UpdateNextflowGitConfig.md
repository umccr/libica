# UpdateNextflowGitConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | URL to the repository | 
**git_credential_id** | **str** | Id the of the git credential | [optional] 
**main_file_path** | **str** | Path of the main file | 
**commit_id** | **str** | Id the of the git commit | 
**config_file_path** | **str** | Path of the config file | [optional] 

## Example

```python
from libica.openapi.v3.models.update_nextflow_git_config import UpdateNextflowGitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNextflowGitConfig from a JSON string
update_nextflow_git_config_instance = UpdateNextflowGitConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateNextflowGitConfig.to_json())

# convert the object into a dict
update_nextflow_git_config_dict = update_nextflow_git_config_instance.to_dict()
# create an instance of UpdateNextflowGitConfig from a dict
update_nextflow_git_config_from_dict = UpdateNextflowGitConfig.from_dict(update_nextflow_git_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


