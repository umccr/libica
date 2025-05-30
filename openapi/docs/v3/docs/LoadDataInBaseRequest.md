# LoadDataInBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_quoted_newlines** | **bool** | Enable to include newlines contained in quoted data sections in the cell’s value. When disabled, newlines will signal a new row | [optional] [default to False]
**data_id** | **str** | ID of the data to load into the table | 
**delimiter** | **str** | field delimiter | [optional] [default to ',']
**encoding** | **str** | Encoding | [optional] [default to 'UTF8']
**force_load** | **bool** | When false (default): the data will not be loaded if it was already previously loaded to table ; when true, the data will be loaded even if already loaded in the past | [optional] [default to False]
**header_rows_to_skip** | **int** | number of rows to skip (usually for headers) | [optional] [default to 1]
**ignore_unknown_values** | **bool** | When enabled, rows with extra column values that do not match the schema will be ignored and will not be loaded into the table, rows with too few values will receive default value null | [optional] [default to False]
**include_references** | **bool** | Include references | [optional] [default to True]
**include_data_reference** | **bool** | Include Data Reference | [optional] [default to True]
**include_sample_reference** | **bool** | Include Sample Reference | [optional] [default to True]
**include_pipeline_reference** | **bool** | Include Pipeline Reference | [optional] [default to True]
**include_pipeline_execution_reference** | **bool** | Include Pipeline Execution Reference | [optional] [default to True]
**include_tenant_reference** | **bool** | Include Tenant Reference | [optional] [default to True]
**null_marker** | **str** | Specifies a string that represents a null value in a CSV/TSV file. | [optional] 
**number_of_errors_allowed** | **int** | The maximum number of bad records that Base can ignore when running the job | [optional] [default to 0]
**quote** | **str** | The value that is used to quote data sections in a CSV/TSV file | [optional] 
**write_preference** | **str** | specifies how to write data in the table. | [optional] [default to 'APPENDTOTABLE']

## Example

```python
from libica.openapi.v3.models.load_data_in_base_request import LoadDataInBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoadDataInBaseRequest from a JSON string
load_data_in_base_request_instance = LoadDataInBaseRequest.from_json(json)
# print the JSON string representation of the object
print(LoadDataInBaseRequest.to_json())

# convert the object into a dict
load_data_in_base_request_dict = load_data_in_base_request_instance.to_dict()
# create an instance of LoadDataInBaseRequest from a dict
load_data_in_base_request_from_dict = LoadDataInBaseRequest.from_dict(load_data_in_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


