# AWSDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the s3 bucket | 
**key_prefix** | **str** | Key prefix within the bucket for ICA to operate within. Data may only be created having this prefix and the given credentials will only give access to it. If not set, default is to allow operation on the full bucket. No leading slash, and must end with a trailing slash. | [optional] 
**server_side_encryption_algorithm** | **str** | Used to specify the type of server-side encryption (SSE) to be used on the object provider. This value is used to determine the Amazon S3 header \&quot;x-amz-server-side-encryption\&quot; value. For example, specify \&quot;AES256\&quot; for SSE-S3, or \&quot;AWS:KMS\&quot; for SSE-KMS. By default if none is specified, \&quot;AES256\&quot; will be used. | [optional] 
**server_side_encryption_key** | **str** | Used to specify the server-side encryption key that might be associated with the specified server-side encryption algorithm. This value can be the AWS KMS arn key, to be used for the Amazon S3 header \&quot;x-amz-server-side-encryption-aws-kms-key-id\&quot; value. Value will be ignored if encryption is \&quot;AES256\&quot;. | [optional] 

## Example

```python
from libica.openapi.v3.models.aws_details import AWSDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AWSDetails from a JSON string
aws_details_instance = AWSDetails.from_json(json)
# print the JSON string representation of the object
print(AWSDetails.to_json())

# convert the object into a dict
aws_details_dict = aws_details_instance.to_dict()
# create an instance of AWSDetails from a dict
aws_details_from_dict = AWSDetails.from_dict(aws_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


