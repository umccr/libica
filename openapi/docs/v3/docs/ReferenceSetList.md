# ReferenceSetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReferenceSet]**](ReferenceSet.md) |  | 

## Example

```python
from libica.openapi.v3.models.reference_set_list import ReferenceSetList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceSetList from a JSON string
reference_set_list_instance = ReferenceSetList.from_json(json)
# print the JSON string representation of the object
print(ReferenceSetList.to_json())

# convert the object into a dict
reference_set_list_dict = reference_set_list_instance.to_dict()
# create an instance of ReferenceSetList from a dict
reference_set_list_from_dict = ReferenceSetList.from_dict(reference_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


