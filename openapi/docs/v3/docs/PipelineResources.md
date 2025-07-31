# PipelineResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**f1** | **bool** |  | [optional] 
**f2** | **bool** |  | [optional] 
**gpu** | **bool** |  | [optional] 
**software_only** | **bool** | Can not be true in case one of [f1,f2,gpu] is also true. | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_resources import PipelineResources

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineResources from a JSON string
pipeline_resources_instance = PipelineResources.from_json(json)
# print the JSON string representation of the object
print(PipelineResources.to_json())

# convert the object into a dict
pipeline_resources_dict = pipeline_resources_instance.to_dict()
# create an instance of PipelineResources from a dict
pipeline_resources_from_dict = PipelineResources.from_dict(pipeline_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


