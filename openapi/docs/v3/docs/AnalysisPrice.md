# AnalysisPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the analysis price | [optional] 
**currency** | **str** | The currency of the analysis price | [optional] [default to 'iCredit']

## Example

```python
from libica.openapi.v3.models.analysis_price import AnalysisPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisPrice from a JSON string
analysis_price_instance = AnalysisPrice.from_json(json)
# print the JSON string representation of the object
print(AnalysisPrice.to_json())

# convert the object into a dict
analysis_price_dict = analysis_price_instance.to_dict()
# create an instance of AnalysisPrice from a dict
analysis_price_from_dict = AnalysisPrice.from_dict(analysis_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


