# AnalysisStorageV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the storage option | 
**description** | **str** | The description about the storage option | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_storage_v3 import AnalysisStorageV3

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStorageV3 from a JSON string
analysis_storage_v3_instance = AnalysisStorageV3.from_json(json)
# print the JSON string representation of the object
print(AnalysisStorageV3.to_json())

# convert the object into a dict
analysis_storage_v3_dict = analysis_storage_v3_instance.to_dict()
# create an instance of AnalysisStorageV3 from a dict
analysis_storage_v3_from_dict = AnalysisStorageV3.from_dict(analysis_storage_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


