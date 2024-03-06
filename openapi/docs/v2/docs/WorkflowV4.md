# WorkflowV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** | The code of the workflow | 
**urn** | **str** | The URN of the workflow. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | 
**description** | **str** | The description of the workflow | 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**workflow_tags** | [**PipelineTag**](PipelineTag.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


