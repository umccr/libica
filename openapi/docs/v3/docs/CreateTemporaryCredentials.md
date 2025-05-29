# CreateTemporaryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials_format** | **str** | The format in which temporary credentials have to be returned. If not provided, temporary credentials will be returned in a cloud specific format. | [optional] 
**read_only_credentials** | **bool** | The temporary credentials will be read-only. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_temporary_credentials import CreateTemporaryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemporaryCredentials from a JSON string
create_temporary_credentials_instance = CreateTemporaryCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateTemporaryCredentials.to_json())

# convert the object into a dict
create_temporary_credentials_dict = create_temporary_credentials_instance.to_dict()
# create an instance of CreateTemporaryCredentials from a dict
create_temporary_credentials_from_dict = CreateTemporaryCredentials.from_dict(create_temporary_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


