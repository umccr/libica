# DataUrlWithPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | The id of the file/folder as it was uploaded. | 
**data_urn** | **str** | The URN of this data. The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. | 
**data_path** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.data_url_with_path import DataUrlWithPath

# TODO update the JSON string below
json = "{}"
# create an instance of DataUrlWithPath from a JSON string
data_url_with_path_instance = DataUrlWithPath.from_json(json)
# print the JSON string representation of the object
print(DataUrlWithPath.to_json())

# convert the object into a dict
data_url_with_path_dict = data_url_with_path_instance.to_dict()
# create an instance of DataUrlWithPath from a dict
data_url_with_path_from_dict = DataUrlWithPath.from_dict(data_url_with_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


