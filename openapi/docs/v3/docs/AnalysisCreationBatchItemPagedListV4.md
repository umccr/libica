# AnalysisCreationBatchItemPagedListV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisCreationBatchItemV4]**](AnalysisCreationBatchItemV4.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_paged_list_v4 import AnalysisCreationBatchItemPagedListV4

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemPagedListV4 from a JSON string
analysis_creation_batch_item_paged_list_v4_instance = AnalysisCreationBatchItemPagedListV4.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemPagedListV4.to_json())

# convert the object into a dict
analysis_creation_batch_item_paged_list_v4_dict = analysis_creation_batch_item_paged_list_v4_instance.to_dict()
# create an instance of AnalysisCreationBatchItemPagedListV4 from a dict
analysis_creation_batch_item_paged_list_v4_from_dict = AnalysisCreationBatchItemPagedListV4.from_dict(analysis_creation_batch_item_paged_list_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


