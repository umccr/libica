# IlmnRepoDockerImageSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_url** | **str** |  | 
**regions** | [**List[IlmnRepoDockerImageRegion]**](IlmnRepoDockerImageRegion.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.ilmn_repo_docker_image_settings import IlmnRepoDockerImageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of IlmnRepoDockerImageSettings from a JSON string
ilmn_repo_docker_image_settings_instance = IlmnRepoDockerImageSettings.from_json(json)
# print the JSON string representation of the object
print(IlmnRepoDockerImageSettings.to_json())

# convert the object into a dict
ilmn_repo_docker_image_settings_dict = ilmn_repo_docker_image_settings_instance.to_dict()
# create an instance of IlmnRepoDockerImageSettings from a dict
ilmn_repo_docker_image_settings_from_dict = IlmnRepoDockerImageSettings.from_dict(ilmn_repo_docker_image_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


