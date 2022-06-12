# AnalysisStepLogs

Contains references to the standard output (stdout) and standard error (stderr) log streams of an analysis step. In this object both log streams could be provided in 2 different formats: as a WebSocket stream URL or as an ICA Data reference. The status of the analysis step determines which format is provided: a WebSocket URL during step execution, a Data reference after step execution. Note however that an analysis step might not expose log streams at all, which would result in this object being empty. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**std_out_data** | [**Data**](Data.md) |  | [optional] 
**std_out_stream** | **str, none_type** | A WebSocket URL for reading the standard output log stream. Might be closed by ICA as soon as the analysis step execution has finished. | [optional] 
**std_err_data** | [**Data**](Data.md) |  | [optional] 
**std_err_stream** | **str, none_type** | A WebSocket URL for reading the standard error log stream. Might be closed by ICA as soon as the analysis step execution has finished. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


