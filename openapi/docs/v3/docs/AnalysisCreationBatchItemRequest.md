# AnalysisCreationBatchItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_reference** | **str** |  | 
**pipeline_id** | **str** | The pipeline for which an analysis will be created. | 
**tags** | [**AnalysisTag**](AnalysisTag.md) |  | 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_request import AnalysisCreationBatchItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemRequest from a JSON string
analysis_creation_batch_item_request_instance = AnalysisCreationBatchItemRequest.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemRequest.to_json())

# convert the object into a dict
analysis_creation_batch_item_request_dict = analysis_creation_batch_item_request_instance.to_dict()
# create an instance of AnalysisCreationBatchItemRequest from a dict
analysis_creation_batch_item_request_from_dict = AnalysisCreationBatchItemRequest.from_dict(analysis_creation_batch_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


