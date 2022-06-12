# VolumeFileListRequest

Request for listing files within a volume
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_id** | **str** | Volume identifier | [optional] 
**file_ids** | **list[str]** | File identifiers to list | [optional] 
**include_presigned_url** | **bool** | Optional parameter that returns presigned URL for each file when set to true | [optional] 
**presigned_url_mode** | **str** | Optional parameter to specify presigned url&#39;s content-disposition. If not specified, the browser will determine the default behavior.  Possible values: Attachment, Inline, Browser | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


