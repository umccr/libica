# CwlAnalysisInputJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_json** | **str** | The input json of the CWL analysis. | 

## Example

```python
from libica.openapi.v3.models.cwl_analysis_input_json import CwlAnalysisInputJson

# TODO update the JSON string below
json = "{}"
# create an instance of CwlAnalysisInputJson from a JSON string
cwl_analysis_input_json_instance = CwlAnalysisInputJson.from_json(json)
# print the JSON string representation of the object
print(CwlAnalysisInputJson.to_json())

# convert the object into a dict
cwl_analysis_input_json_dict = cwl_analysis_input_json_instance.to_dict()
# create an instance of CwlAnalysisInputJson from a dict
cwl_analysis_input_json_from_dict = CwlAnalysisInputJson.from_dict(cwl_analysis_input_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


