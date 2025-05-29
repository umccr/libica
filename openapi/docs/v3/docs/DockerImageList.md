# DockerImageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DockerImage]**](DockerImage.md) |  | 

## Example

```python
from libica.openapi.v3.models.docker_image_list import DockerImageList

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImageList from a JSON string
docker_image_list_instance = DockerImageList.from_json(json)
# print the JSON string representation of the object
print(DockerImageList.to_json())

# convert the object into a dict
docker_image_list_dict = docker_image_list_instance.to_dict()
# create an instance of DockerImageList from a dict
docker_image_list_from_dict = DockerImageList.from_dict(docker_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


