# CreateCwlAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_reference** | **str** | The user-reference of the analysis. This should be something meaningful for the user. | 
**pipeline_id** | **str** | The pipeline for which an analysis will be created. | 
**tags** | [**CreateAnalysisTag**](CreateAnalysisTag.md) |  | [optional] 
**analysis_storage_id** | **str** | The id of the storage to use for the analysis. | [optional] 
**output_parent_folder_id** | **str** | The id or the urn of the folder in which the output folder should be created. | [optional] 
**logs** | [**CreateAnalysisLogs**](CreateAnalysisLogs.md) |  | [optional] 
**analysis_output** | [**List[AnalysisOutputMapping]**](AnalysisOutputMapping.md) |  | [optional] 
**analysis_input** | [**CwlAnalysisInput**](CwlAnalysisInput.md) |  | 
**activation_code_detail_id** | **str** | Indicates under which activation code the pipeline is executed. | [optional] 

## Example

```python
from libica.openapi.v3.models.create_cwl_analysis import CreateCwlAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCwlAnalysis from a JSON string
create_cwl_analysis_instance = CreateCwlAnalysis.from_json(json)
# print the JSON string representation of the object
print(CreateCwlAnalysis.to_json())

# convert the object into a dict
create_cwl_analysis_dict = create_cwl_analysis_instance.to_dict()
# create an instance of CreateCwlAnalysis from a dict
create_cwl_analysis_from_dict = CreateCwlAnalysis.from_dict(create_cwl_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


