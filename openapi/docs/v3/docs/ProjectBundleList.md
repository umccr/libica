# ProjectBundleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectBundle]**](ProjectBundle.md) |  | 

## Example

```python
from libica.openapi.v3.models.project_bundle_list import ProjectBundleList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBundleList from a JSON string
project_bundle_list_instance = ProjectBundleList.from_json(json)
# print the JSON string representation of the object
print(ProjectBundleList.to_json())

# convert the object into a dict
project_bundle_list_dict = project_bundle_list_instance.to_dict()
# create an instance of ProjectBundleList from a dict
project_bundle_list_from_dict = ProjectBundleList.from_dict(project_bundle_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


