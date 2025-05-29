# AnalysisInputExternalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 
**mount_path** | **str** | The mount path is the location where the input file will be located on the machine that is running the pipeline. The use of a relative path is encouraged, but an absolute path is also allowed. The path should end with the file name, which may differ from the original input data. | [optional] 
**s3_details** | [**AnalysisS3DataDetails**](AnalysisS3DataDetails.md) |  | [optional] 
**basespace_details** | [**AnalysisBaseSpaceDataDetails**](AnalysisBaseSpaceDataDetails.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_input_external_data import AnalysisInputExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisInputExternalData from a JSON string
analysis_input_external_data_instance = AnalysisInputExternalData.from_json(json)
# print the JSON string representation of the object
print(AnalysisInputExternalData.to_json())

# convert the object into a dict
analysis_input_external_data_dict = analysis_input_external_data_instance.to_dict()
# create an instance of AnalysisInputExternalData from a dict
analysis_input_external_data_from_dict = AnalysisInputExternalData.from_dict(analysis_input_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


