# ProjectTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** |  | 
**user_tags** | **List[str]** |  | 

## Example

```python
from libica.openapi.v3.models.project_tag import ProjectTag

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTag from a JSON string
project_tag_instance = ProjectTag.from_json(json)
# print the JSON string representation of the object
print(ProjectTag.to_json())

# convert the object into a dict
project_tag_dict = project_tag_instance.to_dict()
# create an instance of ProjectTag from a dict
project_tag_from_dict = ProjectTag.from_dict(project_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


