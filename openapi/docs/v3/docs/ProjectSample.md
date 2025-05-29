# ProjectSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | [**Sample**](Sample.md) |  | 
**project_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.project_sample import ProjectSample

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSample from a JSON string
project_sample_instance = ProjectSample.from_json(json)
# print the JSON string representation of the object
print(ProjectSample.to_json())

# convert the object into a dict
project_sample_dict = project_sample_instance.to_dict()
# create an instance of ProjectSample from a dict
project_sample_from_dict = ProjectSample.from_dict(project_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


