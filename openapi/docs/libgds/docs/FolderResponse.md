# FolderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this Folder | [optional] 
**name** | **str** | The name of this Folder | [optional] 
**volume_id** | **str** | The unique identifier for this Folder&#39;s Volume | [optional] 
**volume_name** | **str** | The name of this Folder&#39;s Volume | [optional] 
**tenant_id** | **str** | The unique identifier for this Folders&#39;s Tenant | [optional] 
**sub_tenant_id** | **str** | The unique identifier for this Folder&#39;s Sub Tenant | [optional] 
**urn** | **str** | The Universal Resource Name, unique to this Folder | [optional] 
**path** | **str** | The (GDS) folder path to this Folder | [optional] 
**acl** | **list[str]** | The list of directly specified Id(s) that have access to this Folder | [optional] 
**inherited_acl** | **list[str]** | The inherited list of Id(s) that have access to this Folder | [optional] 
**time_created** | **datetime** | The date &amp; time this Folder was created, in GDS | [optional] 
**created_by** | **str** | The creator of this Folder | [optional] 
**time_modified** | **datetime** | The date &amp; time this Folder was updated, in GDS | [optional] 
**modified_by** | **str** | The updator of this Folder | [optional] 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**archive_job_storage_tier** | [**StorageTier**](StorageTier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


