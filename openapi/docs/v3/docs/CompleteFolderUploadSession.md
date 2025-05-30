# CompleteFolderUploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_expected_uploaded_files** | **int** | The number of expected uploaded files within this session. | 

## Example

```python
from libica.openapi.v3.models.complete_folder_upload_session import CompleteFolderUploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteFolderUploadSession from a JSON string
complete_folder_upload_session_instance = CompleteFolderUploadSession.from_json(json)
# print the JSON string representation of the object
print(CompleteFolderUploadSession.to_json())

# convert the object into a dict
complete_folder_upload_session_dict = complete_folder_upload_session_instance.to_dict()
# create an instance of CompleteFolderUploadSession from a dict
complete_folder_upload_session_from_dict = CompleteFolderUploadSession.from_dict(complete_folder_upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


