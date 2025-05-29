# WorkflowSessionExternalData

The external data used as input by the workflow session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** | Possible values are: s3, http, basespace. More types could be added in a future release. | 
**mount_path** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.workflow_session_external_data import WorkflowSessionExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionExternalData from a JSON string
workflow_session_external_data_instance = WorkflowSessionExternalData.from_json(json)
# print the JSON string representation of the object
print(WorkflowSessionExternalData.to_json())

# convert the object into a dict
workflow_session_external_data_dict = workflow_session_external_data_instance.to_dict()
# create an instance of WorkflowSessionExternalData from a dict
workflow_session_external_data_from_dict = WorkflowSessionExternalData.from_dict(workflow_session_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


