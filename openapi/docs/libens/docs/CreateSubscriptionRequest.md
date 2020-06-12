# CreateSubscriptionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Event type which will be subscribed to | 
**actions** | **list[str]** | Actions which will be subscribed to for the event type | [optional] 
**name** | **str** | Name of the subscription | 
**description** | **str** | Optional description for the subscription | [optional] 
**filter_expression** | **str** | JSON-structured filter expression for events matching the subscription | [optional] 
**delivery_target** | [**DeliveryTarget**](DeliveryTarget.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


