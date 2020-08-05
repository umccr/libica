# WorkflowRunHistoryEvent

Information about a specific event in the workflow run history
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event, such as the name of the step/task for state-level events and run name for run-level events | [optional] 
**event_id** | **int** | Identifier for the history event, if any | [optional] 
**previous_event_id** | **int** | Identifier for any previous history event (if available) | [optional] 
**event_type** | **str** | Type of history event. The associated details entry will be populated based on the type of event. | [optional] 
**timestamp** | **datetime** | Timestamp for the history event | [optional] 
**event_details** | [**object**](.md) | Details for history event | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


