# ProjectPipelineV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline** | [**PipelineV4**](PipelineV4.md) |  | 
**project_id** | **str** |  | 
**bundle_links** | [**BundleList**](BundleList.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_pipeline_v4 import ProjectPipelineV4

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPipelineV4 from a JSON string
project_pipeline_v4_instance = ProjectPipelineV4.from_json(json)
# print the JSON string representation of the object
print(ProjectPipelineV4.to_json())

# convert the object into a dict
project_pipeline_v4_dict = project_pipeline_v4_instance.to_dict()
# create an instance of ProjectPipelineV4 from a dict
project_pipeline_v4_from_dict = ProjectPipelineV4.from_dict(project_pipeline_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


