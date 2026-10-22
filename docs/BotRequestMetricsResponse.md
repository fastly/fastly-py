# BotRequestMetricsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[BotRequestMetricsDataItem]**](BotRequestMetricsDataItem.md) | An array of time series data items containing metric counts. Items are grouped by `timestamp` by default, or by a combination of `timestamp` and `bot` or `datacenter` or `region` when the `group_by` parameter is set. This dataset is sparse: only keys with non-zero values are included.  | [optional] 
**meta** | [**BotRequestMetricsMetadata**](BotRequestMetricsMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


