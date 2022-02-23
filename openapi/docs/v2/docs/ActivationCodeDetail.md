# ActivationCodeDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pipeline_bundle** | [**PipelineBundle**](PipelineBundle.md) |  | 
**usages** | [**[ActivationCodeDetailUsage]**](ActivationCodeDetailUsage.md) |  | 
**allowed_slots** | **int, none_type** | The allowed slot within this code, empty means unlimited | [optional] 
**used_slots** | **int, none_type** | Indicates how many slots can are used. | [optional] 
**moved_slots** | **int, none_type** | The slots that where moved to another activation code | [optional] 
**original_slots** | **int, none_type** | The assigned allowed slot within this code, empty means unlimited | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


