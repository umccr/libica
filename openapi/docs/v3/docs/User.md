# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**username** | **str** |  | 
**email** | **str** |  | 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**active** | **bool** |  | 
**tenant_administrator** | **bool** |  | 
**job_title** | **str** |  | [optional] 
**greeting** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**email_verified** | **bool** |  | 
**two_factor_authentication** | **bool** |  | 
**country** | [**Country**](Country.md) |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from libica.openapi.v3.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


