# ReferenceDataList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReferenceData]**](ReferenceData.md) |  | 

## Example

```python
from libica.openapi.v3.models.reference_data_list import ReferenceDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceDataList from a JSON string
reference_data_list_instance = ReferenceDataList.from_json(json)
# print the JSON string representation of the object
print(ReferenceDataList.to_json())

# convert the object into a dict
reference_data_list_dict = reference_data_list_instance.to_dict()
# create an instance of ReferenceDataList from a dict
reference_data_list_from_dict = ReferenceDataList.from_dict(reference_data_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


