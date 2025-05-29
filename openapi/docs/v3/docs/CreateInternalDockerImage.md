# CreateInternalDockerImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_data_id** | **str** | The id of the data for which an Docker image will be created. | 
**docker_data_project_id** | **str** | The id of the project where the Docker data resides. | 
**name** | **str** |  | 
**version** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**regions** | **List[str]** | The UUID of the regions where the Docker image will be made available. | 

## Example

```python
from libica.openapi.v3.models.create_internal_docker_image import CreateInternalDockerImage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalDockerImage from a JSON string
create_internal_docker_image_instance = CreateInternalDockerImage.from_json(json)
# print the JSON string representation of the object
print(CreateInternalDockerImage.to_json())

# convert the object into a dict
create_internal_docker_image_dict = create_internal_docker_image_instance.to_dict()
# create an instance of CreateInternalDockerImage from a dict
create_internal_docker_image_from_dict = CreateInternalDockerImage.from_dict(create_internal_docker_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


