# PipelineVersionComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_comment** | **str** | The version comment (up to 4000 characters) | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_version_comment import PipelineVersionComment

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineVersionComment from a JSON string
pipeline_version_comment_instance = PipelineVersionComment.from_json(json)
# print the JSON string representation of the object
print(PipelineVersionComment.to_json())

# convert the object into a dict
pipeline_version_comment_dict = pipeline_version_comment_instance.to_dict()
# create an instance of PipelineVersionComment from a dict
pipeline_version_comment_from_dict = PipelineVersionComment.from_dict(pipeline_version_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


