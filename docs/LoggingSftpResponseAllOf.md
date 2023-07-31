# LoggingSftpResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A hostname or IPv4 address. | [optional] 
**port** | **str** | The port number. | [optional]  if omitted the server will use the default value of "22"
**period** | **str** | How frequently log files are finalized so they can be available for reading (in seconds). | [optional]  if omitted the server will use the default value of "3600"
**gzip_level** | **int** | The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


