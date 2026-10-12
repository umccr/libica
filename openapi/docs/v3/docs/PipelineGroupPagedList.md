# PipelineGroupPagedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PipelineGroup]**](PipelineGroup.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.pipeline_group_paged_list import PipelineGroupPagedList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineGroupPagedList from a JSON string
pipeline_group_paged_list_instance = PipelineGroupPagedList.from_json(json)
# print the JSON string representation of the object
print(PipelineGroupPagedList.to_json())

# convert the object into a dict
pipeline_group_paged_list_dict = pipeline_group_paged_list_instance.to_dict()
# create an instance of PipelineGroupPagedList from a dict
pipeline_group_paged_list_from_dict = PipelineGroupPagedList.from_dict(pipeline_group_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


