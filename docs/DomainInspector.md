# DomainInspector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Value to use for subsequent requests. | [optional] 
**aggregate_delay** | **int** | Offset of entry timestamps from the current time due to processing time. | [optional] 
**data** | [**[DomainInspectorRealtimeEntry]**](DomainInspectorRealtimeEntry.md) | A list of report [entries](#entry-data-model), each representing one second of time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


