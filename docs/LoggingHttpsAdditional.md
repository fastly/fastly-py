# LoggingHttpsAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send logs to. Must use HTTPS. Required. | [optional] 
**request_max_entries** | **int** | The maximum number of logs sent in one request. Defaults `0` (10k). | [optional]  if omitted the server will use the default value of 0
**request_max_bytes** | **int** | The maximum number of bytes sent in one request. Defaults `0` (100MB). | [optional]  if omitted the server will use the default value of 0
**content_type** | **str, none_type** | Content type of the header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**header_name** | **str, none_type** | Name of the custom header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**message_type** | [**LoggingMessageType**](LoggingMessageType.md) |  | [optional] 
**header_value** | **str, none_type** | Value of the custom header sent with the request. | [optional]  if omitted the server will use the default value of "null"
**method** | **str** | HTTP method used for request. | [optional]  if omitted the server will use the default value of "POST"
**json_format** | **str** | Enforces valid JSON formatting for log entries. | [optional] 
**format** | **str** | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional]  if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


