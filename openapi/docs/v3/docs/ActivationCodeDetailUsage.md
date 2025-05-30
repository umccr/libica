# ActivationCodeDetailUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**used_slots** | **int** | Indicates how many slots can are used, -1 means unused | 
**allowed_slots** | **int** | Indicates how many slots can be used, -1 means unlimited | 

## Example

```python
from libica.openapi.v3.models.activation_code_detail_usage import ActivationCodeDetailUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeDetailUsage from a JSON string
activation_code_detail_usage_instance = ActivationCodeDetailUsage.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeDetailUsage.to_json())

# convert the object into a dict
activation_code_detail_usage_dict = activation_code_detail_usage_instance.to_dict()
# create an instance of ActivationCodeDetailUsage from a dict
activation_code_detail_usage_from_dict = ActivationCodeDetailUsage.from_dict(activation_code_detail_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


