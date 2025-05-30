# ReferenceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the reference data | 
**species** | [**Species**](Species.md) |  | [optional] 
**data_format** | [**DataFormat**](DataFormat.md) |  | [optional] 
**version** | **str** | The version of the reference data | 
**type_list** | [**ReferenceDataTypeList**](ReferenceDataTypeList.md) |  | 

## Example

```python
from libica.openapi.v3.models.reference_data import ReferenceData

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceData from a JSON string
reference_data_instance = ReferenceData.from_json(json)
# print the JSON string representation of the object
print(ReferenceData.to_json())

# convert the object into a dict
reference_data_dict = reference_data_instance.to_dict()
# create an instance of ReferenceData from a dict
reference_data_from_dict = ReferenceData.from_dict(reference_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


