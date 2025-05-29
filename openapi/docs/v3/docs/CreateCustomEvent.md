# CreateCustomEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The event code that should match a custom subscription. | 
**content** | **object** | The content that will be forwarded to the configured custom subscription destinations. | 

## Example

```python
from libica.openapi.v3.models.create_custom_event import CreateCustomEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomEvent from a JSON string
create_custom_event_instance = CreateCustomEvent.from_json(json)
# print the JSON string representation of the object
print(CreateCustomEvent.to_json())

# convert the object into a dict
create_custom_event_dict = create_custom_event_instance.to_dict()
# create an instance of CreateCustomEvent from a dict
create_custom_event_from_dict = CreateCustomEvent.from_dict(create_custom_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


