# UploadRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UploadRule]**](UploadRule.md) |  | 

## Example

```python
from libica.openapi.v3.models.upload_rule_list import UploadRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of UploadRuleList from a JSON string
upload_rule_list_instance = UploadRuleList.from_json(json)
# print the JSON string representation of the object
print(UploadRuleList.to_json())

# convert the object into a dict
upload_rule_list_dict = upload_rule_list_instance.to_dict()
# create an instance of UploadRuleList from a dict
upload_rule_list_from_dict = UploadRuleList.from_dict(upload_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


