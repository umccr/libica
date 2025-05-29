# InputFormS3DataDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_credentials_id** | **str** | The storage credentials with the S3 access key. | [optional] 

## Example

```python
from libica.openapi.v3.models.input_form_s3_data_details import InputFormS3DataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InputFormS3DataDetails from a JSON string
input_form_s3_data_details_instance = InputFormS3DataDetails.from_json(json)
# print the JSON string representation of the object
print(InputFormS3DataDetails.to_json())

# convert the object into a dict
input_form_s3_data_details_dict = input_form_s3_data_details_instance.to_dict()
# create an instance of InputFormS3DataDetails from a dict
input_form_s3_data_details_from_dict = InputFormS3DataDetails.from_dict(input_form_s3_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


