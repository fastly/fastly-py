# LoggingHttpsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the real-time logging configuration. | [optional] 
**placement** | **str, none_type** | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional] 
**response_condition** | **str, none_type** | The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional] 
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional]  if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
**format_version** | **str** | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional]  if omitted the server will use the default value of "2"
**tls_ca_cert** | **str, none_type** | A secure certificate to authenticate a server with. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_client_cert** | **str, none_type** | The client certificate used to make authenticated requests. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_client_key** | **str, none_type** | The client private key used to make authenticated requests. Must be in PEM format. | [optional]  if omitted the server will use the default value of "null"
**tls_hostname** | **str, none_type** | The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional]  if omitted the server will use the default value of "null"
**request_max_entries** | **int** | The maximum number of logs sent in one request. Defaults `0` (10k). | [optional]  if omitted the server will use the default value of 0
**request_max_bytes** | **int** | The maximum number of bytes sent in one request. Defaults `0` (100MB). | [optional]  if omitted the server will use the default value of 0
**url** | **str** | The URL to send logs to. Must use HTTPS. Required. | [optional] 
**content_type** | **str, none_type** | Content type of the header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**header_name** | **str, none_type** | Name of the custom header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**message_type** | [**LoggingMessageType**](LoggingMessageType.md) |  | [optional] 
**header_value** | **str, none_type** | Value of the custom header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**method** | **str** | HTTP method used for request. | [optional]  if omitted the server will use the default value of "POST"
**json_format** | **str** | Enforces valid JSON formatting for log entries. | [optional] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**service_id** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


