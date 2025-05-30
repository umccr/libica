# Download


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A pre-signed url which is temporarily available for downloading the data. | 

## Example

```python
from libica.openapi.v3.models.download import Download

# TODO update the JSON string below
json = "{}"
# create an instance of Download from a JSON string
download_instance = Download.from_json(json)
# print the JSON string representation of the object
print(Download.to_json())

# convert the object into a dict
download_dict = download_instance.to_dict()
# create an instance of Download from a dict
download_from_dict = Download.from_dict(download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


