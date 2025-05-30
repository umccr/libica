# UpdateSingleMetadataField

List of metadata fields to be updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | [**FieldId**](FieldId.md) |  | [optional] 
**field_name** | **str** | The field name to be updated. Either the field ID or field name is required. | [optional] 
**values** | **List[str]** | The updated value(s) | [optional] 

## Example

```python
from libica.openapi.v3.models.update_single_metadata_field import UpdateSingleMetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSingleMetadataField from a JSON string
update_single_metadata_field_instance = UpdateSingleMetadataField.from_json(json)
# print the JSON string representation of the object
print(UpdateSingleMetadataField.to_json())

# convert the object into a dict
update_single_metadata_field_dict = update_single_metadata_field_instance.to_dict()
# create an instance of UpdateSingleMetadataField from a dict
update_single_metadata_field_from_dict = UpdateSingleMetadataField.from_dict(update_single_metadata_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


