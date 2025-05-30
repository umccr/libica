# UpdateMetadataFieldGroup

List of metadata field groups to be updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | [**FieldId**](FieldId.md) |  | [optional] 
**field_name** | **str** | The field name to be updated. Either the field ID or field name is required. | [optional] 
**index** | **int** | Which metadata row index to update | 
**update_single_metadata_fields** | [**List[UpdateSingleMetadataField]**](UpdateSingleMetadataField.md) | List of metadata fields to be updated | 

## Example

```python
from libica.openapi.v3.models.update_metadata_field_group import UpdateMetadataFieldGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataFieldGroup from a JSON string
update_metadata_field_group_instance = UpdateMetadataFieldGroup.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadataFieldGroup.to_json())

# convert the object into a dict
update_metadata_field_group_dict = update_metadata_field_group_instance.to_dict()
# create an instance of UpdateMetadataFieldGroup from a dict
update_metadata_field_group_from_dict = UpdateMetadataFieldGroup.from_dict(update_metadata_field_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


