# LoggingSyslogAdditional


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | [**LoggingMessageType**](LoggingMessageType.md) |  | [optional] 
**hostname** | **str** | The hostname used for the syslog endpoint. | [optional] 
**ipv4** | **str, none_type** | The IPv4 address used for the syslog endpoint. | [optional] 
**token** | **str, none_type** | Whether to prepend each message with a specific token. | [optional]  if omitted the server will use the default value of "null"
**use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


