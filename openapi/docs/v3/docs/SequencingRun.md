# SequencingRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**instrument_run_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from libica.openapi.v3.models.sequencing_run import SequencingRun

# TODO update the JSON string below
json = "{}"
# create an instance of SequencingRun from a JSON string
sequencing_run_instance = SequencingRun.from_json(json)
# print the JSON string representation of the object
print(SequencingRun.to_json())

# convert the object into a dict
sequencing_run_dict = sequencing_run_instance.to_dict()
# create an instance of SequencingRun from a dict
sequencing_run_from_dict = SequencingRun.from_dict(sequencing_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


