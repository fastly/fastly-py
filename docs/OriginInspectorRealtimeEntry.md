# OriginInspectorRealtimeEntry

Each reporting period is represented by an entry in the `Data` property of the top level response and provides access to [measurement data](#measurements-data-model) for that time period, grouped by origin name and optionally by POP. The `datacenter` property organizes the measurements by Fastly POP, while the `aggregated` property combines the measurements of all POPs. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recorded** | **int** | The Unix timestamp at which this record&#39;s data was generated. | [optional] 
**aggregated** | [**{str: (OriginInspectorMeasurements,)}**](OriginInspectorMeasurements.md) | Groups [measurements](#measurements-data-model) by backend name. | [optional] 
**datacenter** | **{str: ({str: (OriginInspectorMeasurements,)},)}** | Groups [measurements](#measurements-data-model) by POP, then backend name. See the [POPs API](https://www.fastly.com/documentation/reference/api/utils/pops/) for details about POP identifiers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


