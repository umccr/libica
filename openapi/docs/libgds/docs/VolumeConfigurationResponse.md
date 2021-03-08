# VolumeConfigurationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the volume configuration | [optional] 
**tenant_id** | **str** | The unique identifier for this Volume Configuration&#39;s Tenant | [optional] 
**sub_tenant_id** | **str** | The unique identifier for this Volume Configurations&#39;s Sub Tenant | [optional] 
**urn** | **str** | The Universal Resource Name, unique to this Volume Configuration | [optional] 
**online_status** | [**VolumeConfigurationOnlineStatus**](VolumeConfigurationOnlineStatus.md) |  | [optional] 
**error_code** | **str** | Error code returned from the object store | [optional] 
**error_message** | **str** | Error message returned from the object store | [optional] 
**time_of_last_error** | **datetime** | Timestamp of the last observed error. | [optional] 
**time_created** | **datetime** | The date &amp; time this Volume was created, in GDS | [optional] 
**created_by** | **str** | The creator of this Volume | [optional] 
**time_modified** | **datetime** | The date &amp; time this Volume was updated, in GDS | [optional] 
**modified_by** | **str** | The updator of this Volume | [optional] 
**object_store_settings** | [**ObjectStoreSettings**](ObjectStoreSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


