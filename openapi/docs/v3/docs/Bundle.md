# Bundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** |  | 
**short_description** | **str** |  | [optional] 
**region** | [**Region**](Region.md) |  | 
**metadata_model** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**release_version** | **str** |  | 
**version_comment** | **str** |  | [optional] 
**status** | **str** |  | 
**categories** | **List[Optional[str]]** | category tags as string array | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.bundle import Bundle

# TODO update the JSON string below
json = "{}"
# create an instance of Bundle from a JSON string
bundle_instance = Bundle.from_json(json)
# print the JSON string representation of the object
print(Bundle.to_json())

# convert the object into a dict
bundle_dict = bundle_instance.to_dict()
# create an instance of Bundle from a dict
bundle_from_dict = Bundle.from_dict(bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


