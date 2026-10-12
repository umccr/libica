# PipelineV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner** | [**UserIdentifier**](UserIdentifier.md) |  | 
**tenant** | [**TenantIdentifier**](TenantIdentifier.md) |  | 
**code** | **str** | The code of the pipeline. This is deprecated, use the name &amp; version attributes instead | 
**description** | **str** | The description of the pipeline | 
**language** | **str** | The language that is used by the pipeline | 
**pipeline_tags** | [**PipelineTag**](PipelineTag.md) |  | 
**analysis_storage** | [**AnalysisStorageV4**](AnalysisStorageV4.md) |  | 
**urn** | **str, none_type** | The URN of the pipeline. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**pipeline_group** | [**PipelineGroupIdentifier**](PipelineGroupIdentifier.md) |  | [optional] 
**name** | **str** | The name of the pipeline | [optional] 
**status** | **str, none_type** | The status of the pipeline | [optional] 
**status_as_string** | **str** | The status of the pipeline as string (&#39;Draft&#39;, &#39;Released&#39;, &#39;Deprecated&#39;, &#39;Archived&#39;, &#39;Importing&#39;, &#39;Import Cancelling&#39;, &#39;Import Incomplete&#39;, &#39;Import Failed&#39;) | [optional] 
**language_version** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**proprietary** | **bool, none_type** | A boolean which indicates if the code of this pipeline is proprietary | [optional]  if omitted the server will use the default value of False
**input_form_type** | **str** | The type of the inputform used. | [optional] 
**report_configs** | [**PipelineReportConfig**](PipelineReportConfig.md) |  | [optional] 
**resources** | [**PipelineResources**](PipelineResources.md) |  | [optional] 
**git_pipeline_import** | [**GitPipelineImport**](GitPipelineImport.md) |  | [optional] 
**version** | **str, none_type** | The version number of the pipeline | [optional] 
**latest_version_in_group** | **bool, none_type** |  | [optional] 
**pipeline_usage** | [**PipelineUsage**](PipelineUsage.md) |  | [optional] 
**icon_name** | **str, none_type** | The icon name of the pipeline | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


