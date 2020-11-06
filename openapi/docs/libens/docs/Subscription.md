# Subscription

Details for an Event Notification Service subscription
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the subscription | [optional] 
**urn** | **str** | URN of the subscription | [optional] 
**type** | **str** | Type of event the subscription matches | [optional] 
**actions** | **list[str]** | Types of actions the subscription matches for the event type | [optional] 
**filter_expression** | **str** | JSON-structured filter expression for events matching the subscription | [optional] 
**name** | **str** | Name of the subscription | [optional] 
**description** | **str** | Optional description for the subscription | [optional] 
**delivery_target** | [**DeliveryTarget**](DeliveryTarget.md) |  | [optional] 
**match_identities** | **list[str]** | ACL Identities for events the subscription matches | [optional] 
**acl** | **list[str]** | The list of identities that have access to this subscription | [optional] 
**tenant_id** | **str** | Tenant id of the subscription owner | [optional] 
**created_by_user_id** | **str** | User id for the creator of the subscription | [optional] 
**time_created** | **datetime** | Timestamp when the subscription was created | [optional] 
**deleted_by_user_id** | **str** | Id of the user who deleted the subscription, if applicable | [optional] 
**time_deleted** | **datetime** | Timestamp when the subscription was deleted, if applicable | [optional] 
**is_deleted** | **bool** | Whether or not the subscription has been deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


