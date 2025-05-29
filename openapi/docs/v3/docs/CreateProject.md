# CreateProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**short_description** | **str** |  | [optional] 
**information** | **str** | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**project_owner_id** | **str** | Owner of the project. Defaults to the current user. | [optional] 
**region_id** | **str** | The region of the project. All data and pipeline executions will reside in this region. | 
**billing_mode** | **str** | The billing mode of the project. It determines who pays for the costs linked to the project. | 
**data_sharing_enabled** | **bool** | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | 
**tags** | [**ProjectTag**](ProjectTag.md) |  | [optional] 
**storage_bundle_id** | **str** |  | 
**metadata_model_id** | **str** |  | [optional] 
**storage_configuration_id** | **str** | An optional storage configuration id to have self managed storage. | [optional] 
**storage_configuration_subfolder** | **str** | An optional subfolder that determines the object prefix of your self managed storage.  If not used, you will not be able to use this storage configuration for any future projects. | [optional] 
**analysis_priority** | **str** | Indicates the priority given to a project and its analyses within a single tenant, where MEDIUM is the default value. | [optional] [default to 'MEDIUM']

## Example

```python
from libica.openapi.v3.models.create_project import CreateProject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProject from a JSON string
create_project_instance = CreateProject.from_json(json)
# print the JSON string representation of the object
print(CreateProject.to_json())

# convert the object into a dict
create_project_dict = create_project_instance.to_dict()
# create an instance of CreateProject from a dict
create_project_from_dict = CreateProject.from_dict(create_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


