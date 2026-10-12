# AnalysisQueryParametersPipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference to filter on. | [optional] 
**user_reference** | **str** | The user-reference to filter on. | [optional] 
**status** | **List[Optional[str]]** |  | [optional] 
**user_tags** | **List[Optional[str]]** | The user-tags to filter on. | [optional] 
**technical_tags** | **List[Optional[str]]** | The technical-tags to filter on. | [optional] 
**reference_tags** | **List[Optional[str]]** | The reference-data-tags to filter on. | [optional] 
**pipeline_names** | **List[Optional[str]]** | The pipeline names to filter on. max of 20 allowed | [optional] 
**pipeline_uuids** | **List[Optional[str]]** | The pipeline unique ids to filter on. max of 20 allowed | [optional] 
**sample_ids** | **List[Optional[str]]** | The sample IDs to filter on. Only analyses where the sample is used as input are returned. Max 20 allowed. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_query_parameters_pipeline import AnalysisQueryParametersPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryParametersPipeline from a JSON string
analysis_query_parameters_pipeline_instance = AnalysisQueryParametersPipeline.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryParametersPipeline.to_json())

# convert the object into a dict
analysis_query_parameters_pipeline_dict = analysis_query_parameters_pipeline_instance.to_dict()
# create an instance of AnalysisQueryParametersPipeline from a dict
analysis_query_parameters_pipeline_from_dict = AnalysisQueryParametersPipeline.from_dict(analysis_query_parameters_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


