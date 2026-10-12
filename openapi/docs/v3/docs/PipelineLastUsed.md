# PipelineLastUsed

The last used date of the pipeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The requested date of the last analysis started with the pipeline | [optional] 
**analysis_id** | **str** | The id of the last analysis started with the pipeline | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_last_used import PipelineLastUsed

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineLastUsed from a JSON string
pipeline_last_used_instance = PipelineLastUsed.from_json(json)
# print the JSON string representation of the object
print(PipelineLastUsed.to_json())

# convert the object into a dict
pipeline_last_used_dict = pipeline_last_used_instance.to_dict()
# create an instance of PipelineLastUsed from a dict
pipeline_last_used_from_dict = PipelineLastUsed.from_dict(pipeline_last_used_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


