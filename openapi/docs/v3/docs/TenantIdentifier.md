# TenantIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The unique name of the tenant. | [optional] 

## Example

```python
from libica.openapi.v3.models.tenant_identifier import TenantIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIdentifier from a JSON string
tenant_identifier_instance = TenantIdentifier.from_json(json)
# print the JSON string representation of the object
print(TenantIdentifier.to_json())

# convert the object into a dict
tenant_identifier_dict = tenant_identifier_instance.to_dict()
# create an instance of TenantIdentifier from a dict
tenant_identifier_from_dict = TenantIdentifier.from_dict(tenant_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


