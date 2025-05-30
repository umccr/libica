# AnalysisPagedListV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisV3]**](AnalysisV3.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_paged_list_v3 import AnalysisPagedListV3

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisPagedListV3 from a JSON string
analysis_paged_list_v3_instance = AnalysisPagedListV3.from_json(json)
# print the JSON string representation of the object
print(AnalysisPagedListV3.to_json())

# convert the object into a dict
analysis_paged_list_v3_dict = analysis_paged_list_v3_instance.to_dict()
# create an instance of AnalysisPagedListV3 from a dict
analysis_paged_list_v3_from_dict = AnalysisPagedListV3.from_dict(analysis_paged_list_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


