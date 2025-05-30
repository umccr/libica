# ActivationCodeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**allowed_slots** | **int** | The allowed slot within this code, -1 means unlimited | 
**used_slots** | **int** | Indicates how many slots can are used. | 
**moved_slots** | **int** | The slots that where moved to another activation code | 
**original_slots** | **int** | The assigned allowed slot within this code, -1 means unlimited | 
**pipeline_bundle** | [**PipelineBundle**](PipelineBundle.md) |  | 
**usages** | [**List[ActivationCodeDetailUsage]**](ActivationCodeDetailUsage.md) |  | 

## Example

```python
from libica.openapi.v3.models.activation_code_detail import ActivationCodeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeDetail from a JSON string
activation_code_detail_instance = ActivationCodeDetail.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeDetail.to_json())

# convert the object into a dict
activation_code_detail_dict = activation_code_detail_instance.to_dict()
# create an instance of ActivationCodeDetail from a dict
activation_code_detail_from_dict = ActivationCodeDetail.from_dict(activation_code_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


