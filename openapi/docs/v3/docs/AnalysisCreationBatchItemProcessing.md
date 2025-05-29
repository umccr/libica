# AnalysisCreationBatchItemProcessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from libica.openapi.v3.models.analysis_creation_batch_item_processing import AnalysisCreationBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemProcessing from a JSON string
analysis_creation_batch_item_processing_instance = AnalysisCreationBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print(AnalysisCreationBatchItemProcessing.to_json())

# convert the object into a dict
analysis_creation_batch_item_processing_dict = analysis_creation_batch_item_processing_instance.to_dict()
# create an instance of AnalysisCreationBatchItemProcessing from a dict
analysis_creation_batch_item_processing_from_dict = AnalysisCreationBatchItemProcessing.from_dict(analysis_creation_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


