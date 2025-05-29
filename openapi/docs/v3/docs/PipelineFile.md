# PipelineFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.pipeline_file import PipelineFile

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineFile from a JSON string
pipeline_file_instance = PipelineFile.from_json(json)
# print the JSON string representation of the object
print(PipelineFile.to_json())

# convert the object into a dict
pipeline_file_dict = pipeline_file_instance.to_dict()
# create an instance of PipelineFile from a dict
pipeline_file_from_dict = PipelineFile.from_dict(pipeline_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


