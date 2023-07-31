# LoggingSftpAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference. | [optional] 
**path** | **str, none_type** | The path to upload logs to. | [optional]  if omitted the server will use the default value of "null"
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**secret_key** | **str, none_type** | The SSH private key for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference. | [optional]  if omitted the server will use the default value of "null"
**ssh_known_hosts** | **str** | A list of host keys for all hosts we can connect to over SFTP. | [optional] 
**user** | **str** | The username for the server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


