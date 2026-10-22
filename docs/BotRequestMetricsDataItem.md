# BotRequestMetricsDataItem

A time series data item containing bot request metric counts. The `bot` field is present when grouped by bot. The `datacenter` field is present when grouped by data center. This dataset is sparse, meaning only keys with non-zero values are included. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp for the time series being reported. | [optional] 
**bot** | **str** | Bot identifier for which data was recorded. Present only when grouped by bot. | [optional] 
**datacenter** | **str** | Datacenter (POP) for which data was recorded. Present only when grouped by datacenter. | [optional] 
**bot_edge_requests_allowed_count** | **int** | Count of edge requests where a bot was detected and the request was allowed by the configured policy. | [optional] 
**bot_edge_requests_challenged_count** | **int** | Count of edge requests where a bot was detected and a client challenge was issued for the request by the configured policy. | [optional] 
**bot_edge_requests_blocked_count** | **int** | Count of edge requests where a bot was detected and the request was blocked by the configured policy. | [optional] 
**bot_edge_requests_challenge_token_valid_count** | **int** | Count of edge requests where a bot was detected and the client making the request has already solved a challenge issued by the configured policy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


