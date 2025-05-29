# BundleSamplePagedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BundleSample]**](BundleSample.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.bundle_sample_paged_list import BundleSamplePagedList

# TODO update the JSON string below
json = "{}"
# create an instance of BundleSamplePagedList from a JSON string
bundle_sample_paged_list_instance = BundleSamplePagedList.from_json(json)
# print the JSON string representation of the object
print(BundleSamplePagedList.to_json())

# convert the object into a dict
bundle_sample_paged_list_dict = bundle_sample_paged_list_instance.to_dict()
# create an instance of BundleSamplePagedList from a dict
bundle_sample_paged_list_from_dict = BundleSamplePagedList.from_dict(bundle_sample_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


