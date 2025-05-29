# ReferenceSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the reference set | 
**reference_data_list** | [**ReferenceDataList**](ReferenceDataList.md) |  | 

## Example

```python
from libica.openapi.v3.models.reference_set import ReferenceSet

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceSet from a JSON string
reference_set_instance = ReferenceSet.from_json(json)
# print the JSON string representation of the object
print(ReferenceSet.to_json())

# convert the object into a dict
reference_set_dict = reference_set_instance.to_dict()
# create an instance of ReferenceSet from a dict
reference_set_from_dict = ReferenceSet.from_dict(reference_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


