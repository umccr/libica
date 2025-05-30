# ProjectDataAndTemporaryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | 
**project_id** | **str** |  | 
**temp_credentials** | [**TempCredentials**](TempCredentials.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_data_and_temporary_credentials import ProjectDataAndTemporaryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataAndTemporaryCredentials from a JSON string
project_data_and_temporary_credentials_instance = ProjectDataAndTemporaryCredentials.from_json(json)
# print the JSON string representation of the object
print(ProjectDataAndTemporaryCredentials.to_json())

# convert the object into a dict
project_data_and_temporary_credentials_dict = project_data_and_temporary_credentials_instance.to_dict()
# create an instance of ProjectDataAndTemporaryCredentials from a dict
project_data_and_temporary_credentials_from_dict = ProjectDataAndTemporaryCredentials.from_dict(project_data_and_temporary_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


