# PipelineUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_used** | [**PipelineLastUsed**](PipelineLastUsed.md) |  | [optional] 
**pinned_in_project** | **bool** | The pinned state of the pipeline within the project | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_usage import PipelineUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineUsage from a JSON string
pipeline_usage_instance = PipelineUsage.from_json(json)
# print the JSON string representation of the object
print(PipelineUsage.to_json())

# convert the object into a dict
pipeline_usage_dict = pipeline_usage_instance.to_dict()
# create an instance of PipelineUsage from a dict
pipeline_usage_from_dict = PipelineUsage.from_dict(pipeline_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


