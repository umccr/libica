# WorkflowArgument

Argument definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the argument key | 
**value** | **str** | A simple string value for the argument. Cannot provide both Value and Json at the same time. | [optional] 
**json** | [**object**](.md) | A JSON value for the argument. Cannot provide both Value and Json at the same time. | [optional] 
**options** | **str** | Comma separated list of options for the argument: Required, Overridable, Writable, Json, Optional, ReadOnly, Final  Some combinations of options are considered errors, like Required/Optional, Overridable/Final, Writable/ReadOnly, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


