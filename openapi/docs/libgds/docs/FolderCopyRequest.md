# FolderCopyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_parent_folder_id** | **str** | The parent folder into which the source folder will be copied. | 
**destination_folder_name** | **str** | A new name for the destination folder. Required if target parent folder is the same as the destination folder.  When optional and not provided, the source folder name is used as the destination folder name. | [optional] 
**metadata_to_copy** | **list[str]** | List of metadata to be copied/kept | [optional] 
**metadata_to_update** | [**object**](.md) | Modifies the contents of existing metadata | [optional] 
**metadata_items_to_add** | [**object**](.md) | Add an item to a metadata with array type | [optional] 
**metadata_items_to_delete** | [**object**](.md) | Delete an item from a metadata with array type | [optional] 
**duplicate_file_action** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


