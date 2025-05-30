# BundleTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwl_tool_definition** | [**CWLToolDefinition**](CWLToolDefinition.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_tool import BundleTool

# TODO update the JSON string below
json = "{}"
# create an instance of BundleTool from a JSON string
bundle_tool_instance = BundleTool.from_json(json)
# print the JSON string representation of the object
print(BundleTool.to_json())

# convert the object into a dict
bundle_tool_dict = bundle_tool_instance.to_dict()
# create an instance of BundleTool from a dict
bundle_tool_from_dict = BundleTool.from_dict(bundle_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


