# DownloadRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** |  | 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**sequence** | **int** | Defines the order of the rule. | 
**format_code** | **str** | Regular expression to select which format this rule applies to. | [optional] 
**project_name** | **str** | Regular expression to select which project this rule applies to. | [optional] 
**target_local_folder** | **str** | The local folder where to write the data. | 
**file_name_expression** | **str** | Will allow the filename to be modified including a set of variables | [optional] 

## Example

```python
from libica.openapi.v3.models.download_rule import DownloadRule

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRule from a JSON string
download_rule_instance = DownloadRule.from_json(json)
# print the JSON string representation of the object
print(DownloadRule.to_json())

# convert the object into a dict
download_rule_dict = download_rule_instance.to_dict()
# create an instance of DownloadRule from a dict
download_rule_from_dict = DownloadRule.from_dict(download_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


