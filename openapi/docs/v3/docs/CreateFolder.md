# CreateFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new folder in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new folder in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_folder import CreateFolder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder from a JSON string
create_folder_instance = CreateFolder.from_json(json)
# print the JSON string representation of the object
print(CreateFolder.to_json())

# convert the object into a dict
create_folder_dict = create_folder_instance.to_dict()
# create an instance of CreateFolder from a dict
create_folder_from_dict = CreateFolder.from_dict(create_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


