# AnalysisLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs_folder** | [**Data**](Data.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_logs import AnalysisLogs

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisLogs from a JSON string
analysis_logs_instance = AnalysisLogs.from_json(json)
# print the JSON string representation of the object
print(AnalysisLogs.to_json())

# convert the object into a dict
analysis_logs_dict = analysis_logs_instance.to_dict()
# create an instance of AnalysisLogs from a dict
analysis_logs_from_dict = AnalysisLogs.from_dict(analysis_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


