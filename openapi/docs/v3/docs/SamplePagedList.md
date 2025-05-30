# SamplePagedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Sample]**](Sample.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.sample_paged_list import SamplePagedList

# TODO update the JSON string below
json = "{}"
# create an instance of SamplePagedList from a JSON string
sample_paged_list_instance = SamplePagedList.from_json(json)
# print the JSON string representation of the object
print(SamplePagedList.to_json())

# convert the object into a dict
sample_paged_list_dict = sample_paged_list_instance.to_dict()
# create an instance of SamplePagedList from a dict
sample_paged_list_from_dict = SamplePagedList.from_dict(sample_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


