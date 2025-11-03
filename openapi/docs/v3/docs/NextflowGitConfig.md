# NextflowGitConfig


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
from libica.openapi.v3.models.nextflow_git_config import NextflowGitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NextflowGitConfig from a JSON string
nextflow_git_config_instance = NextflowGitConfig.from_json(json)
# print the JSON string representation of the object
print(NextflowGitConfig.to_json())

# convert the object into a dict
nextflow_git_config_dict = nextflow_git_config_instance.to_dict()
# create an instance of NextflowGitConfig from a dict
nextflow_git_config_from_dict = NextflowGitConfig.from_dict(nextflow_git_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


