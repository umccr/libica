# CreateAnalysisLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs_folder_id** | **str** | The id or the urn of the folder in which the logs of the analysis should be located. Selecting an existing folder may result in some of its contents being overwritten by new log files. When no folder is selected, the logs folder will be located in the output folder. | [optional] 
**logs_folder_path** | **str** | The path of the folder in which the logs of the analysis should be located (must start with a &#39;/&#39;). Selecting an existing folder may result in some of its contents being overwritten by new log files. When no folder is selected, the logs folder will be located in the output folder. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_analysis_logs import CreateAnalysisLogs

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnalysisLogs from a JSON string
create_analysis_logs_instance = CreateAnalysisLogs.from_json(json)
# print the JSON string representation of the object
print(CreateAnalysisLogs.to_json())

# convert the object into a dict
create_analysis_logs_dict = create_analysis_logs_instance.to_dict()
# create an instance of CreateAnalysisLogs from a dict
create_analysis_logs_from_dict = CreateAnalysisLogs.from_dict(create_analysis_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


