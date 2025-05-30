# Sample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the sample | 
**description** | **str** | The description of the sample | [optional] 
**tags** | [**SampleTag**](SampleTag.md) |  | 
**region** | [**Region**](Region.md) |  | 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 
**status** | **str** |  | 
**metadata_valid** | **bool** | Whether the metadata is valid | 
**metadata** | [**List[MetadataField]**](MetadataField.md) | The metadata of the sample | 
**sequencing_runs** | [**List[SequencingRun]**](SequencingRun.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.sample import Sample

# TODO update the JSON string below
json = "{}"
# create an instance of Sample from a JSON string
sample_instance = Sample.from_json(json)
# print the JSON string representation of the object
print(Sample.to_json())

# convert the object into a dict
sample_dict = sample_instance.to_dict()
# create an instance of Sample from a dict
sample_from_dict = Sample.from_dict(sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


