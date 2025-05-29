# ProjectDataMoveBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 
**destination_folder_id** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.project_data_move_batch import ProjectDataMoveBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataMoveBatch from a JSON string
project_data_move_batch_instance = ProjectDataMoveBatch.from_json(json)
# print the JSON string representation of the object
print(ProjectDataMoveBatch.to_json())

# convert the object into a dict
project_data_move_batch_dict = project_data_move_batch_instance.to_dict()
# create an instance of ProjectDataMoveBatch from a dict
project_data_move_batch_from_dict = ProjectDataMoveBatch.from_dict(project_data_move_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


