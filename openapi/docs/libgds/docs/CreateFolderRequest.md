# CreateFolderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Folder name, unique to this path, for the folder being created | 
**folder_path** | **str** | Path from the root folder to the location for the folder being created; must start and end with &#39;/&#39; | [optional] 
**volume_id** | **str** | The unique identifier for this Folder&#39;s Volume | [optional] 
**volume_name** | **str** | The unique name for the Folder&#39;s Volume | [optional] 
**metadata** | [**object**](.md) | Metadata about this folder and its contents | [optional] 
**acl** | **list[str]** | Optional array to replace the acl on the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


