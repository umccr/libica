# CreateProjectDataUnlinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateProjectDataUnlinkingBatchItem]**](CreateProjectDataUnlinkingBatchItem.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_project_data_unlinking_batch import CreateProjectDataUnlinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectDataUnlinkingBatch from a JSON string
create_project_data_unlinking_batch_instance = CreateProjectDataUnlinkingBatch.from_json(json)
# print the JSON string representation of the object
print(CreateProjectDataUnlinkingBatch.to_json())

# convert the object into a dict
create_project_data_unlinking_batch_dict = create_project_data_unlinking_batch_instance.to_dict()
# create an instance of CreateProjectDataUnlinkingBatch from a dict
create_project_data_unlinking_batch_from_dict = CreateProjectDataUnlinkingBatch.from_dict(create_project_data_unlinking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


