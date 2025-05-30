# Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the file/folder as it was uploaded. | 
**urn** | **str** | The URN of this data. The format is urn:ilmn:ica:region:\\&lt;ID of the region\\&gt;:data:\\&lt;ID of the data\\&gt;#\\&lt;optional data path\\&gt;. The path can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**details** | [**DataDetails**](DataDetails.md) |  | [optional] 
**folder_details** | [**FolderDetails**](FolderDetails.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


