# CreateProjectDataMoveBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateProjectDataMoveBatchItem]**](CreateProjectDataMoveBatchItem.md) |  | 
**destination_folder_id** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.create_project_data_move_batch import CreateProjectDataMoveBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectDataMoveBatch from a JSON string
create_project_data_move_batch_instance = CreateProjectDataMoveBatch.from_json(json)
# print the JSON string representation of the object
print(CreateProjectDataMoveBatch.to_json())

# convert the object into a dict
create_project_data_move_batch_dict = create_project_data_move_batch_instance.to_dict()
# create an instance of CreateProjectDataMoveBatch from a dict
create_project_data_move_batch_from_dict = CreateProjectDataMoveBatch.from_dict(create_project_data_move_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


