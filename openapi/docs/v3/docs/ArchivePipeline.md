# ArchivePipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | An optional message from the pipeline developer | [optional] 

## Example

```python
from libica.openapi.v3.models.archive_pipeline import ArchivePipeline

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivePipeline from a JSON string
archive_pipeline_instance = ArchivePipeline.from_json(json)
# print the JSON string representation of the object
print(ArchivePipeline.to_json())

# convert the object into a dict
archive_pipeline_dict = archive_pipeline_instance.to_dict()
# create an instance of ArchivePipeline from a dict
archive_pipeline_from_dict = ArchivePipeline.from_dict(archive_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


