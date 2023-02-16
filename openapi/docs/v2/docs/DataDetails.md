# DataDetails

The details of this data. This object is optional because it is possible that these details are deleted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**tenant_id** | **str** |  | 
**owning_project_id** | **str** |  | 
**name** | **str** | The name of the file/folder as it was uploaded. | 
**status** | **str** |  | 
**tags** | [**DataTag**](DataTag.md) |  | 
**data_type** | **str** |  | 
**creator_id** | **str, none_type** |  | [optional] 
**tenant_name** | **str, none_type** |  | [optional] 
**owning_project_name** | **str, none_type** |  | [optional] 
**path** | **str, none_type** | The user friendly path of the parent of this data. | [optional] 
**file_size_in_bytes** | **int, none_type** | The size of the file in bytes. Folders do not have a size. | [optional] 
**format** | [**DataFormat**](DataFormat.md) |  | [optional] 
**object_e_tag** | **str, none_type** | The file&#39;s ETag, as received from the cloud provider. Not to be confused with the ETag reponse header of this API. | [optional] 
**stored_for_the_first_time_at** | **datetime, none_type** | Specifies when the data object was stored for the first time | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**will_be_archived_at** | **datetime, none_type** | Specifies when the data object will be archived. | [optional] 
**will_be_deleted_at** | **datetime, none_type** | Specifies when the data object will be deleted. | [optional] 
**sequencing_run** | [**SequencingRun**](SequencingRun.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


