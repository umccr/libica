# LoadDataInBaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | ID of the data to load into the table | 
**allow_jagged_rows** | **bool, none_type** | Enable to accept rows that are missing trailing optional columns. Missing values will be treated as nulls. | [optional]  if omitted the server will use the default value of False
**allow_quoted_newlines** | **bool, none_type** | Enable to include newlines contained in quoted data sections in the cell’s value. When disabled, newlines will signal a new row | [optional]  if omitted the server will use the default value of False
**delimiter** | **str, none_type** | field delimiter | [optional]  if omitted the server will use the default value of ","
**encoding** | **str, none_type** | Encoding | [optional]  if omitted the server will use the default value of "UTF8"
**force_load** | **bool, none_type** | When false (default): the data will not be loaded if it was already previously loaded to table ; when true, the data will be loaded even if already loaded in the past | [optional]  if omitted the server will use the default value of False
**header_rows_to_skip** | **int, none_type** | number of rows to skip (usually for headers) | [optional]  if omitted the server will use the default value of 1
**ignore_unknown_values** | **bool** | When enabled, rows with extra column values that do not match the schema will be ignored and will not be loaded into the table | [optional]  if omitted the server will use the default value of False
**include_references** | **bool, none_type** | Include references | [optional]  if omitted the server will use the default value of True
**include_data_reference** | **bool, none_type** | Include Data Reference | [optional]  if omitted the server will use the default value of True
**include_sample_reference** | **bool, none_type** | Include Sample Reference | [optional]  if omitted the server will use the default value of True
**include_pipeline_reference** | **bool, none_type** | Include Pipeline Reference | [optional]  if omitted the server will use the default value of True
**include_pipeline_execution_reference** | **bool, none_type** | Include Pipeline Execution Reference | [optional]  if omitted the server will use the default value of True
**include_tenant_reference** | **bool, none_type** | Include Tenant Reference | [optional]  if omitted the server will use the default value of True
**null_marker** | **str, none_type** | Specifies a string that represents a null value in a CSV/TSV file. | [optional] 
**number_of_errors_allowed** | **int, none_type** | The maximum number of bad records that Base can ignore when running the job | [optional]  if omitted the server will use the default value of 0
**quote** | **str, none_type** | The value that is used to quote data sections in a CSV/TSV file | [optional] 
**write_preference** | **str, none_type** | specifies how to write data in the table. | [optional]  if omitted the server will use the default value of "APPENDTOTABLE"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


