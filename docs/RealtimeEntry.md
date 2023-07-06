# RealtimeEntry

A list of records, each representing one second of time. The `Data` property provides access to [measurement data](#measurements-data-model) for that time period, grouped in various ways.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recorded** | [**RealtimeEntryRecorded**](RealtimeEntryRecorded.md) |  | [optional] 
**aggregated** | [**RealtimeEntryAggregated**](RealtimeEntryAggregated.md) |  | [optional] 
**datacenter** | [**RealtimeEntryDatacenter**](RealtimeEntryDatacenter.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


