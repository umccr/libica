# CreateAnalysisTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[Optional[str]]** | Technical tags | [optional] 
**user_tags** | **List[Optional[str]]** | User tags | [optional] 
**reference_tags** | **List[Optional[str]]** | Reference tags | [optional] 

## Example

```python
from libica.openapi.v3.models.create_analysis_tag import CreateAnalysisTag

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnalysisTag from a JSON string
create_analysis_tag_instance = CreateAnalysisTag.from_json(json)
# print the JSON string representation of the object
print(CreateAnalysisTag.to_json())

# convert the object into a dict
create_analysis_tag_dict = create_analysis_tag_instance.to_dict()
# create an instance of CreateAnalysisTag from a dict
create_analysis_tag_from_dict = CreateAnalysisTag.from_dict(create_analysis_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


