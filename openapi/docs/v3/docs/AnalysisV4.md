# AnalysisV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**reference** | **str** | The unique reference of the analysis | 
**user_reference** | **str** | The user reference of the analysis | 
**pipeline** | [**PipelineV4**](PipelineV4.md) |  | 
**workflow_session** | [**WorkflowSessionV4**](WorkflowSessionV4.md) |  | [optional] 
**status** | **str** | The status of the analysis | 
**start_date** | **datetime** | When the analysis was started | [optional] 
**end_date** | **datetime** | When the analysis was finished | [optional] 
**summary** | **str** | The summary of the analysis | [optional] 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | [optional] 
**analysis_priority** | **str** | The priority of the analysis | [optional] 
**tags** | [**AnalysisTag**](AnalysisTag.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_v4 import AnalysisV4

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisV4 from a JSON string
analysis_v4_instance = AnalysisV4.from_json(json)
# print the JSON string representation of the object
print(AnalysisV4.to_json())

# convert the object into a dict
analysis_v4_dict = analysis_v4_instance.to_dict()
# create an instance of AnalysisV4 from a dict
analysis_v4_from_dict = AnalysisV4.from_dict(analysis_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


