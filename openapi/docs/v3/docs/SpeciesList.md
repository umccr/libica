# SpeciesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Species]**](Species.md) |  | 

## Example

```python
from libica.openapi.v3.models.species_list import SpeciesList

# TODO update the JSON string below
json = "{}"
# create an instance of SpeciesList from a JSON string
species_list_instance = SpeciesList.from_json(json)
# print the JSON string representation of the object
print(SpeciesList.to_json())

# convert the object into a dict
species_list_dict = species_list_instance.to_dict()
# create an instance of SpeciesList from a dict
species_list_from_dict = SpeciesList.from_dict(species_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


