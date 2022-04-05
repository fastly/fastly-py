# LoggingFtpResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the real-time logging configuration. | [optional] 
**placement** | **str, none_type** | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional] 
**format_version** | **int** | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.   | [optional]  if omitted the server will use the default value of 2
**response_condition** | **str, none_type** | The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional] 
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional]  if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
**message_type** | **str** | How the message should be formatted. | [optional]  if omitted the server will use the default value of "classic"
**timestamp_format** | **str, none_type** | A timestamp format | [optional] [readonly] 
**period** | **int** | How frequently log files are finalized so they can be available for reading (in seconds). | [optional]  if omitted the server will use the default value of 3600
**gzip_level** | **int** | What level of gzip encoding to have when sending logs (default `0`, no compression). If an explicit non-zero value is set, then `compression_codec` will default to \&quot;gzip.\&quot; Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional]  if omitted the server will use the default value of 0
**compression_codec** | **str** | The codec used for compression of your logs. Valid values are `zstd`, `snappy`, and `gzip`. If the specified codec is \&quot;gzip\&quot;, `gzip_level` will default to 3. To specify a different level, leave `compression_codec` blank and explicitly set the level using `gzip_level`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional] 
**address** | **str** | An hostname or IPv4 address. | [optional] 
**hostname** | **str** | Hostname used. | [optional] 
**ipv4** | **str** | IPv4 address of the host. | [optional] 
**password** | **str** | The password for the server. For anonymous use an email address. | [optional] 
**path** | **str** | The path to upload log files to. If the path ends in `/` then it is treated as a directory. | [optional] 
**port** | **int** | The port number. | [optional]  if omitted the server will use the default value of 21
**public_key** | **str, none_type** | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional]  if omitted the server will use the default value of "null"
**user** | **str** | The username for the server. Can be anonymous. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**service_id** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**version** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

