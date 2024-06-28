# LoggingS3Additional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str, none_type** | The access key for your S3 account. Not required if `iam_role` is provided. | [optional] 
**acl** | **str** | The access control list (ACL) specific request header. See the AWS documentation for [Access Control List (ACL) Specific Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html#initiate-mpu-acl-specific-request-headers) for more information. | [optional] 
**bucket_name** | **str** | The bucket name for S3 account. | [optional] 
**domain** | **str** | The domain of the Amazon S3 endpoint. | [optional] 
**iam_role** | **str, none_type** | The Amazon Resource Name (ARN) for the IAM role granting Fastly access to S3. Not required if `access_key` and `secret_key` are provided. | [optional] 
**path** | **str, none_type** | The path to upload logs to. | [optional]  if omitted the server will use the default value of "null"
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**redundancy** | **str, none_type** | The S3 redundancy level. | [optional]  if omitted the server will use the default value of "null"
**secret_key** | **str, none_type** | The secret key for your S3 account. Not required if `iam_role` is provided. | [optional] 
**server_side_encryption_kms_key_id** | **str, none_type** | Optional server-side KMS Key Id. Must be set if `server_side_encryption` is set to `aws:kms` or `AES256`. | [optional]  if omitted the server will use the default value of "null"
**server_side_encryption** | **str, none_type** | Set this to `AES256` or `aws:kms` to enable S3 Server Side Encryption. | [optional]  if omitted the server will use the default value of "null"
**file_max_bytes** | **int** | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


