# DateQuery

Filter on the last used date of the pipeline version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **datetime** | Matches records where the attribute value is before this date | [optional] 
**after** | **datetime** | Matches records where the attribute value is after this date | [optional] 
**empty** | **bool** | Matches records where the attribute value is empty (null) | [optional] 

## Example

```python
from libica.openapi.v3.models.date_query import DateQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DateQuery from a JSON string
date_query_instance = DateQuery.from_json(json)
# print the JSON string representation of the object
print(DateQuery.to_json())

# convert the object into a dict
date_query_dict = date_query_instance.to_dict()
# create an instance of DateQuery from a dict
date_query_from_dict = DateQuery.from_dict(date_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


