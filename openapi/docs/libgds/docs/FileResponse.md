# FileResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_metadata** | [**object**](.md) | Metadata about this file&#39;s volume | [optional] 
**id** | **str** | A unique identifier for this File | [optional] 
**name** | **str** | The name of this File | [optional] 
**volume_id** | **str** | The unique identifier of the volume where the file resides | [optional] 
**parent_folder_id** | **str** | The unique identifier of the folder where the file resides | [optional] 
**volume_name** | **str** | The name of the volume where the file resides | [optional] 
**volume_configuration_name** | **str** | The name of the volume configuration (BYOB only) | [optional] 
**type** | **str** | The type of the File | [optional] 
**tenant_id** | **str** | The unique identifier for this File&#39;s Tenant | [optional] 
**sub_tenant_id** | **str** | The unique identifier for this File&#39;s Sub Tenant | [optional] 
**path** | **str** | The (GDS) path to this File | [optional] 
**time_created** | **datetime** | The date &amp; time this File was created, in GDS | [optional] 
**created_by** | **str** | The creator of this File | [optional] 
**time_modified** | **datetime** | The date &amp; time this File was updated, in GDS | [optional] 
**modified_by** | **str** | The updator of this File | [optional] 
**inherited_acl** | **list[str]** | The inherited list of Id(s) that have access to this File | [optional] 
**urn** | **str** | The Universal Resource Name, unique to this File | [optional] 
**size_in_bytes** | **int** | The File&#39;s Size in bytes | [optional] 
**metadata** | [**object**](.md) | Metadata about this File | [optional] 
**is_uploaded** | **bool** | The current upload state of the File | [optional] 
**archive_status** | [**ArchiveStatuses**](ArchiveStatuses.md) |  | [optional] 
**time_archived** | **datetime** | The date &amp; time this File was archived | [optional] 
**storage_tier** | [**StorageTier**](StorageTier.md) |  | [optional] 
**e_tag** | **str** | The File&#39;s ETag | [optional] 
**format** | **str** | The File&#39;s Format | [optional] 
**format_edam** | **str** |  | [optional] 
**status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**life_cycle** | [**FileLifeCycleSettings**](FileLifeCycleSettings.md) |  | [optional] 
**presigned_url** | **str** | The presigned Url allowing access to this File | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


