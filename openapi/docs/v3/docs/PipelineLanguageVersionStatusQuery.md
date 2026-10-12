# PipelineLanguageVersionStatusQuery

Filter on the language version status of the pipeline version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | The language version statuses to filter on. Possible values: &#39;Supported&#39;, &#39;Deprecated&#39;, &#39;Not Supported&#39;. | [optional] 
**match_mode** | **str** | Whether to include or exclude pipelines matching the given statuses. INCLUDE returns only pipelines whose language version status is in the list. EXCLUDE returns pipelines whose language version status is NOT in the list, including pipelines with no language version status set. Defaults to INCLUDE when not provided. Allowed values: INCLUDE, EXCLUDE. | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_language_version_status_query import PipelineLanguageVersionStatusQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineLanguageVersionStatusQuery from a JSON string
pipeline_language_version_status_query_instance = PipelineLanguageVersionStatusQuery.from_json(json)
# print the JSON string representation of the object
print(PipelineLanguageVersionStatusQuery.to_json())

# convert the object into a dict
pipeline_language_version_status_query_dict = pipeline_language_version_status_query_instance.to_dict()
# create an instance of PipelineLanguageVersionStatusQuery from a dict
pipeline_language_version_status_query_from_dict = PipelineLanguageVersionStatusQuery.from_dict(pipeline_language_version_status_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


