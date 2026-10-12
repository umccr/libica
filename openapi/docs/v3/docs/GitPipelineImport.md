# GitPipelineImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | URL to the repository | 
**git_credential_id** | **str** | Id of the git credential | [optional] 
**main_file_path** | **str** | Path of the main file | [optional] 
**commit_id** | **str** | Id of the git commit | 
**config_file_path** | **str** | Path of the config file | [optional] 
**schema_file_path** | **str** | Path of the schema file | [optional] 

## Example

```python
from libica.openapi.v3.models.git_pipeline_import import GitPipelineImport

# TODO update the JSON string below
json = "{}"
# create an instance of GitPipelineImport from a JSON string
git_pipeline_import_instance = GitPipelineImport.from_json(json)
# print the JSON string representation of the object
print(GitPipelineImport.to_json())

# convert the object into a dict
git_pipeline_import_dict = git_pipeline_import_instance.to_dict()
# create an instance of GitPipelineImport from a dict
git_pipeline_import_from_dict = GitPipelineImport.from_dict(git_pipeline_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


