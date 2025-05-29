# ProjectDataUpdateBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_data_update_batch import ProjectDataUpdateBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUpdateBatch from a JSON string
project_data_update_batch_instance = ProjectDataUpdateBatch.from_json(json)
# print the JSON string representation of the object
print(ProjectDataUpdateBatch.to_json())

# convert the object into a dict
project_data_update_batch_dict = project_data_update_batch_instance.to_dict()
# create an instance of ProjectDataUpdateBatch from a dict
project_data_update_batch_from_dict = ProjectDataUpdateBatch.from_dict(project_data_update_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


