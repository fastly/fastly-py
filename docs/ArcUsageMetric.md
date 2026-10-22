# ArcUsageMetric

A usage metric measured for a single date (or hour, when `granularity` is `hourly`).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | The date (or hour) the usage was measured. Formatted as `YYYY-MM-DD` when `granularity` is `daily`, or `YYYY-MM-DD HH:00:00` when `granularity` is `hourly`.  | 
**usage_type** | **str** | The type of usage being measured. | 
**quantity** | **int** | The quantity of the usage type for this date. | 
**virtual_key_id** | **str** | The ID of the virtual key this usage is attributed to. | [optional] 
**virtual_key_name** | **str** | The display name of the virtual key this usage is attributed to. | [optional] 
**primary_provider** | **str** | The ID of the provider connection originally requested, before any failover occurred. | [optional] 
**provider** | **str** | The name of the provider connection that ultimately served the request. | [optional] 
**provider_connection_id** | **str** | The ID of the provider connection that ultimately served the request. | [optional] 
**model** | **str** | The AI model identifier used. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


