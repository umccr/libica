# AwsTempCredentials

In case of AWS S3 stored data, this will contain the credentials for uploading or downloading the data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | The S3 access key. | 
**secret_key** | **str** | The S3 secret key. | 
**session_token** | **str** | The S3 session token. | 
**region** | **str** | The S3 region. | 
**bucket** | **str** | The S3 bucket name. | 
**object_prefix** | **str** | The S3 object prefix these temporary credentials will give access to. | 
**server_side_encryption_algorithm** | **str, none_type** | Used to specify the type of server-side encryption (SSE) to be used on the object provider. This value is used to determine the Amazon S3 header \&quot;x-amz-server-side-encryption\&quot; value. For example, specify \&quot;AES256\&quot; for SSE-S3, or \&quot;AWS:KMS\&quot; for SSE-KMS. By default if none is specified, \&quot;AES256\&quot; will be used. | [optional] 
**server_side_encryption_key** | **str, none_type** | Used to specify the server-side encryption key that might be associated with the specified server-side encryption algorithm. This value can be the AWS KMS arn key, to be used for the Amazon S3 header \&quot;x-amz-server-side-encryption-aws-kms-key-id\&quot; value. Value will be ignored if encryption is \&quot;AES256\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


