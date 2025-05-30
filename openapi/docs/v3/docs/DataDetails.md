# DataDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**creator_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**owning_project_id** | **str** |  | 
**owning_project_name** | **str** |  | [optional] 
**name** | **str** | The name of the file/folder as it was uploaded. | 
**path** | **str** | The user friendly path of the parent of this data. | [optional] 
**file_size_in_bytes** | **int** | The size of the file in bytes. Folders do not have a size. | [optional] 
**status** | **str** |  | 
**tags** | [**DataTag**](DataTag.md) |  | 
**format** | [**DataFormat**](DataFormat.md) |  | [optional] 
**data_type** | **str** |  | 
**object_e_tag** | **str** | The file&#39;s ETag, as received from the cloud provider. Not to be confused with the ETag reponse header of this API. | [optional] 
**stored_for_the_first_time_at** | **datetime** | Specifies when the data object was stored for the first time | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**application** | [**ApplicationV4**](ApplicationV4.md) |  | [optional] 
**will_be_archived_at** | **datetime** | Specifies when the data object will be archived. | [optional] 
**will_be_deleted_at** | **datetime** | Specifies when the data object will be deleted. | [optional] 
**sequencing_run** | [**SequencingRun**](SequencingRun.md) |  | [optional] 

## Example

```python
from libica.openapi.v3.models.data_details import DataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DataDetails from a JSON string
data_details_instance = DataDetails.from_json(json)
# print the JSON string representation of the object
print(DataDetails.to_json())

# convert the object into a dict
data_details_dict = data_details_instance.to_dict()
# create an instance of DataDetails from a dict
data_details_from_dict = DataDetails.from_dict(data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


