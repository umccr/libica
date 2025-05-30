# ReferenceDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the reference data type | 

## Example

```python
from libica.openapi.v3.models.reference_data_type import ReferenceDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceDataType from a JSON string
reference_data_type_instance = ReferenceDataType.from_json(json)
# print the JSON string representation of the object
print(ReferenceDataType.to_json())

# convert the object into a dict
reference_data_type_dict = reference_data_type_instance.to_dict()
# create an instance of ReferenceDataType from a dict
reference_data_type_from_dict = ReferenceDataType.from_dict(reference_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


