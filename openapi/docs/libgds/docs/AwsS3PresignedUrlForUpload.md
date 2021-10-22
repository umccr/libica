# AwsS3PresignedUrlForUpload

AwsS3PresignedUrlForUpload
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**single_part_url** | **str** | A single part presigned url for upload | [optional] 
**multipart_template** | **str** | A url template for multi parts presigned url for upload | [optional] 
**multipart_signatures** | [**list[PartInfo]**](PartInfo.md) | Multi parts info that needs to be applied to the MultipartTemplate | [optional] 
**multipart_upload_id** | **str** | Multi part upload id | [optional] 
**server_side_encryption_algorithm** | **str** | The server side encryption method used by S3.  This value is used to determine the Amazon S3 header \&quot;x-amz-server-side-encryption\&quot; value.  Possible values: &#39;AES256&#39; and &#39;aws:kms&#39;. | [optional] 
**server_side_encryption_key** | **str** | Server-side encryption key that might be associated with the specified server-side encryption algorithm  This value can be the AWS KMS arn key, to be used for the Amazon S3 header \&quot;x-amz-server-side-encryption-aws-kms-key-id\&quot; value  This is only used when ServerSideEncryptionAlgorithm is &#39;aws:kms&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


