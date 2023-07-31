# LoggingGcsAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the GCS bucket. | [optional] 
**path** | **str** |  | [optional]  if omitted the server will use the default value of "/"
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**project_id** | **str** | Your Google Cloud Platform project ID. Required | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


