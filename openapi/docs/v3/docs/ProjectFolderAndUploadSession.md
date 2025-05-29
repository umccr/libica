# ProjectFolderAndUploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | 
**project_id** | **str** |  | 
**upload_session** | [**FolderUploadSession**](FolderUploadSession.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_folder_and_upload_session import ProjectFolderAndUploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFolderAndUploadSession from a JSON string
project_folder_and_upload_session_instance = ProjectFolderAndUploadSession.from_json(json)
# print the JSON string representation of the object
print(ProjectFolderAndUploadSession.to_json())

# convert the object into a dict
project_folder_and_upload_session_dict = project_folder_and_upload_session_instance.to_dict()
# create an instance of ProjectFolderAndUploadSession from a dict
project_folder_and_upload_session_from_dict = ProjectFolderAndUploadSession.from_dict(project_folder_and_upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


