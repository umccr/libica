# WorkflowSessionSequencingRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The sequencing run number (SRN) related to the workflow session. | [optional] 
**instrument_run_id** | **str** | The instrument run id related to the workflow session. | [optional] 
**external_run_id** | **str** | The external sequencing run id related to the workflow session. | [optional] 

## Example

```python
from libica.openapi.v3.models.workflow_session_sequencing_run import WorkflowSessionSequencingRun

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionSequencingRun from a JSON string
workflow_session_sequencing_run_instance = WorkflowSessionSequencingRun.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionSequencingRun.to_json())

# convert the object into a dict
workflow_session_sequencing_run_dict = workflow_session_sequencing_run_instance.to_dict()
# create an instance of WorkflowSessionSequencingRun from a dict
workflow_session_sequencing_run_from_dict = WorkflowSessionSequencingRun.from_dict(workflow_session_sequencing_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


