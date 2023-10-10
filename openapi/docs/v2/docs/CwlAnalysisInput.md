# CwlAnalysisInput

This object contains a \"oneOf\" construct. With the \"objectType\" attribute you can specify which object type you want to provide. Use \"STRUCTURED\" for type \"CreateAnalysisStructuredInput\" or use \"JSON\" for type \"CreateAnalysisJsonInput\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** |  | 
**parameters** | [**[AnalysisParameterInput], none_type**](AnalysisParameterInput.md) |  | [optional] 
**reference_data_parameters** | [**[AnalysisReferenceDataParameter], none_type**](AnalysisReferenceDataParameter.md) |  | [optional] 
**data_ids** | **[str]** |  | [optional] 
**mounts** | [**[AnalysisInputDataMount], none_type**](AnalysisInputDataMount.md) |  | [optional] 
**external_data** | [**[AnalysisInputExternalData], none_type**](AnalysisInputExternalData.md) |  | [optional] 
**inputs** | [**[AnalysisDataInput]**](AnalysisDataInput.md) |  | [optional] 
**input_json** | **str** | Contains the input JSON, as an escaped JSON String. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


