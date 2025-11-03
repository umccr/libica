# InternalDockerImageRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | [**RegionV4**](RegionV4.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.internal_docker_image_region import InternalDockerImageRegion

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDockerImageRegion from a JSON string
internal_docker_image_region_instance = InternalDockerImageRegion.from_json(json)
# print the JSON string representation of the object
print(InternalDockerImageRegion.to_json())

# convert the object into a dict
internal_docker_image_region_dict = internal_docker_image_region_instance.to_dict()
# create an instance of InternalDockerImageRegion from a dict
internal_docker_image_region_from_dict = InternalDockerImageRegion.from_dict(internal_docker_image_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


