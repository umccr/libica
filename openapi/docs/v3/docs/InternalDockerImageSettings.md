# InternalDockerImageSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[DockerImageRegion]**](DockerImageRegion.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.internal_docker_image_settings import InternalDockerImageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDockerImageSettings from a JSON string
internal_docker_image_settings_instance = InternalDockerImageSettings.from_json(json)
# print the JSON string representation of the object
print(InternalDockerImageSettings.to_json())

# convert the object into a dict
internal_docker_image_settings_dict = internal_docker_image_settings_instance.to_dict()
# create an instance of InternalDockerImageSettings from a dict
internal_docker_image_settings_from_dict = InternalDockerImageSettings.from_dict(internal_docker_image_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


