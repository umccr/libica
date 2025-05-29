# ProjectFileAndUploadUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | 
**project_id** | **str** |  | 
**upload_url** | **str** | A pre-signed url which is temporarily available for uploading the data. | 

## Example

```python
from libica.openapi.v3.models.project_file_and_upload_url import ProjectFileAndUploadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFileAndUploadUrl from a JSON string
project_file_and_upload_url_instance = ProjectFileAndUploadUrl.from_json(json)
# print the JSON string representation of the object
print(ProjectFileAndUploadUrl.to_json())

# convert the object into a dict
project_file_and_upload_url_dict = project_file_and_upload_url_instance.to_dict()
# create an instance of ProjectFileAndUploadUrl from a dict
project_file_and_upload_url_from_dict = ProjectFileAndUploadUrl.from_dict(project_file_and_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


