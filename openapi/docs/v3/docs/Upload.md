# Upload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A pre-signed url which is temporarily available for uploading the data. | 

## Example

```python
from libica.openapi.v3.models.upload import Upload

# TODO update the JSON string below
json = "{}"
# create an instance of Upload from a JSON string
upload_instance = Upload.from_json(json)
# print the JSON string representation of the object
print(Upload.to_json())

# convert the object into a dict
upload_dict = upload_instance.to_dict()
# create an instance of Upload from a dict
upload_from_dict = Upload.from_dict(upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


