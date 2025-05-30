# CreateUploadRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**local_folder** | **str** | The local folder to monitor. Files in this folder on your local environment will be uploaded to the specified project. Only files matching the filePattern will be uploaded. | 
**file_pattern** | **str** | The regular expression to match a file name. eg: to match all files use &#39;.*&#39; | 
**data_format_id** | **str** | The format which will be assigned to the uploaded data. If not specified, an auto-detection of the format will be done. | [optional] 
**project_id** | **str** | The project to which the data will be uploaded. | 

## Example

```python
from libica.openapi.v3.models.create_upload_rule import CreateUploadRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUploadRule from a JSON string
create_upload_rule_instance = CreateUploadRule.from_json(json)
# print the JSON string representation of the object
print(CreateUploadRule.to_json())

# convert the object into a dict
create_upload_rule_dict = create_upload_rule_instance.to_dict()
# create an instance of CreateUploadRule from a dict
create_upload_rule_from_dict = CreateUploadRule.from_dict(create_upload_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


