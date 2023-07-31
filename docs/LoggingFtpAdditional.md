# LoggingFtpAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An hostname or IPv4 address. | [optional] 
**hostname** | **str** | Hostname used. | [optional] 
**ipv4** | **str** | IPv4 address of the host. | [optional] 
**password** | **str** | The password for the server. For anonymous use an email address. | [optional] 
**path** | **str** | The path to upload log files to. If the path ends in `/` then it is treated as a directory. | [optional] 
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**user** | **str** | The username for the server. Can be anonymous. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


