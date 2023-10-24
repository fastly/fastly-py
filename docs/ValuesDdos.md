# ValuesDdos

The results of the query, optionally filtered and grouped over the requested timespan.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddos_action_limit_streams_connections** | **int** | For HTTP/2, the number of connections the limit-streams action was applied to. The limit-streams action caps the allowed number of concurrent streams in a connection. | [optional] 
**ddos_action_limit_streams_requests** | **int** | For HTTP/2, the number of requests made on a connection for which the limit-streams action was taken. The limit-streams action caps the allowed number of concurrent streams in a connection. | [optional] 
**ddos_action_tarpit_accept** | **int** | The number of times the tarpit-accept action was taken. The tarpit-accept action adds a delay when accepting future connections. | [optional] 
**ddos_action_tarpit** | **int** | The number of times the tarpit action was taken. The tarpit action delays writing the response to the client. | [optional] 
**ddos_action_close** | **int** | The number of times the close action was taken. The close action aborts the connection as soon as possible. The close action takes effect either right after accept, right after the client hello, or right after the response was sent. | [optional] 
**ddos_action_blackhole** | **int** | The number of times the blackhole action was taken. The blackhole action quietly closes a TCP connection without sending a reset. The blackhole action quietly closes a TCP connection without notifying its peer (all TCP state is dropped). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


