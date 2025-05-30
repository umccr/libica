# SampleCreationBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | [optional] 
**sequencing_run_id** | **str** | The sequencingRunId to link to all created samples and linked data | [optional] 

## Example

```python
from libica.openapi.v3.models.sample_creation_batch import SampleCreationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCreationBatch from a JSON string
sample_creation_batch_instance = SampleCreationBatch.from_json(json)
# print the JSON string representation of the object
print(SampleCreationBatch.to_json())

# convert the object into a dict
sample_creation_batch_dict = sample_creation_batch_instance.to_dict()
# create an instance of SampleCreationBatch from a dict
sample_creation_batch_from_dict = SampleCreationBatch.from_dict(sample_creation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


