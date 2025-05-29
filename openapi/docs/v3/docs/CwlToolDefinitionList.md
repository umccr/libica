# CwlToolDefinitionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CWLToolDefinition]**](CWLToolDefinition.md) |  | 

## Example

```python
from libica.openapi.v3.models.cwl_tool_definition_list import CwlToolDefinitionList

# TODO update the JSON string below
json = "{}"
# create an instance of CwlToolDefinitionList from a JSON string
cwl_tool_definition_list_instance = CwlToolDefinitionList.from_json(json)
# print the JSON string representation of the object
print(CwlToolDefinitionList.to_json())

# convert the object into a dict
cwl_tool_definition_list_dict = cwl_tool_definition_list_instance.to_dict()
# create an instance of CwlToolDefinitionList from a dict
cwl_tool_definition_list_from_dict = CwlToolDefinitionList.from_dict(cwl_tool_definition_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


