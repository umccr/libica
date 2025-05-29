# CreateFileAndUploadUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new file in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new file in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**format_code** | **str** | The code of the format you would like to assign at creation time. If not specified, auto format assignment will be done. | [optional] 
**file_type** | **str** | The expected content type for the upload, to include in the upload url. | [optional] 
**hash** | **str** | The expected md5 hash for the upload content, to include in the upload url. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_file_and_upload_url import CreateFileAndUploadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileAndUploadUrl from a JSON string
create_file_and_upload_url_instance = CreateFileAndUploadUrl.from_json(json)
# print the JSON string representation of the object
print(CreateFileAndUploadUrl.to_json())

# convert the object into a dict
create_file_and_upload_url_dict = create_file_and_upload_url_instance.to_dict()
# create an instance of CreateFileAndUploadUrl from a dict
create_file_and_upload_url_from_dict = CreateFileAndUploadUrl.from_dict(create_file_and_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


