# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** |  | 
**active** | **bool** | Indicates whether the project is active or hidden. | 
**region** | [**Region**](Region.md) |  | 
**billing_mode** | **str** | The billing mode of the project. It determines who pays for the costs linked to the project. | 
**tags** | [**ProjectTag**](ProjectTag.md) |  | 
**tenant_name** | **str, none_type** |  | [optional] 
**urn** | **str, none_type** | The URN of the project. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**base_enabled** | **bool, none_type** | Indicates whether the project is base enabled. | [optional] 
**short_description** | **str, none_type** |  | [optional] 
**information** | **str, none_type** | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**data_sharing_enabled** | **bool, none_type** | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | [optional] 
**storage_bundle** | [**StorageBundle**](StorageBundle.md) |  | [optional] 
**self_managed_storage_configuration** | [**StorageConfiguration**](StorageConfiguration.md) |  | [optional] 
**analysis_priority** | **str, none_type** | Indicates the priority given to a project and its analyses within a single tenant. Note that for a PUT call, when not providing a value for this attribute (null value or absent attribute), the persisted value will not change. | [optional] 
**metadata_model** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


