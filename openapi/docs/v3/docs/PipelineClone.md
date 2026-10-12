# PipelineClone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the pipeline | 
**version** | **str** | The version number of the pipeline. Use of semantic versioning is recommended but not enforced. | [optional] 
**version_comment** | **str** |  | [optional] 
**description** | **str** | The description of the pipeline | [optional] 
**language_version** | **str** | Version of the pipeline language  | [optional] 
**proprietary** | **bool** | A boolean which indicates if the code of this pipeline is proprietary | [optional] 
**icon_name** | **str** | The icon name of the pipeline | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_clone import PipelineClone

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineClone from a JSON string
pipeline_clone_instance = PipelineClone.from_json(json)
# print the JSON string representation of the object
print(PipelineClone.to_json())

# convert the object into a dict
pipeline_clone_dict = pipeline_clone_instance.to_dict()
# create an instance of PipelineClone from a dict
pipeline_clone_from_dict = PipelineClone.from_dict(pipeline_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


