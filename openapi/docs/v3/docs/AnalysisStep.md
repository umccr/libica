# AnalysisStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** | The status of the analysis step | 
**queue_date** | **datetime** | When the analysis step was queued | [optional] 
**start_date** | **datetime** | When the analysis step was started | [optional] 
**end_date** | **datetime** | When the analysis step was finished | [optional] 
**technical** | **bool** | Indicates which kind of step was executed | 
**logs** | [**AnalysisStepLogs**](AnalysisStepLogs.md) |  | 
**exit_code** | **int** | The exit code of the analysis step | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_step import AnalysisStep

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStep from a JSON string
analysis_step_instance = AnalysisStep.from_json(json)
# print the JSON string representation of the object
print(AnalysisStep.to_json())

# convert the object into a dict
analysis_step_dict = analysis_step_instance.to_dict()
# create an instance of AnalysisStep from a dict
analysis_step_from_dict = AnalysisStep.from_dict(analysis_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


