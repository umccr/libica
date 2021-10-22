# CreateVolumeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the volume | 
**volume_configuration_name** | **str** | Unique name of the volume configuration to use | [optional] 
**root_key_prefix** | **str** | The base bucket location for volumes associated with custom VolumeConfigurations. If not provided, the given volume Name is used.  If provided, it must start with the VolumeConfiguration&#39;s keyprefix and end with a /.  To create a volume representing the root of a bucket, use the value &#39;/&#39;. | [optional] 
**metadata** | [**object**](.md) | Metadata about this volume and its contents | [optional] 
**life_cycle** | [**VolumeLifeCycleSettings**](VolumeLifeCycleSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


