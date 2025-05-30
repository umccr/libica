# PipelineFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PipelineFile]**](PipelineFile.md) |  | 

## Example

```python
from libica.openapi.v3.models.pipeline_file_list import PipelineFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineFileList from a JSON string
pipeline_file_list_instance = PipelineFileList.from_json(json)
# print the JSON string representation of the object
print(PipelineFileList.to_json())

# convert the object into a dict
pipeline_file_list_dict = pipeline_file_list_instance.to_dict()
# create an instance of PipelineFileList from a dict
pipeline_file_list_from_dict = PipelineFileList.from_dict(pipeline_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


