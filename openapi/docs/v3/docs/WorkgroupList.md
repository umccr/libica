# WorkgroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Workgroup]**](Workgroup.md) |  | 

## Example

```python
from libica.openapi.v3.models.workgroup_list import WorkgroupList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupList from a JSON string
workgroup_list_instance = WorkgroupList.from_json(json)
# print the JSON string representation of the object
print(WorkgroupList.to_json())

# convert the object into a dict
workgroup_list_dict = workgroup_list_instance.to_dict()
# create an instance of WorkgroupList from a dict
workgroup_list_from_dict = WorkgroupList.from_dict(workgroup_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


