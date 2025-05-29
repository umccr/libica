# StringSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.string_settings import StringSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StringSettings from a JSON string
string_settings_instance = StringSettings.from_json(json)
# print the JSON string representation of the object
print(StringSettings.to_json())

# convert the object into a dict
string_settings_dict = string_settings_instance.to_dict()
# create an instance of StringSettings from a dict
string_settings_from_dict = StringSettings.from_dict(string_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


