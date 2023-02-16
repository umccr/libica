# BulkFolderMetadataUpdateRequest

Request to bulk update metadata on folders and sub files.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | Folder unique id. | 
**file_status** | **str** | File status to filter on. | [optional] 
**parent_folder_metadata_updates** | [**MetadataUpdateRequest**](MetadataUpdateRequest.md) |  | [optional] 
**children_folders_updates** | [**MetadataUpdateRequest**](MetadataUpdateRequest.md) |  | [optional] 
**children_files_updates** | [**MetadataUpdateRequest**](MetadataUpdateRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


