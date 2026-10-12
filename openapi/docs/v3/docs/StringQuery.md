# StringQuery

Filter on the description of the pipeline version. Only one of the fields can be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equals** | **str** | Matches records where the attribute value equals this string | [optional] 
**contains** | **str** | Matches records where the attribute value contains this string | [optional] 
**starts_with** | **str** | Matches records where the attribute value starts with this string | [optional] 

## Example

```python
from libica.openapi.v3.models.string_query import StringQuery

# TODO update the JSON string below
json = "{}"
# create an instance of StringQuery from a JSON string
string_query_instance = StringQuery.from_json(json)
# print the JSON string representation of the object
print(StringQuery.to_json())

# convert the object into a dict
string_query_dict = string_query_instance.to_dict()
# create an instance of StringQuery from a dict
string_query_from_dict = StringQuery.from_dict(string_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


