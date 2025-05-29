# CreateFileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new file in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new file in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**format_code** | **str** | The code of the format you would like to assign at creation time. If not specified, auto format assignment will be done. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_file_data import CreateFileData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileData from a JSON string
create_file_data_instance = CreateFileData.from_json(json)
# print the JSON string representation of the object
print(CreateFileData.to_json())

# convert the object into a dict
create_file_data_dict = create_file_data_instance.to_dict()
# create an instance of CreateFileData from a dict
create_file_data_from_dict = CreateFileData.from_dict(create_file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


