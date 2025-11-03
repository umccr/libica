# DataUpdateGroup

Updates to apply.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ids** | **List[str]** |  | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**will_be_archived_at** | **datetime** | The timestamp when the data should be archived. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
**will_be_deleted_at** | **datetime** | The timestamp when the data should be deleted. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; eg: 2021-01-30T08:30:00Z | [optional] 
**clear_will_be_archived_at** | **bool** | Boolean to indicate that the willBeArchivedAt value should be cleared. | [optional] [default to False]
**clear_will_be_deleted_at** | **bool** | Boolean to indicate that the willBeDeletedAt value should be cleared. | [optional] [default to False]

## Example

```python
from libica.openapi.v3.models.data_update_group import DataUpdateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DataUpdateGroup from a JSON string
data_update_group_instance = DataUpdateGroup.from_json(json)
# print the JSON string representation of the object
print(DataUpdateGroup.to_json())

# convert the object into a dict
data_update_group_dict = data_update_group_instance.to_dict()
# create an instance of DataUpdateGroup from a dict
data_update_group_from_dict = DataUpdateGroup.from_dict(data_update_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


