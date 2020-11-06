# WorkflowSignal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique resource ID | [optional] 
**urn** | **str** | URN of the resource | [optional] 
**href** | **str** | HREF to the resource | [optional] 
**send_heartbeat_href** | **str** | HREF to send a heartbeat to a workflow signal | [optional] 
**send_success_response_href** | **str** | HREF to succeed a workflow signal | [optional] 
**send_failure_response_href** | **str** | HREF to fail a workflow signal | [optional] 
**name** | **str** | Unique name of the signal | [optional] 
**status** | **str** | Current status of the signal | [optional] 
**type** | **str** | User-defined type associated with the signal | [optional] 
**description** | **str** | Description of the signal | [optional] 
**inputs** | [**object**](.md) | Inputs defined by the originating WaitForSignal state, in JSON. | [optional] 
**workflow_run** | [**WorkflowRunCompact**](WorkflowRunCompact.md) |  | [optional] 
**timeout_seconds** | **int** | Signal timeout in seconds. The Signal will timeout if a heartbeat, succeed or fail is not received in this time interval. | [optional] 
**result** | [**object**](.md) | The result of a successful signalling action in JSON. | [optional] 
**error** | **str** | The error of a failed signal. | [optional] 
**error_cause** | **str** | The error cause of a failed signal. | [optional] 
**created_by_client_id** | **str** | Client ID of the Origin Request | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that modified the resource | [optional] 
**tenant_id** | **str** | Tenant ID the resource belongs to | [optional] 
**acl** | **list[str]** | Access control list of the resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


