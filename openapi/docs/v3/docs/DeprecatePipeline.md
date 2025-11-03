# DeprecatePipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | An optional message from the pipeline developer | [optional] 

## Example

```python
from libica.openapi.v3.models.deprecate_pipeline import DeprecatePipeline

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatePipeline from a JSON string
deprecate_pipeline_instance = DeprecatePipeline.from_json(json)
# print the JSON string representation of the object
print(DeprecatePipeline.to_json())

# convert the object into a dict
deprecate_pipeline_dict = deprecate_pipeline_instance.to_dict()
# create an instance of DeprecatePipeline from a dict
deprecate_pipeline_from_dict = DeprecatePipeline.from_dict(deprecate_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


