# FileListCopyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_volume_id** | **str** | The volume where the source files are copied from. | 
**destination_folder_id** | **str** | The folder into which the source files will be copied. | 
**ids** | **list[str]** | List of files ids to copy | 
**metadata_to_copy** | **list[str]** | List of metadata to be copied/kept | [optional] 
**metadata_to_update** | [**object**](.md) | Modifies the contents of existing metadata | [optional] 
**metadata_items_to_add** | [**object**](.md) | Add an item to a metadata with array type | [optional] 
**metadata_items_to_delete** | [**object**](.md) | Delete an item from a metadata with array type | [optional] 
**duplicate_file_action** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


