# JobPagedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Job]**](Job.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.job_paged_list import JobPagedList

# TODO update the JSON string below
json = "{}"
# create an instance of JobPagedList from a JSON string
job_paged_list_instance = JobPagedList.from_json(json)
# print the JSON string representation of the object
print(JobPagedList.to_json())

# convert the object into a dict
job_paged_list_dict = job_paged_list_instance.to_dict()
# create an instance of JobPagedList from a dict
job_paged_list_from_dict = JobPagedList.from_dict(job_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


