# CreateNextflowAnalysis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_reference** | **str** | The user-reference of the analysis. This should be something meaningful for the user. | 
**pipeline_id** | **str** | The pipeline for which an analysis will be created. | 
**analysis_input** | [**NextflowAnalysisInput**](NextflowAnalysisInput.md) |  | 
**tags** | [**CreateAnalysisTag**](CreateAnalysisTag.md) |  | [optional] 
**analysis_storage_id** | **str, none_type** | The id of the storage to use for the analysis. | [optional] 
**output_parent_folder_id** | **str, none_type** | The id or the urn of the folder in which the output folder should be created. | [optional] 
**analysis_output** | [**[AnalysisOutputMapping], none_type**](AnalysisOutputMapping.md) |  | [optional] 
**activation_code_detail_id** | **str, none_type** | Indicates under which activation code the pipeline is executed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


