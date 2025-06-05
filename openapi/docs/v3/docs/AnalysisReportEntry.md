# AnalysisReportEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_title** | **str** | The name of the report config | [optional] 
**report_data** | [**List[AnalysisReportData]**](AnalysisReportData.md) | The list of analysis report files | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_report_entry import AnalysisReportEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReportEntry from a JSON string
analysis_report_entry_instance = AnalysisReportEntry.from_json(json)
# print the JSON string representation of the object
print(AnalysisReportEntry.to_json())

# convert the object into a dict
analysis_report_entry_dict = analysis_report_entry_instance.to_dict()
# create an instance of AnalysisReportEntry from a dict
analysis_report_entry_from_dict = AnalysisReportEntry.from_dict(analysis_report_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


