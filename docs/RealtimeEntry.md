# RealtimeEntry

A list of records, each representing one second of time. The `Data` property provides access to [measurement data](#measurements-data-model) for that time period, grouped in various ways.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recorded** | **int** | The Unix timestamp at which this record&#39;s data was generated. | [optional] 
**aggregated** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Aggregates [measurements](#measurements-data-model) across all Fastly POPs. | [optional] 
**datacenter** | [**{str: (RealtimeMeasurements,)}**](RealtimeMeasurements.md) | Groups [measurements](#measurements-data-model) by POP. See the [POPs API](/reference/api/utils/pops/) for details of POP identifiers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


