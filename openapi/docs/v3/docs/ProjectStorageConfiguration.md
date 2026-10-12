# ProjectStorageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_configuration_sub_folder** | **str** | The location of the self managed storage | 
**storage_configuration** | [**StorageConfiguration**](StorageConfiguration.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_storage_configuration import ProjectStorageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStorageConfiguration from a JSON string
project_storage_configuration_instance = ProjectStorageConfiguration.from_json(json)
# print the JSON string representation of the object
print(ProjectStorageConfiguration.to_json())

# convert the object into a dict
project_storage_configuration_dict = project_storage_configuration_instance.to_dict()
# create an instance of ProjectStorageConfiguration from a dict
project_storage_configuration_from_dict = ProjectStorageConfiguration.from_dict(project_storage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


