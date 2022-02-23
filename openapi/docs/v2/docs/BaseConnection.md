# BaseConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator** | **str** | Specifies the supported snowflake authenticator to use. Currently &#39;oauth&#39; only is supported | 
**access_token** | **str** | Specifies the OAuth token to use for authentication | 
**dns_name** | **str** | snowflake dns name. Usually something like &#39;&lt;&lt;account&gt;&gt;.snowflakecomputing.com&#39; | 
**user_principal_name** | **str** | Specifies the user principal name. This is required for some snowflake client (snowSQL for instance) | 
**database_name** | **str** | Specifies the database name bound to the project specified | 
**schema_name** | **str** | Specifies the schema name bound to the project specified | 
**warehouse_name** | **str** | Specifies the warehouse name bound to the project specified | 
**role_name** | **str** | Specifies the role name bound to the project specified | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


