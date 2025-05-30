# PipelineTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** | Technical tags | 

## Example

```python
from libica.openapi.v3.models.pipeline_tag import PipelineTag

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineTag from a JSON string
pipeline_tag_instance = PipelineTag.from_json(json)
# print the JSON string representation of the object
print(PipelineTag.to_json())

# convert the object into a dict
pipeline_tag_dict = pipeline_tag_instance.to_dict()
# create an instance of PipelineTag from a dict
pipeline_tag_from_dict = PipelineTag.from_dict(pipeline_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


