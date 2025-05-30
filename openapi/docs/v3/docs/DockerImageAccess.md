# DockerImageAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web** | **bool** |  | 
**console** | **bool** |  | 

## Example

```python
from libica.openapi.v3.models.docker_image_access import DockerImageAccess

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImageAccess from a JSON string
docker_image_access_instance = DockerImageAccess.from_json(json)
# print the JSON string representation of the object
print(DockerImageAccess.to_json())

# convert the object into a dict
docker_image_access_dict = docker_image_access_instance.to_dict()
# create an instance of DockerImageAccess from a dict
docker_image_access_from_dict = DockerImageAccess.from_dict(docker_image_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


