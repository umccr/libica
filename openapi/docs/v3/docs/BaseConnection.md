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

## Example

```python
from libica.openapi.v3.models.base_connection import BaseConnection

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConnection from a JSON string
base_connection_instance = BaseConnection.from_json(json)
# print the JSON string representation of the object
print(BaseConnection.to_json())

# convert the object into a dict
base_connection_dict = base_connection_instance.to_dict()
# create an instance of BaseConnection from a dict
base_connection_from_dict = BaseConnection.from_dict(base_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


