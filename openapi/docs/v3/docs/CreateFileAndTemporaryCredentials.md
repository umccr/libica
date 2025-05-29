# CreateFileAndTemporaryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new file in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new file in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**format_code** | **str** | The code of the format you would like to assign at creation time. If not specified, auto format assignment will be done. | [optional] 
**temporary_credentials** | [**CreateTemporaryCredentials**](CreateTemporaryCredentials.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.create_file_and_temporary_credentials import CreateFileAndTemporaryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileAndTemporaryCredentials from a JSON string
create_file_and_temporary_credentials_instance = CreateFileAndTemporaryCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateFileAndTemporaryCredentials.to_json())

# convert the object into a dict
create_file_and_temporary_credentials_dict = create_file_and_temporary_credentials_instance.to_dict()
# create an instance of CreateFileAndTemporaryCredentials from a dict
create_file_and_temporary_credentials_from_dict = CreateFileAndTemporaryCredentials.from_dict(create_file_and_temporary_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


