# VolumeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this Volume | [optional] 
**name** | **str** | The name of this Volume | [optional] 
**tenant_id** | **str** | The unique identifier for this Volume&#39;s Tenant | [optional] 
**sub_tenant_id** | **str** | The unique identifier for this Volume&#39;s Sub Tenant | [optional] 
**urn** | **str** | The Universal Resource Name, unique to this Volume | [optional] 
**root_folder_id** | **str** | The unique identifier for the root Folder of this Volume | [optional] 
**root_key_prefix** | **str** | The base bucket location for Volumes associated with custom VolumeConfigurations otherwise this field is not set. | [optional] 
**volume_configuration_name** | **str** | Unique name of the Volume configuration for this Volume.  This field will only be set if a custom Volume configuration is associated. | [optional] 
**inherited_acl** | **list[str]** | The inherited list of Id(s) that have access to this Volume | [optional] 
**time_created** | **datetime** | The date &amp; time this Volume was created, in GDS | [optional] 
**created_by** | **str** | The creator of this Volume | [optional] 
**time_modified** | **datetime** | The date &amp; time this Volume was updated, in GDS | [optional] 
**modified_by** | **str** | The updator of this Volume | [optional] 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**metadata** | [**object**](.md) | Metadata about this Volume | [optional] 
**life_cycle** | [**VolumeLifeCycleSettings**](VolumeLifeCycleSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


