# AnalysisData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[AnalysisData]**](AnalysisData.md) |  | [optional] 
**data_id** | **str** | The id of the file/folder. | 
**format** | [**DataFormat**](DataFormat.md) |  | 
**name** | **str** | The name of the file/folder as it was processed by the analysis. | 
**data_type** | **str** |  | 
**mount_path** | **str** | The requested location where the input file was located on the machine that was running the pipeline. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_data import AnalysisData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisData from a JSON string
analysis_data_instance = AnalysisData.from_json(json)
# print the JSON string representation of the object
print(AnalysisData.to_json())

# convert the object into a dict
analysis_data_dict = analysis_data_instance.to_dict()
# create an instance of AnalysisData from a dict
analysis_data_from_dict = AnalysisData.from_dict(analysis_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


