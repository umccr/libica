# AnalysisV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**reference** | **str** | The unique reference of the analysis | 
**user_reference** | **str** | The user reference of the analysis | 
**pipeline** | [**PipelineV3**](PipelineV3.md) |  | 
**workflow_session** | [**WorkflowSessionV3**](WorkflowSessionV3.md) |  | [optional] 
**status** | **str** | The status of the analysis | 
**start_date** | **datetime** | When the analysis was started | [optional] 
**end_date** | **datetime** | When the analysis was finished | [optional] 
**summary** | **str** | The summary of the analysis | [optional] 
**analysis_storage** | [**AnalysisStorageV3**](AnalysisStorageV3.md) |  | [optional] 
**analysis_priority** | **str** | The priority of the analysis | [optional] 
**tags** | [**AnalysisTag**](AnalysisTag.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_v3 import AnalysisV3

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisV3 from a JSON string
analysis_v3_instance = AnalysisV3.from_json(json)
# print the JSON string representation of the object
print(AnalysisV3.to_json())

# convert the object into a dict
analysis_v3_dict = analysis_v3_instance.to_dict()
# create an instance of AnalysisV3 from a dict
analysis_v3_from_dict = AnalysisV3.from_dict(analysis_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


