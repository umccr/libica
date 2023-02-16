# ActivationCodeDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**allowed_slots** | **int** | The allowed slot within this code, -1 means unlimited | 
**used_slots** | **int** | Indicates how many slots can are used. | 
**moved_slots** | **int** | The slots that where moved to another activation code | 
**original_slots** | **int** | The assigned allowed slot within this code, -1 means unlimited | 
**pipeline_bundle** | [**PipelineBundle**](PipelineBundle.md) |  | 
**usages** | [**[ActivationCodeDetailUsage]**](ActivationCodeDetailUsage.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


