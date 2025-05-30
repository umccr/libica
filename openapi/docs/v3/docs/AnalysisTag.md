# AnalysisTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** | Technical tags | 
**user_tags** | **List[str]** | User tags | 
**reference_tags** | **List[str]** | Reference tags | 

## Example

```python
from libica.openapi.v3.models.analysis_tag import AnalysisTag

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTag from a JSON string
analysis_tag_instance = AnalysisTag.from_json(json)
# print the JSON string representation of the object
print(AnalysisTag.to_json())

# convert the object into a dict
analysis_tag_dict = analysis_tag_instance.to_dict()
# create an instance of AnalysisTag from a dict
analysis_tag_from_dict = AnalysisTag.from_dict(analysis_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


