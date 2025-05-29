# ProjectDataCopyBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 
**destination_folder_id** | **str** |  | [optional] 
**copy_user_tags** | **bool** |  | 
**copy_technical_tags** | **bool** |  | 
**copy_instrument_info** | **bool** |  | 
**action_on_exist** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.project_data_copy_batch import ProjectDataCopyBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataCopyBatch from a JSON string
project_data_copy_batch_instance = ProjectDataCopyBatch.from_json(json)
# print the JSON string representation of the object
print(ProjectDataCopyBatch.to_json())

# convert the object into a dict
project_data_copy_batch_dict = project_data_copy_batch_instance.to_dict()
# create an instance of ProjectDataCopyBatch from a dict
project_data_copy_batch_from_dict = ProjectDataCopyBatch.from_dict(project_data_copy_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


