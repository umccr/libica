# PipelineGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name of the pipeline group | 

## Example

```python
from libica.openapi.v3.models.pipeline_group import PipelineGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineGroup from a JSON string
pipeline_group_instance = PipelineGroup.from_json(json)
# print the JSON string representation of the object
print(PipelineGroup.to_json())

# convert the object into a dict
pipeline_group_dict = pipeline_group_instance.to_dict()
# create an instance of PipelineGroup from a dict
pipeline_group_from_dict = PipelineGroup.from_dict(pipeline_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


