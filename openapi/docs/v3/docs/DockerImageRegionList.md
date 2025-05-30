# DockerImageRegionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_ids** | **List[str]** |  | 

## Example

```python
from libica.openapi.v3.models.docker_image_region_list import DockerImageRegionList

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImageRegionList from a JSON string
docker_image_region_list_instance = DockerImageRegionList.from_json(json)
# print the JSON string representation of the object
print(DockerImageRegionList.to_json())

# convert the object into a dict
docker_image_region_list_dict = docker_image_region_list_instance.to_dict()
# create an instance of DockerImageRegionList from a dict
docker_image_region_list_from_dict = DockerImageRegionList.from_dict(docker_image_region_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


