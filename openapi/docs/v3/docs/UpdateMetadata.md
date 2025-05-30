# UpdateMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_single_metadata_fields** | [**List[UpdateSingleMetadataField]**](UpdateSingleMetadataField.md) | List of metadata fields to be updated | [optional] 
**update_metadata_field_groups** | [**List[UpdateMetadataFieldGroup]**](UpdateMetadataFieldGroup.md) | List of metadata field groups to be updated | [optional] 

## Example

```python
from libica.openapi.v3.models.update_metadata import UpdateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadata from a JSON string
update_metadata_instance = UpdateMetadata.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadata.to_json())

# convert the object into a dict
update_metadata_dict = update_metadata_instance.to_dict()
# create an instance of UpdateMetadata from a dict
update_metadata_from_dict = UpdateMetadata.from_dict(update_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


