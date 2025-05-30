# AnalysisInputDataMount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** |  | 
**mount_path** | **str** | The mount path is the location where the input file will be located on the machine that is running the pipeline. The use of a relative path is encouraged, but an absolute path is also allowed. The path should end with the file name, which may differ from the original input data. | 

## Example

```python
from libica.openapi.v3.models.analysis_input_data_mount import AnalysisInputDataMount

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisInputDataMount from a JSON string
analysis_input_data_mount_instance = AnalysisInputDataMount.from_json(json)
# print the JSON string representation of the object
print(AnalysisInputDataMount.to_json())

# convert the object into a dict
analysis_input_data_mount_dict = analysis_input_data_mount_instance.to_dict()
# create an instance of AnalysisInputDataMount from a dict
analysis_input_data_mount_from_dict = AnalysisInputDataMount.from_dict(analysis_input_data_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


