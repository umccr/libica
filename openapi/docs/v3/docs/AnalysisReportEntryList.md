# AnalysisReportEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisReportEntry]**](AnalysisReportEntry.md) |  | 

## Example

```python
from libica.openapi.v3.models.analysis_report_entry_list import AnalysisReportEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReportEntryList from a JSON string
analysis_report_entry_list_instance = AnalysisReportEntryList.from_json(json)
# print the JSON string representation of the object
print(AnalysisReportEntryList.to_json())

# convert the object into a dict
analysis_report_entry_list_dict = analysis_report_entry_list_instance.to_dict()
# create an instance of AnalysisReportEntryList from a dict
analysis_report_entry_list_from_dict = AnalysisReportEntryList.from_dict(analysis_report_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


