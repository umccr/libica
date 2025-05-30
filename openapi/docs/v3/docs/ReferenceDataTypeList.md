# ReferenceDataTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReferenceDataType]**](ReferenceDataType.md) |  | 

## Example

```python
from libica.openapi.v3.models.reference_data_type_list import ReferenceDataTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceDataTypeList from a JSON string
reference_data_type_list_instance = ReferenceDataTypeList.from_json(json)
# print the JSON string representation of the object
print(ReferenceDataTypeList.to_json())

# convert the object into a dict
reference_data_type_list_dict = reference_data_type_list_instance.to_dict()
# create an instance of ReferenceDataTypeList from a dict
reference_data_type_list_from_dict = ReferenceDataTypeList.from_dict(reference_data_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


