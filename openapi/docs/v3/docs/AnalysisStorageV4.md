# AnalysisStorageV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name of the storage option | 
**description** | **str** | The description about the storage option | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_storage_v4 import AnalysisStorageV4

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStorageV4 from a JSON string
analysis_storage_v4_instance = AnalysisStorageV4.from_json(json)
# print the JSON string representation of the object
print(AnalysisStorageV4.to_json())

# convert the object into a dict
analysis_storage_v4_dict = analysis_storage_v4_instance.to_dict()
# create an instance of AnalysisStorageV4 from a dict
analysis_storage_v4_from_dict = AnalysisStorageV4.from_dict(analysis_storage_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


