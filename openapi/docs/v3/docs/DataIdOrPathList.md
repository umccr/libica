# DataIdOrPathList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ids** | **List[str]** |  | [optional] 
**data_paths** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.data_id_or_path_list import DataIdOrPathList

# TODO update the JSON string below
json = "{}"
# create an instance of DataIdOrPathList from a JSON string
data_id_or_path_list_instance = DataIdOrPathList.from_json(json)
# print the JSON string representation of the object
print(DataIdOrPathList.to_json())

# convert the object into a dict
data_id_or_path_list_dict = data_id_or_path_list_instance.to_dict()
# create an instance of DataIdOrPathList from a dict
data_id_or_path_list_from_dict = DataIdOrPathList.from_dict(data_id_or_path_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


