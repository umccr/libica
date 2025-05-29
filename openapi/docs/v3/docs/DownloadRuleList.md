# DownloadRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DownloadRule]**](DownloadRule.md) |  | 

## Example

```python
from libica.openapi.v3.models.download_rule_list import DownloadRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRuleList from a JSON string
download_rule_list_instance = DownloadRuleList.from_json(json)
# print the JSON string representation of the object
print(DownloadRuleList.to_json())

# convert the object into a dict
download_rule_list_dict = download_rule_list_instance.to_dict()
# create an instance of DownloadRuleList from a dict
download_rule_list_from_dict = DownloadRuleList.from_dict(download_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


