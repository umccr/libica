# CreateProjectDataLinkingBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateProjectDataLinkingBatchItem]**](CreateProjectDataLinkingBatchItem.md) |  | 

## Example

```python
from libica.openapi.v3.models.create_project_data_linking_batch import CreateProjectDataLinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectDataLinkingBatch from a JSON string
create_project_data_linking_batch_instance = CreateProjectDataLinkingBatch.from_json(json)
# print the JSON string representation of the object
print(CreateProjectDataLinkingBatch.to_json())

# convert the object into a dict
create_project_data_linking_batch_dict = create_project_data_linking_batch_instance.to_dict()
# create an instance of CreateProjectDataLinkingBatch from a dict
create_project_data_linking_batch_from_dict = CreateProjectDataLinkingBatch.from_dict(create_project_data_linking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


