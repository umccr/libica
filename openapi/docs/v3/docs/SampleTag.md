# SampleTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** |  | 
**user_tags** | **List[str]** |  | 
**connector_tags** | **List[str]** |  | 
**run_in_tags** | **List[str]** |  | 

## Example

```python
from libica.openapi.v3.models.sample_tag import SampleTag

# TODO update the JSON string below
json = "{}"
# create an instance of SampleTag from a JSON string
sample_tag_instance = SampleTag.from_json(json)
# print the JSON string representation of the object
print(SampleTag.to_json())

# convert the object into a dict
sample_tag_dict = sample_tag_instance.to_dict()
# create an instance of SampleTag from a dict
sample_tag_from_dict = SampleTag.from_dict(sample_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


