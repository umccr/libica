# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**urn** | **str** | The URN of the project. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**name** | **str** |  | 
**active** | **bool** | Indicates whether the project is active or hidden. | 
**base_enabled** | **bool** | Indicates whether the project is base enabled. | [optional] 
**short_description** | **str** |  | [optional] 
**information** | **str** | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**region** | [**Region**](Region.md) |  | 
**billing_mode** | **str** | The billing mode of the project. It determines who pays for the costs linked to the project. | 
**data_sharing_enabled** | **bool** | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | [optional] 
**tags** | [**ProjectTag**](ProjectTag.md) |  | 
**storage_bundle** | [**StorageBundle**](StorageBundle.md) |  | [optional] 
**self_managed_storage_configuration** | [**StorageConfiguration**](StorageConfiguration.md) |  | [optional] 
**analysis_priority** | **str** | Indicates the priority given to a project and its analyses within a single tenant. Note that for a PUT call, when not providing a value for this attribute (null value or absent attribute), the persisted value will not change. | [optional] 
**metadata_model** | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 
**project_owner** | **str** | projectOwner is the current project owner, ownerId is the original project creator. These can be different because you can transfer ownership of a project. | [optional] 

## Example

```python
from libica.openapi.v3.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


