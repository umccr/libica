# DockerImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | 
**type** | **str** |  | 
**internal_docker_image_settings** | [**InternalDockerImageSettings**](InternalDockerImageSettings.md) |  | [optional] 
**external_docker_image_settings** | [**ExternalDockerImageSettings**](ExternalDockerImageSettings.md) |  | [optional] 
**bench_settings** | [**BenchSettings**](BenchSettings.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.docker_image import DockerImage

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImage from a JSON string
docker_image_instance = DockerImage.from_json(json)
# print the JSON string representation of the object
print(DockerImage.to_json())

# convert the object into a dict
docker_image_dict = docker_image_instance.to_dict()
# create an instance of DockerImage from a dict
docker_image_from_dict = DockerImage.from_dict(docker_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


