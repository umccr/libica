# CwlAnalysisOutputJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_json** | **str** | The output json of the CWL analysis. | 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_output_json import CwlAnalysisOutputJson

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisOutputJson from a JSON string
cwl_analysis_output_json_instance = CwlAnalysisOutputJson.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisOutputJson.to_json())

# convert the object into a dict
cwl_analysis_output_json_dict = cwl_analysis_output_json_instance.to_dict()
# create an instance of CwlAnalysisOutputJson from a dict
cwl_analysis_output_json_from_dict = CwlAnalysisOutputJson.from_dict(cwl_analysis_output_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


