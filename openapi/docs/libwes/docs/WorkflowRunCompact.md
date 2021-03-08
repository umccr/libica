# WorkflowRunCompact

Compact details of a workflow run
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique resource ID | [optional] 
**urn** | **str** | URN of the resource | [optional] 
**href** | **str** | HREF to the resource | [optional] 
**name** | **str** | Name of the workflow run | [optional] 
**time_started** | **datetime** | The time (in UTC) the workflow run started | [optional] 
**time_stopped** | **datetime** | The time (in UTC) the Workflow Run stopped | [optional] 
**status** | **str** | Workflow run status | [optional] 
**idempotency_key** | **str** |  | [optional] 
**status_summary** | **str** | Workflow run status summary | [optional] 
**error** | **str** | Error for a failed workflow run | [optional] 
**error_cause** | **str** | Error cause for a failed workflow run | [optional] 
**workflow_version** | [**WorkflowVersionCompact**](WorkflowVersionCompact.md) |  | [optional] 
**created_by_client_id** | **str** | Client ID of the Origin Request | [optional] 
**engine_parameters** | **str** | Workflow Engine Parameters | [optional] 
**time_created** | **datetime** | Time (in UTC) the resource was created | [optional] 
**time_modified** | **datetime** | Time (in UTC) the resource was modified | [optional] 
**created_by** | **str** | User that created the resource | [optional] 
**modified_by** | **str** | User that modified the resource | [optional] 
**tenant_id** | **str** | Tenant ID the resource belongs to | [optional] 
**acl** | **list[str]** | Access control list of the resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


