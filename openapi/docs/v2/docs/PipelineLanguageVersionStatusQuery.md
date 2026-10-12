# PipelineLanguageVersionStatusQuery

Filter on the language version status of the pipeline version.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **[str]** | The language version statuses to filter on. Possible values: &#39;Supported&#39;, &#39;Deprecated&#39;, &#39;Not Supported&#39;. | [optional] 
**match_mode** | **str** | Whether to include or exclude pipelines matching the given statuses. INCLUDE returns only pipelines whose language version status is in the list. EXCLUDE returns pipelines whose language version status is NOT in the list, including pipelines with no language version status set. Defaults to INCLUDE when not provided. Allowed values: INCLUDE, EXCLUDE. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


