# BundlePipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline** | [**PipelineV3**](PipelineV3.md) |  | 
**bundle_id** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.bundle_pipeline import BundlePipeline

# TODO update the JSON string below
json = "{}"
# create an instance of BundlePipeline from a JSON string
bundle_pipeline_instance = BundlePipeline.from_json(json)
# print the JSON string representation of the object
print(BundlePipeline.to_json())

# convert the object into a dict
bundle_pipeline_dict = bundle_pipeline_instance.to_dict()
# create an instance of BundlePipeline from a dict
bundle_pipeline_from_dict = BundlePipeline.from_dict(bundle_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


