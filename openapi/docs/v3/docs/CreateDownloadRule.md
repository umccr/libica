# CreateDownloadRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**sequence** | **int** | Defines the order of the rule. | 
**format_code** | **str** | Regular expression to filter which format this rule applies to. | [optional] 
**project_name** | **str** | Regular expression to filter which project this rule applies to. | [optional] 
**target_local_folder** | **str** | The local folder where to write the data. | 
**file_name_expression** | **str** | Will allow the filename to be modified including a set of variables | [optional] 

## Example

```python
from libica.openapi.v3.models.create_download_rule import CreateDownloadRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDownloadRule from a JSON string
create_download_rule_instance = CreateDownloadRule.from_json(json)
# print the JSON string representation of the object
print(CreateDownloadRule.to_json())

# convert the object into a dict
create_download_rule_dict = create_download_rule_instance.to_dict()
# create an instance of CreateDownloadRule from a dict
create_download_rule_from_dict = CreateDownloadRule.from_dict(create_download_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


