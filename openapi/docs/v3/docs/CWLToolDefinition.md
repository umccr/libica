# CWLToolDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | Name of the tool definition | 
**description** | **str** | Description of the tool definition | [optional] 
**status** | **str** | Status of the tool definition | 
**version_comment** | **str** | version comment of the tool definition | [optional] 
**release_version** | **int** | release version of the tool definition | [optional] 
**links** | [**Link**](Link.md) |  | [optional] 
**categories** | **List[Optional[str]]** | category tags as string array | [optional] 

## Example

```python
from libica.openapi.v3.models.cwl_tool_definition import CWLToolDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CWLToolDefinition from a JSON string
cwl_tool_definition_instance = CWLToolDefinition.from_json(json)
# print the JSON string representation of the object
print(CWLToolDefinition.to_json())

# convert the object into a dict
cwl_tool_definition_dict = cwl_tool_definition_instance.to_dict()
# create an instance of CWLToolDefinition from a dict
cwl_tool_definition_from_dict = CWLToolDefinition.from_dict(cwl_tool_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


