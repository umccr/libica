# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**additional_status_information** | **str** | Additional information regarding the status of this job. | [optional] 
**subject_type** | **str** | The type of the subject for which this job provides execution. | 
**subject_id** | **str** | The id of the subject for which this job provides execution. | 
**time_created** | **datetime** |  | 
**time_started** | **datetime** |  | [optional] 
**time_finished** | **datetime** |  | [optional] 
**owner** | [**User**](User.md) |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**bundle** | [**Bundle**](Bundle.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


