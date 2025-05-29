# ProjectPipelineList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectPipeline]**](ProjectPipeline.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_pipeline_list import ProjectPipelineList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPipelineList from a JSON string
project_pipeline_list_instance = ProjectPipelineList.from_json(json)
# print the JSON string representation of the object
print(ProjectPipelineList.to_json())

# convert the object into a dict
project_pipeline_list_dict = project_pipeline_list_instance.to_dict()
# create an instance of ProjectPipelineList from a dict
project_pipeline_list_from_dict = ProjectPipelineList.from_dict(project_pipeline_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


