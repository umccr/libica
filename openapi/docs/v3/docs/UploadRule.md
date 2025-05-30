# UploadRule


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
**local_folder** | **str** | The local folder to monitor. Files in this folder on your local environment will be uploaded to the specified project. Only files matching the filePattern will be uploaded. | 
**file_pattern** | **str** | The regular expression to match a file name. eg: to match all files use &#39;.*&#39; | 
**data_format** | [**DataFormat**](DataFormat.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from libica.openapi.v3.models.upload_rule import UploadRule

# TODO update the JSON string below
json = "{}"
# create an instance of UploadRule from a JSON string
upload_rule_instance = UploadRule.from_json(json)
# print the JSON string representation of the object
print(UploadRule.to_json())

# convert the object into a dict
upload_rule_dict = upload_rule_instance.to_dict()
# create an instance of UploadRule from a dict
upload_rule_from_dict = UploadRule.from_dict(upload_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


