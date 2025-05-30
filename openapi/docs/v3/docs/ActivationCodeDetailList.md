# ActivationCodeDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ActivationCodeDetail]**](ActivationCodeDetail.md) |  | 

## Example

```python
from libica.openapi.v3.models.activation_code_detail_list import ActivationCodeDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationCodeDetailList from a JSON string
activation_code_detail_list_instance = ActivationCodeDetailList.from_json(json)
# print the JSON string representation of the object
print(ActivationCodeDetailList.to_json())

# convert the object into a dict
activation_code_detail_list_dict = activation_code_detail_list_instance.to_dict()
# create an instance of ActivationCodeDetailList from a dict
activation_code_detail_list_from_dict = ActivationCodeDetailList.from_dict(activation_code_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


