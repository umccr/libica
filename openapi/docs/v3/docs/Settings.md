# Settings

This object contains a \"anyOf\" construct. Depending on which type, you will receive a StringSettings-, IntegerSettings or OptionsSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | **List[str]** |  | [optional] 
**options** | **List[str]** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print(Settings.to_json())

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_from_dict = Settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


