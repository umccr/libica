# InlineView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A pre-signed url which is temporarily available for inline viewing the data. | 

## Example

```python
from libica.openapi.v3.models.inline_view import InlineView

# TODO update the JSON string below
json = "{}"
# create an instance of InlineView from a JSON string
inline_view_instance = InlineView.from_json(json)
# print the JSON string representation of the object
print(InlineView.to_json())

# convert the object into a dict
inline_view_dict = inline_view_instance.to_dict()
# create an instance of InlineView from a dict
inline_view_from_dict = InlineView.from_dict(inline_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


