# PipelineV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**code** | **str** | The code of the pipeline | 
**description** | **str** | The description of the pipeline | 
**language** | **str** | The language that is used by the pipeline | 
**pipeline_tags** | [**PipelineTag**](PipelineTag.md) |  | 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | 
**urn** | **str, none_type** | The URN of the pipeline. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**status** | **str, none_type** | The status of the pipeline | [optional] 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**proprietary** | **bool, none_type** | A boolean which indicates if the code of this pipeline is proprietary | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


