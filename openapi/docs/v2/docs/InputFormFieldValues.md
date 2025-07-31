# InputFormFieldValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**values** | **[str, none_type], none_type** | Use &#39;values&#39; for all fields except data fields. Use string values to avoid rounding of numbers with a high precision. &#39;&#39; values for textbox type fields will be treated as null. | [optional] 
**data_values** | [**[InputFormData], none_type**](InputFormData.md) | Use &#39;dataValues&#39; for data fields. | [optional] 
**external_data_values** | [**[AnalysisInputExternalData], none_type**](AnalysisInputExternalData.md) | Use &#39;externalDataValues&#39; for external data | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


