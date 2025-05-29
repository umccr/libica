# DataFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** | The code of the format. For example: FASTQ, BAM, ... | 
**description** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.data_format import DataFormat

# TODO update the JSON string below
json = "{}"
# create an instance of DataFormat from a JSON string
data_format_instance = DataFormat.from_json(json)
# print the JSON string representation of the object
print(DataFormat.to_json())

# convert the object into a dict
data_format_dict = data_format_instance.to_dict()
# create an instance of DataFormat from a dict
data_format_from_dict = DataFormat.from_dict(data_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


