# ExternalDockerImageSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.external_docker_image_settings import ExternalDockerImageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDockerImageSettings from a JSON string
external_docker_image_settings_instance = ExternalDockerImageSettings.from_json(json)
# print the JSON string representation of the object
print(ExternalDockerImageSettings.to_json())

# convert the object into a dict
external_docker_image_settings_dict = external_docker_image_settings_instance.to_dict()
# create an instance of ExternalDockerImageSettings from a dict
external_docker_image_settings_from_dict = ExternalDockerImageSettings.from_dict(external_docker_image_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


