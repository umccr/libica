# CreateProjectDataCopyBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateProjectDataCopyBatchItem]**](CreateProjectDataCopyBatchItem.md) |  | 
**destination_folder_id** | **str** |  | [optional] 
**copy_user_tags** | **bool** |  | 
**copy_technical_tags** | **bool** |  | 
**copy_instrument_info** | **bool** |  | 
**action_on_exist** | **str** | only applicable on files, not on folders | 

## Example

```python
from libica.openapi.v3.models.create_project_data_copy_batch import CreateProjectDataCopyBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectDataCopyBatch from a JSON string
create_project_data_copy_batch_instance = CreateProjectDataCopyBatch.from_json(json)
# print the JSON string representation of the object
print(CreateProjectDataCopyBatch.to_json())

# convert the object into a dict
create_project_data_copy_batch_dict = create_project_data_copy_batch_instance.to_dict()
# create an instance of CreateProjectDataCopyBatch from a dict
create_project_data_copy_batch_from_dict = CreateProjectDataCopyBatch.from_dict(create_project_data_copy_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


