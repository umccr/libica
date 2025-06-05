# PipelineReportConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[Config]**](Config.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_report_config import PipelineReportConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineReportConfig from a JSON string
pipeline_report_config_instance = PipelineReportConfig.from_json(json)
# print the JSON string representation of the object
print(PipelineReportConfig.to_json())

# convert the object into a dict
pipeline_report_config_dict = pipeline_report_config_instance.to_dict()
# create an instance of PipelineReportConfig from a dict
pipeline_report_config_from_dict = PipelineReportConfig.from_dict(pipeline_report_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


