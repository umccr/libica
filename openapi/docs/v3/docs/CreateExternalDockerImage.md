# CreateExternalDockerImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.create_external_docker_image import CreateExternalDockerImage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalDockerImage from a JSON string
create_external_docker_image_instance = CreateExternalDockerImage.from_json(json)
# print the JSON string representation of the object
print(CreateExternalDockerImage.to_json())

# convert the object into a dict
create_external_docker_image_dict = create_external_docker_image_instance.to_dict()
# create an instance of CreateExternalDockerImage from a dict
create_external_docker_image_from_dict = CreateExternalDockerImage.from_dict(create_external_docker_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


