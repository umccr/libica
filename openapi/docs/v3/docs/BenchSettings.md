# BenchSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_compatible** | **bool** |  | 
**access** | [**DockerImageAccess**](DockerImageAccess.md) |  | 

## Example

```python
from libica.openapi.v3.models.bench_settings import BenchSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BenchSettings from a JSON string
bench_settings_instance = BenchSettings.from_json(json)
# print the JSON string representation of the object
print(BenchSettings.to_json())

# convert the object into a dict
bench_settings_dict = bench_settings_instance.to_dict()
# create an instance of BenchSettings from a dict
bench_settings_from_dict = BenchSettings.from_dict(bench_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


