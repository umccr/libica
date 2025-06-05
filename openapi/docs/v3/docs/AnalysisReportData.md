# AnalysisReportData

The list of analysis report files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | The data id of the report | [optional] 
**format** | **str** | The format of the report | [optional] 
**name** | **str** | The name of the report file | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_report_data import AnalysisReportData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReportData from a JSON string
analysis_report_data_instance = AnalysisReportData.from_json(json)
# print the JSON string representation of the object
print(AnalysisReportData.to_json())

# convert the object into a dict
analysis_report_data_dict = analysis_report_data_instance.to_dict()
# create an instance of AnalysisReportData from a dict
analysis_report_data_from_dict = AnalysisReportData.from_dict(analysis_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


