# BundlePipelineList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BundlePipeline]**](BundlePipeline.md) |  | 

## Example

```python
from libica.openapi.v3.models.bundle_pipeline_list import BundlePipelineList

# TODO update the JSON string below
json = "{}"
# create an instance of BundlePipelineList from a JSON string
bundle_pipeline_list_instance = BundlePipelineList.from_json(json)
# print the JSON string representation of the object
print(BundlePipelineList.to_json())

# convert the object into a dict
bundle_pipeline_list_dict = bundle_pipeline_list_instance.to_dict()
# create an instance of BundlePipelineList from a dict
bundle_pipeline_list_from_dict = BundlePipelineList.from_dict(bundle_pipeline_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


