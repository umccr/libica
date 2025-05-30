# CreateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file/folder as how it will be created. | 
**folder_id** | **str** | The id of the folder you want to create this new data in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folder_path** | **str** | The absolute path of the folder you want to create this new data in which must end with &#39;/&#39;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**format_code** | **str** | The code of the format you would like to assign at creation time. This is only allowed for file data. If not specified, auto format assignment will be done. | [optional] 
**data_type** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.create_data import CreateData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateData from a JSON string
create_data_instance = CreateData.from_json(json)
# print the JSON string representation of the object
print(CreateData.to_json())

# convert the object into a dict
create_data_dict = create_data_instance.to_dict()
# create an instance of CreateData from a dict
create_data_from_dict = CreateData.from_dict(create_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


