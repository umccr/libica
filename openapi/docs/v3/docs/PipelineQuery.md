# PipelineQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | Filter on the UUID of the pipeline version | [optional] 
**pipeline_groups** | **List[str]** | Filter on the UUID of the pipeline group containing pipeline versions | [optional] 
**name** | [**StringQuery**](StringQuery.md) |  | [optional] 
**version** | [**StringQuery**](StringQuery.md) |  | [optional] 
**description** | [**StringQuery**](StringQuery.md) |  | [optional] 
**statuses** | **List[str]** | Filter on the status of the pipeline version. Possible values: &#39;Draft&#39;, &#39;Released&#39;, &#39;Deprecated&#39;, &#39;Archived&#39;, &#39;Importing&#39;, &#39;Import Cancelling&#39;, &#39;Import Incomplete&#39;, &#39;Import Failed&#39;. | [optional] 
**pipeline_language** | **str** | Filter on the pipeline language of the pipeline version. Possible values: &#39;Nextflow&#39;, &#39;CWL&#39;. | [optional] 
**pipeline_language_version_status** | [**PipelineLanguageVersionStatusQuery**](PipelineLanguageVersionStatusQuery.md) |  | [optional] 
**last_used** | [**DateQuery**](DateQuery.md) |  | [optional] 
**pinned** | **bool** | Filter on the pinned state of the pipeline version | [optional] 
**owners** | **List[str]** | Filter on the owner of the pipeline version | [optional] 
**number_of_versions_to_include_for_each_pipeline_group** | **int** | Number of pipeline versions to include for each pipeline group. If provided, offset based paging will always be used. If not provided, all versions will be included. | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_query import PipelineQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineQuery from a JSON string
pipeline_query_instance = PipelineQuery.from_json(json)
# print the JSON string representation of the object
print(PipelineQuery.to_json())

# convert the object into a dict
pipeline_query_dict = pipeline_query_instance.to_dict()
# create an instance of PipelineQuery from a dict
pipeline_query_from_dict = PipelineQuery.from_dict(pipeline_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


