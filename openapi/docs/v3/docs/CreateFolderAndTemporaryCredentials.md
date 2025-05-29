# CreateFolderAndTemporaryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new folder in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new folder in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**non_indexed** | **bool** | If you want to create a non-indexed folder. Only possible as a top-level folder, which means the folderId and folderPath attributes are not allowed. | [optional] [default to False]
**temporary_credentials** | [**CreateTemporaryCredentials**](CreateTemporaryCredentials.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.create_folder_and_temporary_credentials import CreateFolderAndTemporaryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderAndTemporaryCredentials from a JSON string
create_folder_and_temporary_credentials_instance = CreateFolderAndTemporaryCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateFolderAndTemporaryCredentials.to_json())

# convert the object into a dict
create_folder_and_temporary_credentials_dict = create_folder_and_temporary_credentials_instance.to_dict()
# create an instance of CreateFolderAndTemporaryCredentials from a dict
create_folder_and_temporary_credentials_from_dict = CreateFolderAndTemporaryCredentials.from_dict(create_folder_and_temporary_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


