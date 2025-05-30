# AwsTempCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | The S3 access key. | 
**secret_key** | **str** | The S3 secret key. | 
**session_token** | **str** | The S3 session token. | 
**region** | **str** | The S3 region. | 
**bucket** | **str** | The S3 bucket name. | 
**object_prefix** | **str** | The S3 object prefix these temporary credentials will give access to. | 
**server_side_encryption_algorithm** | **str** | Used to specify the type of server-side encryption (SSE) to be used on the object provider. This value is used to determine the Amazon S3 header \&quot;x-amz-server-side-encryption\&quot; value. For example, specify \&quot;AES256\&quot; for SSE-S3, or \&quot;AWS:KMS\&quot; for SSE-KMS. By default if none is specified, \&quot;AES256\&quot; will be used. | [optional] 
**server_side_encryption_key** | **str** | Used to specify the server-side encryption key that might be associated with the specified server-side encryption algorithm. This value can be the AWS KMS arn key, to be used for the Amazon S3 header \&quot;x-amz-server-side-encryption-aws-kms-key-id\&quot; value. Value will be ignored if encryption is \&quot;AES256\&quot; | [optional] 

## Example

```python
from libica.openapi.v3.models.aws_temp_credentials import AwsTempCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTempCredentials from a JSON string
aws_temp_credentials_instance = AwsTempCredentials.from_json(json)
# print the JSON string representation of the object
print(AwsTempCredentials.to_json())

# convert the object into a dict
aws_temp_credentials_dict = aws_temp_credentials_instance.to_dict()
# create an instance of AwsTempCredentials from a dict
aws_temp_credentials_from_dict = AwsTempCredentials.from_dict(aws_temp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


