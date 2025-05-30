# RcloneTempCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, str]** | The config in key value format. | 
**file_path_prefix** | **str** | The prefix of the file path. | 
**storage_type** | **str** | The type of the object storage. | 
**expiration_time** | **str** | The timestamp when the credentials expire. | 
**upload_session_id** | **str** | The folder upload session id which can be used after upload to complete the upload session. | [optional] 

## Example

```python
from libica.openapi.v3.models.rclone_temp_credentials import RcloneTempCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of RcloneTempCredentials from a JSON string
rclone_temp_credentials_instance = RcloneTempCredentials.from_json(json)
# print the JSON string representation of the object
print(RcloneTempCredentials.to_json())

# convert the object into a dict
rclone_temp_credentials_dict = rclone_temp_credentials_instance.to_dict()
# create an instance of RcloneTempCredentials from a dict
rclone_temp_credentials_from_dict = RcloneTempCredentials.from_dict(rclone_temp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


