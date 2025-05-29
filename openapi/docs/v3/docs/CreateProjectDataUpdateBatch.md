# CreateProjectDataUpdateBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_update_groups** | [**List[DataUpdateGroup]**](DataUpdateGroup.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_project_data_update_batch import CreateProjectDataUpdateBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectDataUpdateBatch from a JSON string
create_project_data_update_batch_instance = CreateProjectDataUpdateBatch.from_json(json)
# print the JSON string representation of the object
print(CreateProjectDataUpdateBatch.to_json())

# convert the object into a dict
create_project_data_update_batch_dict = create_project_data_update_batch_instance.to_dict()
# create an instance of CreateProjectDataUpdateBatch from a dict
create_project_data_update_batch_from_dict = CreateProjectDataUpdateBatch.from_dict(create_project_data_update_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


