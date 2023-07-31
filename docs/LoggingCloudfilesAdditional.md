# LoggingCloudfilesAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Your Cloud Files account access key. | [optional] 
**bucket_name** | **str** | The name of your Cloud Files container. | [optional] 
**path** | **str, none_type** | The path to upload logs to. | [optional]  if omitted the server will use the default value of "null"
**region** | **str, none_type** | The region to stream logs to. | [optional] 
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**user** | **str** | The username for your Cloud Files account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


