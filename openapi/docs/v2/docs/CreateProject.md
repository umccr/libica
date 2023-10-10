# CreateProject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**region_id** | **str** | The region of the project. All data and pipeline executions will reside in this region. | 
**billing_mode** | **str** | The billing mode of the project. It determines who pays for the costs linked to the project. | 
**data_sharing_enabled** | **bool** | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | 
**storage_bundle_id** | **str** |  | 
**short_description** | **str, none_type** |  | [optional] 
**information** | **str, none_type** | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**project_owner_id** | **str, none_type** | Owner of the project. Defaults to the current user. | [optional] 
**tags** | [**ProjectTag**](ProjectTag.md) |  | [optional] 
**metadata_model_id** | **str, none_type** |  | [optional] 
**storage_configuration_id** | **str, none_type** | An optional storage configuration id to have self managed storage. | [optional] 
**storage_configuration_subfolder** | **str, none_type** | An optional subfolder that determines the object prefix of your self managed storage.  If not used, you will not be able to use this storage configuration for any future projects. | [optional] 
**analysis_priority** | **str, none_type** | Indicates the priority given to a project and its analyses within a single tenant, where MEDIUM is the default value. | [optional]  if omitted the server will use the default value of "MEDIUM"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


