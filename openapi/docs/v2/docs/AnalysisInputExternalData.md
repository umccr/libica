# AnalysisInputExternalData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 
**mount_path** | **str, none_type** | The mount path is the location where the input file will be located on the machine that is running the pipeline. The use of a relative path is encouraged, but an absolute path is also allowed. The path should end with the file name, which may differ from the original input data. | [optional] 
**s3_details** | [**AnalysisS3DataDetails**](AnalysisS3DataDetails.md) |  | [optional] 
**basespace_details** | [**AnalysisBaseSpaceDataDetails**](AnalysisBaseSpaceDataDetails.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


