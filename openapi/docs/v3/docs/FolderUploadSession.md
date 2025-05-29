# FolderUploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the folder upload session. | 
**time_created** | **datetime** | The time the folder upload session was created. | 
**status** | **str** | The status of the folder upload session. | 
**time_session_expires** | **datetime** | The time the folder upload session will expire as it is only temporarily valid. | 
**time_completed** | **datetime** | The time the folder upload session completed. | [optional] 
**time_closed** | **datetime** | The time the folder upload session was closed. | [optional] 
**temp_credentials** | [**TempCredentials**](TempCredentials.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.folder_upload_session import FolderUploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUploadSession from a JSON string
folder_upload_session_instance = FolderUploadSession.from_json(json)
# print the JSON string representation of the object
print(FolderUploadSession.to_json())

# convert the object into a dict
folder_upload_session_dict = folder_upload_session_instance.to_dict()
# create an instance of FolderUploadSession from a dict
folder_upload_session_from_dict = FolderUploadSession.from_dict(folder_upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


