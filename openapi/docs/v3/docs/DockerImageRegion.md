# DockerImageRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | [**RegionV4**](RegionV4.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.docker_image_region import DockerImageRegion

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImageRegion from a JSON string
docker_image_region_instance = DockerImageRegion.from_json(json)
# print the JSON string representation of the object
print(DockerImageRegion.to_json())

# convert the object into a dict
docker_image_region_dict = docker_image_region_instance.to_dict()
# create an instance of DockerImageRegion from a dict
docker_image_region_from_dict = DockerImageRegion.from_dict(docker_image_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


