# Realtime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Value to use for subsequent requests. | [optional] 
**aggregate_delay** | **int** | How long the system will wait before aggregating messages for each second. The most recent data returned will have happened at the moment of the request, minus the aggregation delay. | [optional] 
**data** | [**[RealtimeEntry]**](RealtimeEntry.md) | A list of [records](#record-data-model), each representing one second of time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


