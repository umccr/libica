# PipelineLanguageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name of the version | 
**language** | **str** | The language of the version | 

## Example

```python
from libica.openapi.v3.models.pipeline_language_version import PipelineLanguageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineLanguageVersion from a JSON string
pipeline_language_version_instance = PipelineLanguageVersion.from_json(json)
# print the JSON string representation of the object
print(PipelineLanguageVersion.to_json())

# convert the object into a dict
pipeline_language_version_dict = pipeline_language_version_instance.to_dict()
# create an instance of PipelineLanguageVersion from a dict
pipeline_language_version_from_dict = PipelineLanguageVersion.from_dict(pipeline_language_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


