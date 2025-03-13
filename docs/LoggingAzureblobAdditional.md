# LoggingAzureblobAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str, none_type** | The path to upload logs to. | [optional]  if omitted the server will use the default value of "null"
**account_name** | **str** | The unique Azure Blob Storage namespace in which your data objects are stored. Required. | [optional] 
**container** | **str** | The name of the Azure Blob Storage container in which to store logs. Required. | [optional] 
**sas_token** | **str** | The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required. | [optional] 
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**file_max_bytes** | **int** | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB). Note that Microsoft Azure Storage has [block size limits](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block?tabs&#x3D;microsoft-entra-id#remarks). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


