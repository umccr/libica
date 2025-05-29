# ProjectDataUnlinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_data_unlinking_batch import ProjectDataUnlinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUnlinkingBatch from a JSON string
project_data_unlinking_batch_instance = ProjectDataUnlinkingBatch.from_json(json)
# print the JSON string representation of the object
print(ProjectDataUnlinkingBatch.to_json())

# convert the object into a dict
project_data_unlinking_batch_dict = project_data_unlinking_batch_instance.to_dict()
# create an instance of ProjectDataUnlinkingBatch from a dict
project_data_unlinking_batch_from_dict = ProjectDataUnlinkingBatch.from_dict(project_data_unlinking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


