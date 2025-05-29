# AnalysisCreationBatchItemV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**AnalysisCreationBatchItemRequest**](AnalysisCreationBatchItemRequest.md) |  | 
**processing** | [**AnalysisCreationBatchItemProcessing**](AnalysisCreationBatchItemProcessing.md) |  | 
**created_analysis** | [**AnalysisV3**](AnalysisV3.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_v3 import AnalysisCreationBatchItemV3

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemV3 from a JSON string
analysis_creation_batch_item_v3_instance = AnalysisCreationBatchItemV3.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemV3.to_json())

# convert the object into a dict
analysis_creation_batch_item_v3_dict = analysis_creation_batch_item_v3_instance.to_dict()
# create an instance of AnalysisCreationBatchItemV3 from a dict
analysis_creation_batch_item_v3_from_dict = AnalysisCreationBatchItemV3.from_dict(analysis_creation_batch_item_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


