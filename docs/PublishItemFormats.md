# PublishItemFormats

Transport-specific message payload representations to be used for delivery. At least one format (`http-response`, `http-stream`, and/or `ws-message`) must be specified. Messages are only delivered to subscribers interested in the provided formats. For example, the `ws-message` format will only be sent to WebSocket clients.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_response** | [**HttpResponseFormat**](HttpResponseFormat.md) |  | [optional] 
**http_stream** | [**HttpStreamFormat**](HttpStreamFormat.md) |  | [optional] 
**ws_message** | [**WsMessageFormat**](WsMessageFormat.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


