# OptionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **List[str]** |  | [optional] 
**default_values** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.option_settings import OptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OptionSettings from a JSON string
option_settings_instance = OptionSettings.from_json(json)
# print the JSON string representation of the object
print(OptionSettings.to_json())

# convert the object into a dict
option_settings_dict = option_settings_instance.to_dict()
# create an instance of OptionSettings from a dict
option_settings_from_dict = OptionSettings.from_dict(option_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


