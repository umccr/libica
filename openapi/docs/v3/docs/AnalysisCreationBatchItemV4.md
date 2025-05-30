# AnalysisCreationBatchItemV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**AnalysisCreationBatchItemRequest**](AnalysisCreationBatchItemRequest.md) |  | 
**processing** | [**AnalysisCreationBatchItemProcessing**](AnalysisCreationBatchItemProcessing.md) |  | 
**created_analysis** | [**AnalysisV4**](AnalysisV4.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_v4 import AnalysisCreationBatchItemV4

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemV4 from a JSON string
analysis_creation_batch_item_v4_instance = AnalysisCreationBatchItemV4.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemV4.to_json())

# convert the object into a dict
analysis_creation_batch_item_v4_dict = analysis_creation_batch_item_v4_instance.to_dict()
# create an instance of AnalysisCreationBatchItemV4 from a dict
analysis_creation_batch_item_v4_from_dict = AnalysisCreationBatchItemV4.from_dict(analysis_creation_batch_item_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


