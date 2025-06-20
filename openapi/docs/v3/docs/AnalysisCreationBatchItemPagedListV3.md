# AnalysisCreationBatchItemPagedListV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisCreationBatchItemV3]**](AnalysisCreationBatchItemV3.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_paged_list_v3 import AnalysisCreationBatchItemPagedListV3

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemPagedListV3 from a JSON string
analysis_creation_batch_item_paged_list_v3_instance = AnalysisCreationBatchItemPagedListV3.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemPagedListV3.to_json())

# convert the object into a dict
analysis_creation_batch_item_paged_list_v3_dict = analysis_creation_batch_item_paged_list_v3_instance.to_dict()
# create an instance of AnalysisCreationBatchItemPagedListV3 from a dict
analysis_creation_batch_item_paged_list_v3_from_dict = AnalysisCreationBatchItemPagedListV3.from_dict(analysis_creation_batch_item_paged_list_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


