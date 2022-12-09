# WsMessageFormat

Payload format for delivering to subscribers of WebSocket messages. One of `content` or `content-bin` must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content of a WebSocket `TEXT` message. | [optional] 
**content_bin** | **str** | The base64-encoded content of a WebSocket `BINARY` message. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


