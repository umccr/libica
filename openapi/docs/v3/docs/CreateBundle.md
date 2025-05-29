# CreateBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**short_description** | **str** |  | [optional] 
**bundle_release_version** | **str** |  | 
**bundle_version_comment** | **str** |  | [optional] 
**region_id** | **str** |  | 
**metadata_model_id** | **str** |  | [optional] 
**bundle_status** | **str** |  | 
**categories** | **List[str]** | category tags as string array | 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.create_bundle import CreateBundle

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBundle from a JSON string
create_bundle_instance = CreateBundle.from_json(json)
# print the JSON string representation of the object
print(CreateBundle.to_json())

# convert the object into a dict
create_bundle_dict = create_bundle_instance.to_dict()
# create an instance of CreateBundle from a dict
create_bundle_from_dict = CreateBundle.from_dict(create_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


