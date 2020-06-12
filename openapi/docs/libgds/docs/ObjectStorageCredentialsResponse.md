# ObjectStorageCredentialsResponse

The temporaryUploadCredentials/objectStorageCredentialsResponse will be deprecated. Use objectStoreAccess/awsS3TemporaryUploadCredentials instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Access key for use with AWS S3 | [optional] 
**secret_key** | **str** | Secret key for use with AWS S3 | [optional] 
**session_token** | **str** | Token for use with AWS S3 | [optional] 
**region** | **str** | AWS region the folder will/does reside in | [optional] 
**bucket_name** | **str** | AWS bucket the folder will/does reside in | [optional] 
**service_url** | **str** | Service URL for multi-regional support | [optional] 
**upload_location** | **str** | AWS upload location for this folder | [optional] 
**expiration_date** | **datetime** | expiration for temporary credentials | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


