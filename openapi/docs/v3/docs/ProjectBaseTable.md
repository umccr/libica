# ProjectBaseTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the table which should be used in writing queries | 
**description** | **str** | The description of the table | [optional] 
**type** | **str** | The type of the table | 
**status** | **str** | The status of the table | 
**number_of_records** | **int** | The number of record in the table | [optional] 
**data_size** | **int** | The amount of Data contained in this table in bytes | [optional] 

## Example

```python
from libica.openapi.v3.models.project_base_table import ProjectBaseTable

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBaseTable from a JSON string
project_base_table_instance = ProjectBaseTable.from_json(json)
# print the JSON string representation of the object
print(ProjectBaseTable.to_json())

# convert the object into a dict
project_base_table_dict = project_base_table_instance.to_dict()
# create an instance of ProjectBaseTable from a dict
project_base_table_from_dict = ProjectBaseTable.from_dict(project_base_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


