# FolderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_indexed** | **bool** | Indicates this is a non-indexed folder | 

## Example

```python
from libica.openapi.v3.models.folder_details import FolderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FolderDetails from a JSON string
folder_details_instance = FolderDetails.from_json(json)
# print the JSON string representation of the object
print(FolderDetails.to_json())

# convert the object into a dict
folder_details_dict = folder_details_instance.to_dict()
# create an instance of FolderDetails from a dict
folder_details_from_dict = FolderDetails.from_dict(folder_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


