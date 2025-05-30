# DataTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[Optional[str]]** |  | [optional] 
**user_tags** | **List[Optional[str]]** |  | [optional] 
**connector_tags** | **List[Optional[str]]** |  | [optional] 
**run_in_tags** | **List[Optional[str]]** |  | [optional] 
**run_out_tags** | **List[Optional[str]]** |  | [optional] 
**reference_tags** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.data_tag import DataTag

# TODO update the JSON string below
json = "{}"
# create an instance of DataTag from a JSON string
data_tag_instance = DataTag.from_json(json)
# print the JSON string representation of the object
print(DataTag.to_json())

# convert the object into a dict
data_tag_dict = data_tag_instance.to_dict()
# create an instance of DataTag from a dict
data_tag_from_dict = DataTag.from_dict(data_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


