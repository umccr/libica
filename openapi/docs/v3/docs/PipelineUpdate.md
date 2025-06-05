# PipelineUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the pipeline | [optional] 
**description** | **str** | The description of the pipeline | [optional] 
**language_version** | **str** | Version of the pipeline language  | [optional] 
**proprietary** | **bool** | A boolean which indicates if the code of this pipeline is proprietary | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_update import PipelineUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineUpdate from a JSON string
pipeline_update_instance = PipelineUpdate.from_json(json)
# print the JSON string representation of the object
print(PipelineUpdate.to_json())

# convert the object into a dict
pipeline_update_dict = pipeline_update_instance.to_dict()
# create an instance of PipelineUpdate from a dict
pipeline_update_from_dict = PipelineUpdate.from_dict(pipeline_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


