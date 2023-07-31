# LoggingDigitaloceanAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the DigitalOcean Space. | [optional] 
**access_key** | **str** | Your DigitalOcean Spaces account access key. | [optional] 
**secret_key** | **str** | Your DigitalOcean Spaces account secret key. | [optional] 
**domain** | **str** | The domain of the DigitalOcean Spaces endpoint. | [optional]  if omitted the server will use the default value of "nyc3.digitaloceanspaces.com"
**path** | **str, none_type** | The path to upload logs to. | [optional]  if omitted the server will use the default value of "null"
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


