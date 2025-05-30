# BaseJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**description** | **str** | A short description of the base job | [optional] 
**table** | [**ProjectBaseTable**](ProjectBaseTable.md) |  | [optional] 
**type** | **str** | The type of the job | 
**status** | **str** | The status of the job | 
**overall_duration** | **int** | The duration of the job expressed in milliseconds | [optional] 
**details** | **str** | Detailed description of the job | [optional] 
**bytes_billed** | **int** | Bytes billed | [optional] 

## Example

```python
from libica.openapi.v3.models.base_job import BaseJob

# TODO update the JSON string below
json = "{}"
# create an instance of BaseJob from a JSON string
base_job_instance = BaseJob.from_json(json)
# print the JSON string representation of the object
print(BaseJob.to_json())

# convert the object into a dict
base_job_dict = base_job_instance.to_dict()
# create an instance of BaseJob from a dict
base_job_from_dict = BaseJob.from_dict(base_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


