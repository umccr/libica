# RegionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Region]**](Region.md) |  | 

## Example

```python
from libica.openapi.v3.models.region_list import RegionList

# TODO update the JSON string below
json = "{}"
# create an instance of RegionList from a JSON string
region_list_instance = RegionList.from_json(json)
# print the JSON string representation of the object
print(RegionList.to_json())

# convert the object into a dict
region_list_dict = region_list_instance.to_dict()
# create an instance of RegionList from a dict
region_list_from_dict = RegionList.from_dict(region_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


